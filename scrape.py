from bs4 import BeautifulSoup
import json
import cloudscraper
from slugify import slugify
import urllib.request

# To defeat cloudflare
URL = ""
scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'android',
        'desktop': False
    }
)

html = scraper.get(URL).text
soup = BeautifulSoup(html, 'html.parser')

# Grab the schema
schema = json.loads("".join(soup.find("script", {"type":"application/ld+json"}).contents))
product_name = schema['name']
product_price = schema['offers']['price']
product_url = "https:" + schema['image']

# Generate filename based on spec
file_name = slugify(product_name + ' ' + str(product_price))

# Download the image from the website
urllib.request.urlretrieve(product_url, file_name)
