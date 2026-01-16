import pandas as pd
import numpy as np

data = {
    "Student_ID": [101, 102, 103, 104, 105, 101, 106, 107, 108, 109, 110, 111],
    "Student_Name": ["Aman", "Riya", "Kunal", "Meena", "Arjun", "Aman", "Sonal", "Ravi", "Neha", "Pooja", "Dev", "Isha"],
    "Maths": [78, 105, 67, -5, None, 78, 88, 92, 45, None, 39, 100],
    "Science": [82, 90, None, 55, 110, 82, -10, 85, 60, 73, None, 95],
    "English": [75, 88, 92, None, 66, 75, 80, -20, 58, 77, 44, 102],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Delhi", "Pune", "Delhi", "Mumbai", "Pune", "Delhi", "Mumbai"],
    "Join_Date": ["2023-06-12", "2023-07-01", "2023-06-20", "2023-07-05", "2023-06-18",
                  "2023-06-12", "2023-07-10", "2023-06-25", "2023-07-02", "2023-06-30",
                  "2023-07-08", "2023-06-15"]
}

df = pd.DataFrame(data)

# information about data

print(df.info())

# filling null value

df["Maths"] = df["Maths"].fillna(df["Maths"].mean())
df["Science"] = df["Science"].fillna(df["Science"].mean())
df["English"] = df["English"].fillna(df["English"].mean())

# fixing invalid value

df["Maths"] = df["Maths"].clip(lower=0, upper=100)
df["Science"] = df["Science"].clip(lower=0, upper=100)
df["English"] = df["English"].clip(lower=0, upper=100)

# deleting duplicates

data.drop_duplicates(inplace=True)

# total marks

df["Total_Marks"] = df["Maths","Science","English"].sum(axis=1)

# Average marks

df["Average_Marks"] = df["Maths","Science","English"].mean(axis=1)

#result

df["Result"] = df["Maths","Science","English"].apply(
    lambda row : "pass" if all(marks>=35 for marks in row) else "fail",
    axis = 1
)

