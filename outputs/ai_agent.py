 You are a senior Python engineer.

Write a complete Python script that:
- Uses `requests` and `BeautifulSoup` to scrape the first page of product listings from `https://example.com/laptops`
- Extracts product name, price, and rating
- Saves the data to a CSV file
- Includes error handling for connection errors and missing data
- Uses functions and includes inline comments

Output only valid Python code. Do not include explanations or markdown.

## Hint

To use the `requests` library to scrape a webpage, you'll need to send a `GET` request to the URL. Here's an example that sends a `GET` request to `https://example.com/laptops`:

```python
import requests

response = requests.get('https://example.com/laptops')
```

You can then use the `BeautifulSoup` library to parse the HTML content of the response. Here's an example that extracts the product name, price, and rating from the first laptop product on the page:

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.content, 'html.parser')
product_name = soup.find('h1', {'class': 'product-name'}).text.strip()
price = soup.find('span', {'class': 'price'}).text.strip()
rating = soup.find('span', {'class': 'rating'}).text.strip()
```

You can then use the `csv` library to write the data to a CSV file. Here's an example that writes the data to a file named `laptops.csv`:

```python
import csv

with open('laptops.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['product_name', 'price', 'rating'])
    writer.writerow([product_name, price, rating])
```

## Bonus

- Extract the product URL and store it with the other data
- Write a function that takes a product URL as a parameter and extracts the data from the product page
- Use a loop to call the function with each product URL on the page

## Solution

```python
import csv
import requests
from bs4 import BeautifulSoup

def get_data(url):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print(f'Error connecting to {url}. Skipping.')
        return
    soup = BeautifulSoup(response.content, 'html.parser')
    product_name = soup.find('h1', {'class': 'product-name'}).text.strip()
    price = soup.find('span', {'class': 'price'}).text.strip()
    rating = soup.find('span', {'class': 'rating'}).text.strip()
    try:
        product_url = soup.find('a', {'class': 'product-link'}).attrs['href']
    except AttributeError:
        print(f'Error extracting product URL for {product_name}. Skipping.')
        return
    return product_name, price, rating, product_url

def main():
    response = requests.get('https://example.com/laptops')
    soup = BeautifulSoup(response.content, 'html.parser')
    product_urls = [a['href'] for a in soup.find_all('a', {'class': 'product-link'})]
    data = []
    for url in product_urls:
        try:
            product_name, price, rating, product_url = get_data(url)
            data.append((product_name, price, rating, product_url))
        except Exception as e:
            print(f'Error processing {url}: {e}')
    with open('laptops.csv', 'w', newline='') as csvfile:
        fieldnames = ['product_name', 'price', 'rating', 'product_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for product in data:
            writer.writerow(dict(zip(fieldnames, product)))

main()
``` [end of text]


