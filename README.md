

# NewsFetcher: Top Headlines by Category & Query

## Overview

**NewsFetcher** is a Python-based tool that allows you to fetch, display, and save the latest news articles from around the web. Using the News API, this script retrieves top headlines by category or query and stores them in a readable format, making it easy to stay updated on trending topics in the US or Greece.

This lightweight and easy-to-use tool is perfect for journalists, researchers, or anyone who wants a simple way to collect and organize news articles.

---

## Features

* **Fetch Top Headlines**: Retrieve the latest articles from News API based on categories like `technology`, `sports`, `general`, and more.
* **Custom Queries**: Search for articles using any keyword or phrase, e.g., `"Elon Musk"`.
* **Multiple Regions**: Fetch news from different countries (currently US and Greece) by adjusting the country parameter.
* **Console Display**: Articles are printed nicely in the terminal with titles and URLs.
* **Save to Text File**: Automatically saves fetched articles to a `.txt` file named after the category or query for easy reference.
* **Easy to Use**: Minimal setup — just provide your News API key and a category or search term.

---

## Getting Started

### 1. Installation

Clone the repository:

```bash
git clone https://github.com/VasilisKokotakis/NewsAPI-Headlines-Fetcher.git
cd NewsAPI-Headlines-Fetcher
```

Install dependencies:

```bash
pip install requests
```

### 2. Configuration

Open the script and replace the placeholder with your News API key:

```python
API_KEY = 'YOUR_NEWS_API_KEY'
```

### 3. Running the Script

Fetch articles by category:

```bash
python3 News.py technology
```

Fetch articles by keyword query:

```bash
python3 News.py "Elon Musk"
```

If no argument is provided, it defaults to `general`.

### 4. Explore Results

* Articles are printed in the terminal.
* Articles are saved to a `.txt` file named after the category or query, e.g., `technology_articles.txt`.

---

## Dependencies

* Python 3.x
* [Requests](https://docs.python-requests.org/en/master/)
* [News API](https://newsapi.org/)

---

## Contributions

Contributions are welcome! You can submit new features, bug fixes, or improvements via pull requests. Ideas for enhancing search capabilities or supporting more countries are especially appreciated.

---

## License

MIT License

