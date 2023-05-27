import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape product details from a given URL
def scrape_product_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find and return the required details
    description = soup.find('div', id='productDescription').text.strip()
    asin = soup.find('span', text='ASIN:').find_next('span').text.strip()
    product_description = soup.find('div', id='productDescription').text.strip()
    manufacturer = soup.find('a', id='bylineInfo').text.strip()

    return description, asin, product_description, manufacturer

# Read the CSV file containing product listings
csv_file = open('product_data.csv', 'r', encoding='utf-8')
reader = csv.reader(csv_file)
next(reader)  # Skip the header row

# Prepare the CSV file to store the complete product data
csv_file_complete = open('complete_product_data.csv', 'w', newline='', encoding='utf-8')
writer_complete = csv.writer(csv_file_complete)

