# 📚 Books Parser

**Tech stack:** Python · Requests · BeautifulSoup · lxml · Pandas · openpyxl

## 📋 Task

Parser collects information about 1000 books from [books.toscrape.com](https://books.toscrape.com) and saves the results to an Excel file.

## ✅ Each book contains

- 📖 Title
- ⭐ Rating
- 💰 Price

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install requests beautifulsoup4 lxml pandas openpyxl
```

### 2. Run the script
```bash
python books_parser.py
```

### 3. Get the result
The output will appear in `books.xlsx` in the project folder.

## 📊 Results Example

| title | rating | price |
|---|---|---|
| A Light in the Attic | Three | £51.77 |
| Tipping the Velvet | One | £53.74 |
| Sharp Objects | Four | £47.82 |

**Total collected:** 1000 books
