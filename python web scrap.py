#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
from bs4 import BeautifulSoup
import csv

# URL of the Books to Scrape website
url = "https://books.toscrape.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}

response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    books = soup.find_all(class_="product_pod")

    # Open a CSV file to write the data
    with open("books_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["Title", "Price", "Availability", "Link"])

        # Loop through each book and extract data
        for book in books:
            title = book.h3.a['title']
            price = book.find(class_="price_color").get_text(strip=True)
            availability = book.find(class_="availability").get_text(strip=True)
            # Extract the relative link and convert it to an absolute URL
            link = url + book.h3.a['href']
            
            # Write the book details into the CSV file
            writer.writerow([title, price, availability, link])
            
            # Print the book details (optional)
            print(f"Title: {title}\nPrice: {price}\nAvailability: {availability}\nLink: {link}\n{'-' * 40}")

    print("Data has been exported to books_data.csv successfully.")

else:
    print("Failed to retrieve the page, status code:", response.status_code)


# In[6]:


import requests
from bs4 import BeautifulSoup
import csv

# URL of the Books to Scrape website
url = "https://books.toscrape.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}

response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    books = soup.find_all(class_="product_pod")

    # Open a CSV file to write the data with UTF-8 encoding
    with open("books_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["Title", "Price", "Availability", "Link"])

        # Loop through each book and extract data
        for book in books:
            title = book.h3.a['title']
            price = book.find(class_="price_color").get_text(strip=True)
            availability = book.find(class_="availability").get_text(strip=True)
            # Extract the relative link and convert it to an absolute URL
            link = url + book.h3.a['href']
            
            # Write the book details into the CSV file
            writer.writerow([title, price, availability, link])
            
            # Print the book details (optional)
            print(f"Title: {title}\nPrice: {price}\nAvailability: {availability}\nLink: {link}\n{'-' * 40}")

    print("Data has been exported to books_data.csv successfully.")

else:
    print("Failed to retrieve the page, status code:", response.status_code)

