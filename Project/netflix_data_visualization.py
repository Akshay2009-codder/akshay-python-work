import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix.csv")

df = df.drop_duplicates()

df["Country"] = df["Country"].fillna("Unknown")
df["Rating"] = df["Rating"].fillna("Not Rated")
df["Genre"] = df["Genre"].fillna("Unknown")
df["Director"] = df["Director"].fillna("Not Given")
df["Cast"] = df["Cast"].fillna("Not Given")

df["Date_Added"] = pd.to_datetime(df["Date_Added"], errors="coerce")

df["Duration"] = df["Duration"].astype(str)
df["Duration_Min"] = df["Duration"].str.extract(r"(\d+)").astype(float)

type_count = df["Type"].value_counts()
rating_count = df["Rating"].value_counts().head(8)
country_count = df["Country"].value_counts().head(6)
genre_count = df["Genre"].value_counts().head(6)
year_count = df["Release_Year"].value_counts().sort_index()

plt.figure()
plt.pie(type_count, labels=type_count.index, autopct="%1.1f%%")
plt.title("Content Type Distribution")
plt.show()

plt.figure()
plt.bar(rating_count.index, rating_count.values)
plt.title("Top Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

plt.figure()
plt.bar(country_count.index, country_count.values)
plt.title("Top Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()

plt.figure()
plt.bar(genre_count.index, genre_count.values)
plt.title("Top Genres")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

plt.figure()
plt.hist(df["Release_Year"], bins=15)
plt.title("Release Year Distribution")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

plt.figure()
plt.hist(df[df["Type"] == "Movie"]["Duration_Min"], bins=15)
plt.title("Movie Duration Distribution")
plt.xlabel("Minutes")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
type_count.plot(kind="bar")
plt.title("Type Comparison")

plt.subplot(2, 2, 2)
rating_count.plot(kind="bar")
plt.title("Rating Comparison")

plt.subplot(2, 2, 3)
country_count.plot(kind="bar")
plt.title("Country Comparison")

plt.subplot(2, 2, 4)
year_count.plot()
plt.title("Content Over Years")

plt.tight_layout()
plt.show()
