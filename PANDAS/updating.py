import pandas as pd

data = {
    "Name":["Akshay","Sahal","Anas"],
    "Age":[21,22,23],
    "Salary":[22000,45000,65000],
    "Performance Score" : [95,98,79]
}

df = pd.DataFrame(data)
print("\nDatabase :\n " ,df)

df.loc[1,"Performance Score"] = [99]
print("\nAfter updating : \n" ,df)


df["Salary"] = df["Salary"]*1.05
print("\nAfter incrasing salary  :\n " ,df)