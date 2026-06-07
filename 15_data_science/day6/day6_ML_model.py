import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

data = pd.read_csv("youtube_comments.csv")

X_train, X_test, Y_train, Y_test = train_test_split(
    data["comment"], data["label"], test_size=1, random_state=30
)

model = Pipeline([("tfidf", TfidfVectorizer()), ("clf", LogisticRegression())])

model.fit(X_train, Y_train)
acc = model.score(X_test, Y_test)
print(f"Model trained. Accuracy {acc * 100:.2f}%")
