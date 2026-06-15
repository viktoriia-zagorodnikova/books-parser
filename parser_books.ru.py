import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def collect_books():
    page_num = 1
    data = []

    while True:
        url = f'https://books.toscrape.com/catalogue/page-{page_num}.html'
        html_content = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html_content, 'lxml')
        entries = soup.find_all('article', class_='product_pod')

        if len(entries) == 0:
            break

        for entry in entries:
            title = entry.find('h3').find('a')['title']
            rating = entry.find('p', class_='star-rating')['class'][1]
            price = entry.find('p', class_='price_color').text

            data.append({'title': title, 'rating': rating, 'price': price})

        page_num += 1

    return data

books = collect_books()
print(len(books))

df = pd.DataFrame(books)
df.to_excel('books.xlsx')