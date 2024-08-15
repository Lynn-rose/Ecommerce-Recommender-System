from django.shortcuts import render
from .models import Product
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

from django.core.exceptions import ObjectDoesNotExist

# Function to load and process product data from the CSV
def load_products():
    df = pd.read_csv('../products.csv', index_col='ID')  # Ensure 'ID' is treated as index
    
    for index, row in df.iterrows():
        Product.objects.update_or_create(
            #id=index,  # Use the ID from the DataFrame
            defaults={
                'category_1': row['category_1'],
                'category_2': row['category_2'],
                'category_3': row['category_3'],
                'title': row['title'],
                'product_rating': row['product_rating'],
                'selling_price': row['selling_price(KSH.)'],
                'mrp': row['mrp(KSH.)'],
                'seller_name': row['seller_name'],
                'seller_rating': row['seller_rating'],
                'price_ratio': row['price_ratio'],
                'price_difference': row['price_difference'],
            }
        )


# Function to create a recommendation model based on TF-IDF and cosine similarity
def create_recommendation_model():
    # Load all products into a DataFrame
    df = pd.DataFrame(list(Product.objects.all().values(
        'category_1', 'category_2', 'category_3', 'title', 'product_rating', 
        'selling_price', 'mrp', 'seller_name', 'seller_rating', 
        'price_ratio', 'price_difference'
    )))
    
    df['combined_features'] = (
        df['category_1'] + " " + df['category_2'] + " " + 
        df['category_3'] + " " + df['title']
    )
    
    # TF-IDF Vectorization
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['combined_features'])
    
    # Cosine Similarity Matrix
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    return df, cosine_sim


def recommend_products(query):
    query = str(query).strip()
    
    # Create the recommendation model
    df, cosine_sim = create_recommendation_model()
    
    if not query:
        return []
    
    # Find the index of the product that matches the query
    query_index = df[df['title'].str.contains(query, case=False, na=False)].index.tolist()
    
    if not query_index:
        return []
    
    # Get the first matching index
    query_index = query_index[0]
    
    # Calculate similarity scores
    sim_scores = list(enumerate(cosine_sim[query_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the indices of the top 10 most similar products
    sim_scores = sim_scores[1:11]
    product_indices = [i[0] for i in sim_scores]
    
    # Extract the recommended products from the DataFrame
    recommendations = df.iloc[product_indices][['title', 'product_rating', 'selling_price']]
    
    # Convert the DataFrame to a list of dictionaries and return it
    return recommendations.to_dict(orient='records')


def search_view(request):
    # Get the search query from the request
    query = request.get('title')[0].get('title').get('product_rating').get('selling_price')

    # Get the recommendations based on the query
    recommendations = recommend_products(query)
    
    # Render the template and pass the recommendations to it
    return render(request, 'recommendations.html', {'recommendations': recommendations})


# Home view to display top-rated products
def home(request):
    top_rated_products = Product.objects.order_by('-product_rating')[:12]  # Fetch top 10 rated products
    return render(request, 'products/home.html', {'top_rated_products': top_rated_products})
