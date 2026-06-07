import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"
START_PAGE = "catalogue/page-1.html"
OUTPUT_FILE = "books_data.json"
TARGET_COUNT = 70


def scrape_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

    except requests.RequestException as e:
        print(f"Failde to fetch URL {e}")
        return [], None

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for article in soup.select(".product_pod"):
        title_tag = article.select_one("h3 > a")
        title = title_tag.get("title")
        price_tag = article.select_one(".product_price > .price_color")
        raw_price = price_tag.text.strip()
        price = float(raw_price.replace("Â£", ""))

        # print(f"Title {title} and price is {price}")
        books.append({"title": title, "price" : price})

    next_button = soup.select_one(".next > a")
    next_link = next_button.get('href') if next_button else None
    # print(next_link)

    new_url = urljoin(url, str(next_link)) if next_link else None
    return books, new_url


def main():
    collected = []
    currrent_url = urljoin(BASE_URL, START_PAGE)

    while len(collected) < TARGET_COUNT and currrent_url:
        print(f"Scraping: {currrent_url} ")
        books, new_url = scrape_page(currrent_url)
        collected.extend(books)
        currrent_url = new_url


    collected = collected[:TARGET_COUNT]
    print(f"scraping {len(collected)} is Done! ")

    with open(OUTPUT_FILE, 'w', encoding="utf-8") as f:
        json.dump(collected, f, indent=2)
    print(f"Data saved to json {OUTPUT_FILE}")


if __name__ == "__main__" :
    main()

