import pandas as pd

data = {
    "Name": ["Arjun", "Bharat", "Chetan", "Dinesh", "Eshvar"],
    "Age": [18, 22, 18, 20, 22],
    "Salary": [22000,14000,56000,34000,43000],
    "Score": [65, 72, 90, 68, 90]
}

df = pd.DataFrame(data)

grouped_by = df.groupby("Age")["Salary"].sum()
print(grouped_by)