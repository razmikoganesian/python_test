from flask.testing import FlaskClient
import pandas as pd

data = [
    {
        "title": "Harry Potter",
        "author": "J.Rowling",
        "genre": "fantasy",
        "desription": "Magik world",
    },
    {
        "title": "Show Dog",
        "author": "Phil Knight",
        "genre": "biography",
        "desription": "Nike company history",
    },
    {
        "title": "Graf Monte Kristo",
        "author": "Alexzandr Duma",
        "genre": "prison escape",
        "desription": "History of person",
    },
    {
        "title": "My life <y achievemnets",
        "author": "Henry Ford",
        "genre": "biography",
        "desription": "Ford company history",
    },
]

df = pd.DataFrame(data)
df.to_csv("books.csv", index=False)
print("✅ Book Data set created!")
