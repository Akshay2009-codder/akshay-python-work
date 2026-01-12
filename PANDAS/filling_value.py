import pandas as pd

data = {
    "Name":["Akshay","Sahal",None],
    "Age":[21,22,None],
    "Salary":[22000,45000,None],
    "Performance Score" : [95,98,None]
}

df = pd.DataFrame(data)

print("Befor filling value")
print(df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print("After filling value")
print(df)