import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_all_h2_headers(url):
    array1 = []
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)  
        response.raise_for_status()  
    except requests.RequestException as e:
        print(f"Failde to fetch the page, - {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    h2_tags = soup.find_all("h2")
    for h2 in h2_tags:
        header_text = h2.get_text()
        if header_text and header_text.lower() != "contents":
            array1.append(header_text)
    
    for item in array1[:10]:
        print(item)
    


get_all_h2_headers(URL)