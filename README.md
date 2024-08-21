<!-- #region -->
# Ecommerce Recommender System
A recommendation system that gives users suggestions that best match user specs, enhancing online shopping by simplifying decisions and boosting customer satisfaction.

<p>
    <img src="Images/WhatsApp Image 2024-08-13 at 3.45.03 PM.jpeg" alt="readme Image"/>
</p>
<p align="center">
    <img src="https://img.shields.io/badge/-scikit--learn-F7931E?logo=scikit-learn&logoColor=white&style=flat-square">
    <img src="https://img.shields.io/badge/-Surprise-4B0082?logo=python&logoColor=white&style=flat-square">
    <img src="https://img.shields.io/badge/-Vercel-FF4B4B?logo=vercel&logoColor=white&style=flat-square">
    <img src="https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white&style=flat-square">
    <img src="https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white&style=flat-square">
    <img src="https://img.shields.io/badge/-NLTK-4EA94B?logo=python&logoColor=white&style=flat-square">
    <img src="https://img.shields.io/badge/-Seaborn-3776AB?logo=python&logoColor=white&style=flat-square">
    <img src="https://img.shields.io/badge/-Plotly-3F4F75?logo=plotly&logoColor=white&style=flat-square">
    <img src="https://img.shields.io/badge/-Django-3F4F75?logo=django&logoColor=white&style=flat-square">
</p>

#### Authors
* [Lynn Achieng](https://github.com/Lynn-rose)
* [Troye Gilbert](https://github.com/franchiseBoyz)
* [Edmund Nyaribo](https://github.com/EdmundNyaribo)
* [Josephine Maro]()
* [Pascalia Maiga](https://github.com/Passie2001)

## Introduction

The project aims to develop a chatbot that provides personalized product recommendations to online shoppers. With the vast array of choices on platforms like Amazon and Jumia, consumers often find it overwhelming to make quick decisions. This chatbot will simplify the shopping experience by analyzing user preferences and suggesting the best products based on their specifications. The goal is to enhance customer satisfaction, reduce decision-making time, and increase sales for businesses by offering tailored recommendations that meet the users' needs efficiently. This solution addresses the common issue of choice overload in online shopping.

## Objective

The goal is to Develop a recommendation system that provides accurate and relevant personalized product suggestions based on user specs, enhancing online shopping by simplifying decisions and boosting customer satisfaction. The model will help users make informed decisions when selecting products by considering their preferences and constraints.

## Project Overview

This project followed the CRISP-DM process. The CRISP-DM process is a data mining process model that describes commonly used approaches that data mining experts use to tackle problems. The CRISP-DM process is divided into six phases; Business Understanding, Data Understanding, Data Preparation, Modelling, Evaluation, and Deployment. The following is a brief description of each phase:

- **Business Understanding**: Exploring the business reasons for our data mining effort and what the company hopes to gain from the project.
- **Data Understanding**: The datasets we utilized comprised of csv files scraped from https://www.flipkart.com.
- **Data Preparation**: It mainly involved; selecting the data to discover the columns to be used, cleaning the data to correct and remove erroneous values, formatting the data to effectively perform mathematical operations and integrating the datasets to create a merged dataset for effective analysis.
- **Exploratory Data Analysis**: The goal of this procedure is to summarize the main characteristics of the dataset, which is often done visually.
- **Modelling**: To further support and provide insight we built a hybrid-based system.
- **Evaluation**: Accuracy Score, Mean Absolute Error abd Root Mean Squared Error were used to measure the average of absolute deviance between actual and predicted ratings given by users.
- **Recommendation and Conclusion**: It mainly involved interpreting our project findings, offering opinions based on the findings, proposing a solution to the gap discovered in the research that needs to be filled, and the next steps to be undertaken in future analysis.

## Setup Instructions

All these should be done in the terminal.

1. Clone the Repository:

    `git clone https://github.com/yourusername/your-repo-name.git`
    
     `cd your-repo-name`
     
2. Create and Activate a Virtual Environment:

 `python3 -m venv env`
 
 `source env/bin/activate`
 
 On Windows, use `env\Scripts\activate`
 
3. Create your branch and move into your branch

  `git checkout -b branch-name`
  
4. Install Dependencies:

Generate a `requirements.txt` file using this command

   `pip freeze > requirements.txt`
    
   Install the required packages:
    
   `pip install -r requirements.txt`


Backend Setup
1. Set Up the Database:
    Run the following commands to create and apply database migrations:
    
    `python manage.py makemigrations`
    
    `python manage.py migrate`
    
2. Create a Superuser:
    Create a superuser to access the Django admin panel:
    
    `python manage.py createsuperuser`
    
3. Run the Development Server: 

    `python manage.py runserver`    

Frontend Setup
If using plain HTML/CSS/JavaScript, ensure your static files are correctly placed in the `static` directory of your Django project.

Running the Application
1. Start the Backend Server:

    `python manage.py runserver`
    
2. Access the Application:
    Copy this url and paste it on the web browser `http://127.0.0.1:8000`

Usage
- Admin Panel: Access the Django admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.
- Task Management: Use the web interface to search and get recommendations for products.




## Our Data

We sourced data by scraping destination review data from **Flipkart** using a popular web scraping tool, [Scrapy](https://www.flipkart.com) 
Here's a breakdown of some of the main columns we used in coming up with recommendations:

* `id`: Unique identifier for each item.
* `category_1`: Contained a general category of the products eg. ‘Sports, Books and more.
* `category_2`: Contained a more specific category of category_1 eg. ‘Exercise Fitness’.
* `category_3`: contained a specified category of category_2 eg. Cardio Equipment.
* `title`: Holds the name and description of the product.
* `product_rating`: the rating of the product.
* `mrp `: marked retail price.
* `selling_price`: the retail selling price of the product.


There were a lot more columns in the data we scraped such as `sellername`, `sellerrating` and `highlights` that were dropped.
We also conducted feature engineering on some columns to capture more information. All this is well documented in the included project [**writeup**](https://github.com/Lynn-rose/Ecommerce-Recommender-System/blob/main/Documentation%20for%20Ecommerce%20recommendation%20System.docx.pdf).

## EDA

We conducted some EDA that yielded us some domain knowledge we could use to inform future steps and modelling
Some of the plots we came up with are shown below: 
<p align='center'>
    <img src="Images/Screenshot 2024-08-13 145700.jpg" alt="Distribution of categories"/>
    <img src="Images/Screenshot 2024-08-13 145751.jpg" alt="top 20 most rated category"/>
    <img src="Images/Screenshot 2024-08-13 145828.jpg" alt="price distribution in each category"/>
</p> 

## Modelling 

We built multiple models powered by different algorithms.
These include:
* `SVDpp`
* `SVD`
* `KNNwithMean`
* `Baseline Model(KNNBasic)`

The best performing ones were tuned and ensembled to produce one model however this did not exhibit better performance. Further scaling of the dataset was done and cross validation included to improve the accuracy score  
## Deployment

Included in the repository is a django user interface that serves as the rudimentary method through which users shall interact with our model. The interface was further deployed using **Railway**, this  is after integrating the web server with PostgreSQL.The link to the deployed version is [Ecommerce Recommender System](https://web-production-4170.up.railway.app/).

## Additional Documentation

As mentioned before included in this repository is the complete project documentation. This includes:
* [Non-technical presentation](https://github.com/Lynn-rose/Ecommerce-Recommender-System/blob/main/Ecommerce%20Recommender%20System.pdf).
* [Write-up documentation](https://github.com/Lynn-rose/Ecommerce-Recommender-System/blob/main/Documentation%20for%20Ecommerce%20recommendation%20System.docx.pdf).

<!-- #endregion -->

```python

```
