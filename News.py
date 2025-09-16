import requests
from sys import argv

API_KEY = '******'

URL = 'https://newsapi.org/v2/top-headlines?'

def get_articles_by_category(category):
    query_parameters = {
        "category": category,
        "sortBy": "top",
        "country": "us",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters, category)


def get_articles_by_query(query):
    query_parameters = {
        "q": query,
        "sortBy": "top",
        "country": "gr",
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters, query)


def _get_articles(params, name_for_file):
    response = requests.get(URL, params=params)
    articles = response.json().get('articles', [])

    if not articles:
        print("No articles found!")
        return

    results = []
    output_lines = []

    for i, article in enumerate(articles, start=1):
        title = article.get("title", "No Title")
        url = article.get("url", "No URL")
        results.append({"title": title, "url": url})
        output_lines.append(f"{i}. {title}\n{url}\n")

    # Print to console
    print("\n".join(output_lines))

    # Save to text file
    filename = f"{name_for_file}_articles.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(line + "\n" for line in output_lines)

    print(f"\nSaved {len(results)} articles to {filename}")


def get_sources_by_category(category):
    url = 'https://newsapi.org/v2/top-headlines/sources'
    query_parameters = {
        "category": category,
        "language": "gr",
        "apiKey": API_KEY
    }

    response = requests.get(url, params=query_parameters)
    sources = response.json().get('sources', [])

    for source in sources:
        print(source.get('name', 'No Name'))
        print(source.get('url', 'No URL'))


if __name__ == "__main__":
    category = argv[1] if len(argv) > 1 else "general"
    print(f"Getting news for {category}...\n")
    get_articles_by_category(category)
    print(f"\nSuccessfully retrieved top {category} headlines")
