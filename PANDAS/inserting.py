import pandas as pd

data = {
    "Name":["Akshay","Sahal","Anas"],
    "Age":[21,22,23],
    "Salary":[22000,45000,65000],
    "Performance Score" : [95,98,79]
}

df = pd.DataFrame(data)

# df["Bonus"] = df["Salary"] * 0.1     # it is used for inserting in last
# print(df)

df.insert(3,"Bonus",df["Salary"]*0.1) # it is used for inserting in specific pocison
print(df)