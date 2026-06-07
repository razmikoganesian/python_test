from ast import main
from urllib import response

import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import re

BASE_URL = "https://books.toscrape.com/"
IMAGE_DIR = "books_images"


def sanitize_file_name(title):
    return re.sub(r"[^\w\-_. ]", "", title).replace(" ", "_")


def download_images(image_url, filename):
    try:
        response = requests.get(image_url, stream=True, timeout=10)
        response.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

    except Exception as e:
        print(f"Failed to download file {e}")


def scrape_and_download_images():
    url = BASE_URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select(".product_pod")[:10]

    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)

    for book in books:
        title_tag = book.select_one("h3 > a")
        title = title_tag.get("title")
        image_tag = book.select_one(".image_container img")
        image = image_tag.get("src")
        image_url = urljoin(url, image)

        print(image_url)

        filename = sanitize_file_name(title) + ".jpg"
        filepath = os.path.join(IMAGE_DIR, filename)
        print(filepath)

        print(f"Downloading: {title} ")
        download_images(image_url, filepath)

    print("All books cover downloaded")


def main():
    scrape_and_download_images()


if __name__ == "__main__":
    main()
