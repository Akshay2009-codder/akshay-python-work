import pandas as pd

students = pd.DataFrame({
    "Student_id": [1, 2, 3, 4, 5, 1, 3],
    "Student": ["Sahal", "Enderman", "Farhu", "pps", "Yash", "Sahal", "Farhu"],
    "City": ["Chadotar", "Palanpur", "Radhanpur", "Maheshana", "Jitpur", "Chadotar", "Radhanpur"],
    "Marks": [85, 90, 78, 88, 92, 85, 78]
})

# detecting duplicate values

duplicate = students[students.duplicated()]
print("\n only Duplicates values : \n " , duplicate)

# Removing duplicates

new_data = students.drop_duplicates()
print("\n data after removing duplicates : \n " , new_data)

# showing unique citys

uniqe_city  = students["City"].nunique()
print("Unique cities : \n " , uniqe_city)

#count of unique cities

count_u_city = students["City"].unique()
print("Count of unique cities : \n " , count_u_city)

# Value count of cities

v_count_city = students["City"].value_counts()
print("Value count of cities  : \n " , v_count_city)