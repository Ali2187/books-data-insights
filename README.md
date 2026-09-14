# books-data-insights
End-to-end book data analysis project covering web scraping, data cleaning, EDA, visualization, and interactive dashboard development.
## Project Overview
This project collects book data through web scraping and transforms the raw data into a clean and structured dataset ready for analysis.

The project demonstrates a complete data workflow:

**Web Scraping → Data Cleaning → Exploratory Data Analysis → Visualization → Dashboard**

The goal is to extract useful insights from book-related data such as prices, ratings, availability, categories, and reviews.
## libraries used
- pandas 
- matplotlib
- seaborn
- requests
- BeautifulSoup
- time
- re
- streamlit
- plotly
##  Project Workflow
### 1. Web Scraping

Book information was collected from the website using:

- `Requests`
- `BeautifulSoup`
- `lxml`

The scraper extracts information from multiple pages and product pages.

### 2. Data Collection

The collected data was stored in a structured CSV dataset.

### 3. Data Cleaning

The dataset was cleaned and prepared for analysis by:

- Handling missing values
- Removing duplicate records
- Cleaning text columns
- Converting numerical columns to appropriate data types
- Extracting numerical values from scraped data
- Checking data consistency

### 1. Web Scraping

Book information was collected from the website using:

- `Requests`
- `BeautifulSoup`
- `lxml`

The scraper extracts information from multiple pages and product pages.

### 2. Data Collection

The collected data was stored in a structured CSV dataset.

### 3. Data Cleaning

The dataset was cleaned and prepared for analysis by:

- Handling missing values
- Removing duplicate records
- Cleaning text columns
- Converting numerical columns to appropriate data types
- Extracting numerical values from scraped data
- Checking data consistency

## 5. Data Visualization

Different visualizations were created using Matplotlib and Seaborn to make the findings easier to understand.

### 6. Dashboard

An interactive dashboard was developed to allow users to explore the dataset using filters and visualizations.

## Dataset

The dataset contains information about 1000 books and includes 15 features.

 Column ==> Description 
---==>---
 `title` ==> Book title 
 `price` ==> Book price 
 `rating` ==> Book rating
 `Availability` ==> Book availability status 
 `Stock_Count` ==> Number of books in stock 
 `Category` ==> Book category 
 `UPC` ==> Unique product code 
 `Product_Type` ==> Product type 
 `Price_Excl_Tax` ==> Price excluding tax 
 `Price_Incl_Tax` ==> Price including tax 
 `Tax` ==> Tax amount 
 `Number_of_Reviews` ==> Number of reviews 
 `Description` ==> Book description 
 `Product_URL` ==> Product page URL 
 `Image_URL` ==> Book image URL 

## <img width="1057" height="450" alt="newplot (3)" src="https://github.com/user-attachments/assets/1c0c3190-4059-4831-a929-9e4cdf1edec4" />
 Data Types

### Numerical Features

- `price`
- `rating`
- `Stock_Count`
- `Price_Excl_Tax`
- `Price_Incl_Tax`
- `Tax`
- `Number_of_Reviews`

### Text Features

- `title`
- `Availability`
- `Category`
- `UPC`
- `Product_Type`
- `Description`

### URL Features

- `Product_URL`
- `Image_URL`

## 📈 Data Analysis

The exploratory analysis focuses on understanding the characteristics of the book dataset.

### Rating Analysis

The distribution of book ratings was analyzed to understand how books are rated.
<img width="2400" height="1500" alt="rating_distribution" src="https://github.com/user-attachments/assets/131e2197-3bea-4ebc-a058-94ecd97ed77e" />

### Price Analysis

Book prices were analyzed to understand their distribution and variation.

<img width="3000" height="1800" alt="price_distribution" src="https://github.com/user-attachments/assets/f6a191d9-deb6-4988-843d-73c6b92b401f" />
### Correlation Analysis

A correlation analysis was performed to examine relationships between numerical variables.

<img width="3000" height="2400" alt="correlation_matrix" src="https://github.com/user-attachments/assets/3bbb8fb4-9802-49b0-b2fa-fa9761536d64" />

##  Interactive Dashboard

An interactive dashboard was developed to explore the book dataset.

The dashboard allows users to filter and analyze the data based on different attributes.

<img width="1917" height="861" alt="image" src="https://github.com/user-attachments/assets/b37cd9a8-375d-4774-9cd4-2c3f270ddd48" />
