import pandas as pd
import random

positive = [
    "I love this product",
    "Amazing experience",
    "Best purchase ever",
    "Very happy with this",
    "Absolutely fantastic",
    "Highly recommended",
    "Works perfectly",
    "Superb quality",
    "Exceeded expectations",
    "Really good service"
]

negative = [
    "Worst product ever",
    "I hate this",
    "Very bad experience",
    "Not worth the money",
    "Terrible quality",
    "Completely disappointed",
    "Waste of time",
    "Very poor service",
    "Do not buy this",
    "Awful experience"
]

neutral = [
    "It is okay",
    "Average experience",
    "Nothing special",
    "It works fine",
    "Could be better",
    "Not bad, not great",
    "Just normal",
    "Okay product",
    "Fair enough",
    "Decent but not amazing"
]

data = []

for _ in range(400):
    data.append([random.choice(positive), "positive"])
    data.append([random.choice(negative), "negative"])
    data.append([random.choice(neutral), "neutral"])

df = pd.DataFrame(data, columns=["review", "sentiment"])
df.to_csv("data/reviews.csv", index=False)

print("Dataset created successfully")
