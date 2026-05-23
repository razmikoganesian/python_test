import requests
from bs4 import BeautifulSoup
import csv


URL = "https://news.ycombinator.com/"
CSV_FILE = "top20.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_titles_and_urls_(url):
    posts = []
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)  
        response.raise_for_status()  
    except requests.RequestException as e:
        print(f"Failde to fetch the page, - {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.select("span.titleline > a")

    for title in titles[:20]:
        title_text = title.text.strip()
        href = title.get("href")

        posts.append({"title": title_text, "url": href})

        # print(f"\n {title_text}. \n {href} \n\n")
    return posts


def save_in_csv(data):
    if not data:
        print("No data!!!")
        return
    
    with open(CSV_FILE, 'w', encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "url"])
        writer.writeheader()
        writer.writerows(data)
    print(f" Saved data to CSV {CSV_FILE}")

def main():
    print("Scrapping some data")
    posts = get_titles_and_urls_(URL)
    print("Collected all data")
    save_in_csv(posts)

        
if __name__ == "__main__":
    main()



get_titles_and_urls_(URL)