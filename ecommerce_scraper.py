from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import pandas as pd 

# Constants for file names
INPUT_CSV = "input.csv"
PRODUCT_DATA_CSV = "product_data.csv"



def scrape_amazon(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    try:
        # Scraping the product title
        title_element = WebDriverWait(driver,40).until(
            EC.presence_of_element_located((By.ID, 'productTitle'))
        )
        title = title_element.text.strip()

        # Scraping the product price
        price_element = WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.ID, 'a-price-whole'))
        )
        price = price_element.text.strip()

        # Manually setting the ecommerce platform to 'Amazon'
        ecommerce = 'Amazon'
        print(title)

        # Constructing the product data dictionary
        product_data = {
            'title': title,
            'url': url,
            'price': price,
            'ecommerce': ecommerce,
        }

        return product_data
    finally:
        driver.quit()
def scrape_flipkart(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    try:
        # Scraping the product title (adjust the selector as per Flipkart's HTML structure)
        title_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, '_35KyD6'))
        )
        title = title_element.text.strip()

        # Scraping the product price (adjust the selector as per Flipkart's HTML structure)
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, '_16Jk6d'))
        )
        price = price_element.text.strip()

        # Manually setting the ecommerce platform to 'Flipkart'
        ecommerce = 'Flipkart'

        # Constructing the product data dictionary
        product_data = {
            'title': title,
            'url': url,
            'price': price,
            'ecommerce': ecommerce,
        }

        return product_data
    finally:
        driver.quit()

def scrape_maple(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    try:
        # Scraping the product title (adjust the selector as per Maple's HTML structure)
        title_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.product-title'))
        )
        title = title_element.text.strip()

        # Scraping the product price (adjust the selector as per Maple's HTML structure)
        price_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.a-price-whole'))
        )
        price = price_element.text.strip()

        # Manually setting the ecommerce platform to 'Maple'
        ecommerce = 'Maple'

        # Constructing the product data dictionary
        product_data = {
            'title': title,
            'url': url,
            'price': price,
            'ecommerce': ecommerce,
        }

        return product_data
    finally:
        driver.quit()


def scrape_product_data(input_csv):
    with open(input_csv, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amazon_url = row['url']
            product_data = scrape_amazon(amazon_url)

            # Scraping data from Flipkart 
            flipkart_data = scrape_flipkart(product_data['title'])
            maple_data = scrape_maple(product_data['title'])

            # Store data in a CSV file
            with open('product_data.csv', 'a', newline='') as out_file:
                writer = csv.writer(out_file)
                writer.writerow([product_data['title'], product_data['url'],
                                 flipkart_data['price'], maple_data['price']])



# Example usage:
if __name__ == "__main__":
    # Step 1: Scrape product data from Amazon
    scrape_product_data('input.csv')

