import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    "Student" : ["Mahesh","Ratan","Dashu","Samrat","Kiran","Fenil"],
    "Subject" : ["Python","Java","Dsa","C","Html","Php"],
    "Marks" : [98,67,None,98,None,56],
    "City" : ["Chuva","Dhanera","Maheshana",None,"Sanval",None]
}

df = pd.DataFrame(data)

# Step 1: Handling missing values
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["City"] = df["City"].fillna("Unknown")

print("After handling missing value:\n", df)

# Step 2: Encoding categorical data
encoding = pd.get_dummies(df, columns=["Subject", "City"])
print("Encoding data:\n", encoding)

# Step 4: Feature & Target Separation
X = encoding.drop("Marks", axis=1)
y = encoding["Marks"]

# Step 5: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 6: Print Shapes
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)
