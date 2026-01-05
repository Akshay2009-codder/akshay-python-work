import pandas as pd

info = {
    "Name":["Akshay","Yash","Rudra","Sahal","Farhan","Anas","Prgyan","Badal"],
    "Age":[18,23,24,24,24,24,24,24],
    "Performance": [78,98,78,90,98,78,98,78]

}

df = pd.DataFrame(info)
print(df)

# filtering one row
print("\n printing about one row ")
print(df[["Performance"]])

# filtering multiple rows

print("\n printing about two rows ")
print(df[["Age","Performance"]])

# applaying one condition
print("\n filtering using one condition ")
condition_1 = df[df["Performance"]>90]
print(condition_1)

# appliying multiple conditions
print("\n filtering using multiple conditions ")
condition_2 = df[(df["Performance"]>90) & (df["Age"] > 20)]
print(condition_2)