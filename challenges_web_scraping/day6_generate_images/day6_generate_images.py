import os
from click import wrap_text
import requests
import textwrap
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont


BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_DIRECTORY = "quotes"

def fetch_quotes():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select(".quote")[:5]

    quote_data = []
    for q in quotes:
        text = q.select_one(".text").text.strip()
        author = q.select_one(".author").text.strip()

        tags = [tag.text.strip() for tag in q.select(".tag")]

        quote_data.append({
            "text": text,
            "author": author,
            "tags": tags
        })


    return quote_data

def create_image(text, author, index):
    width, height = 800, 400
    background_color = "#fdf6e3"
    text_color = "#626060"

    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()

    wrapped = textwrap.fill(text, width=60)
    author_text = f"- {author}"

    y_text = 60
    draw.text((40, y_text), wrapped, font=font, fill=text_color)

    y_text += wrapped.count('\n') * 15 + 40

    draw.text((500, y_text), author_text, font=font, fill=text_color )
    

    # save image
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)

    filename = os.path.join(OUTPUT_DIRECTORY, f"quote_{index+1}.png")

    image.save(filename)
    print("Picture created and saved!")

def main():
    quotes = fetch_quotes()
    for index, quote in enumerate(quotes):
        create_image(
            quote["text"],
            quote["author"],
            index
        )

if __name__ == "__main__":
    main()



