import requests
from bs4 import BeautifulSoup
import csv

# URL of the product listings
url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"

# Send a GET request to the URL
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the product divs
product_divs = soup.find_all('div', class_='s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t2 puis-include-content-margin puis s-latency-cf-section s-card-border')

# Prepare the CSV file to store the scraped data
csv_file = open('product_data.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(csv_file)

# Write the header row to the CSV file
header = ['Product Name', 'Price', 'Rating', 'Reviews']
writer.writerow(header)

# Iterate over each product div and extract the required information
for product_div in product_divs:
    # Find the product name
    product_name = product_div.find('span', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal').text.strip()

    # Find the product price
    product_price = product_div.find('span', class_='a-price-whole').text.strip()

    # Find the product rating
    product_rating = product_div.find('span', class_='a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom').text.strip()

    # Find the product reviews
    product_reviews = product_div.find('span', class_='a-size-base s-underline-text').text.strip()

    # Write the extracted information to the CSV file
    writer.writerow([product_name, product_price, product_rating, product_reviews])

# Close the CSV file
csv_file.close()
