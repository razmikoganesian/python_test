import pandas as pd
import numpy as np
import random

toxic_comments = ["It is boriing", "SO bad", "Can't wathc it"]
supportive_comments = ["So good", "I am insprired", "Amazing"]

data = []

for i in range(3):
    data.append({"comment": random.choice(toxic_comments), "label": "toxic"})
    data.append({"comment": random.choice(supportive_comments), "label": "positive"})

data_frame = pd.DataFrame(data)
data_frame.to_csv("youtube_comments.csv", index=False)
print("Data saved✅")
