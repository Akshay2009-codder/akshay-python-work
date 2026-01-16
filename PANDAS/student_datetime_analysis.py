import pandas as pd

students = pd.DataFrame({
    "Student": ["Sahal", "Enderman", "Farhu", "pps", "Yash"],
    "Join_Date": ["2023-06-12", "2023-06-15", "2023-07-01", "2023-07-05", "2023-07-10"],
    "Marks": [85, 90, 78, 88, 92]
})

# converting joindate in to datetime

students["Join_Date"] = pd.to_datetime(students["Join_Date"])
print(students)

# extrecking year

year = students["Join_Date"].dt.year
print("Extracking year : " ,year)

# extracdking month

month = students["Join_Date"].dt.month
print("Extracking month : " ,month)

# extracking day name

day_name = students["Join_Date"].dt.day_name()
print("Extracking day name : " ,day_name)