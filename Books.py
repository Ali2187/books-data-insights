import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re


# website Configuration
BASE_URL = "https://books.toscrape.com/"
current_url = BASE_URL + "index.html"
headers = {
    "User-Agent": "Mozilla/5.0"
}
#list to store all books
books=[]
while current_url:
    print('Scraping ' + current_url)
    # get current page
    response = requests.get(current_url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")

    # find all books in current page
    book_list= soup.find_all('article',{'class':'product_pod'})
    # Loop through books
    for book in book_list:
        # title
        title =book.find('h3').find('a')['title']
        # Price
        price = book.find('p',class_='price_color').text.strip()
        price =float(price.replace('£',''))
        # Rating
        rating_classes = book.find('p',class_='star-rating')['class']

        rating_map={
            'One':1,
            'Two':2,
            'Three':3,
            'Four':4,
            'Five':5,
        }

        rating=None
        for value in rating_classes:
            if value in rating_map:
                rating=rating_map[value]

            # Product URL
        book_link = book.find('h3').find('a')['href']

        product_url = requests.compat.urljoin(current_url, book_link)

        # Open book details page
        book_response = requests.get(product_url, headers=headers)
        book_soup = BeautifulSoup(book_response.content, "lxml")
        # Category
        breadcrumb = book_soup.find('ul',class_='breadcrumb')
        category = breadcrumb.find_all('a')[-1].text.strip()

        # Description
        description_div = book_soup.find('div',id='product_description')
        if description_div:
            description = description_div.find_next_sibling('p').text.strip()
        else:
            description = None

        # Image URL
        image = book_soup.find('div',class_='item active').find('img')['src']
        img_url = requests.compat.urljoin(product_url, image)

        # Product information table
        table = book_soup.find('table',class_='table-striped')

        product_info ={}

        for row in table.find_all('tr'):

            key = row.find('th').text.strip()
            value = row.find('td').text.strip()

            product_info[key] = value

        # UPC
        upc = product_info.get('UPC')

        # Product type
        product_type = product_info.get('Product Type')
        # Price excluding tax
        price_excl_tax = product_info.get('Price (excl. tax)')
        if price_excl_tax:
            price_excl_tax = float(price_excl_tax.replace('£',''))

        # Price including tax
        price_incl_tax = product_info.get('Price (incl. tax)')
        if price_incl_tax:
            price_incl_tax = float(price_incl_tax.replace('£',''))

        # Tax
        tax = product_info.get('Tax')
        if tax:
            tax = float(tax.replace('£',''))

        # Number of reviews
        reviews = product_info.get('Number of reviews')

        # Availability
        availability = product_info.get(
            "Availability"
        )
        # Stock Count
        stock = None

        if availability:

            stock_match = re.search(
                r"(\d+)\s+available",
                availability,
                re.IGNORECASE
            )

            if stock_match:
                stock = int(
                    stock_match.group(1)
                )
        # Save book
        books.append({
                'title':title,
                'price':price,
                'rating':rating,
                'Availability': availability,
                "Stock_Count": stock,
                "Category": category,
                "UPC": upc,
                "Product_Type": product_type,
                "Price_Excl_Tax": price_excl_tax,
                "Price_Incl_Tax": price_incl_tax,
                "Tax": tax,
                "Number_of_Reviews": reviews,
                "Description": description,
                "Product_URL": product_url,
                "Image_URL": img_url
            })
        print(
                "  Scraped:",
                title
            )

        # Small delay
        time.sleep(0.1)

    # Find next button
    next_button = soup.find('li',class_='next')
    if next_button:
        next_link = next_button.find('a')['href']
        # Convert next link to full URL
        current_url = requests.compat.urljoin(
            current_url,
            next_link
        )
    else:
        # No Next button = last page
        current_url = None

    time.sleep(0.5)

# Create DataFrame

df = pd.DataFrame(books)

print("\nTotal books:", len(df))

print("\nFirst 5 books:")

print(
    df.head()
)

# Save CSV
df.to_csv("books.csv", index=False, encoding='utf-8')

print(
    "\nbooks.csv created successfully!"
)