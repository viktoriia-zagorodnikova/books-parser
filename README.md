# 📚 Books Parser

## Task
Parser collects information about 1000 books from books.toscrape.com and saves to Excel.

Each book contains:
- 📖 Title
- ⭐ Rating
- 💰 Price

## How to run

Install libraries:
pip install requests beautifulsoup4 lxml pandas openpyxl

Run the file:
python parser_books.ru.py

Result will appear in books.xlsx file

## Results example

| title | rating | price |
|-------|--------|-------|
| A Light in the Attic | Three | £51.77 |
| Tipping the Velvet | One | £53.74 |
| Sharp Objects | Four | £47.82 |

Total collected: 1000 books
