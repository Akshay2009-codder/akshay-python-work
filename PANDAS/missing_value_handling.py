import pandas as pd

data = {
    "Name":["Akshay","Sahal",None],
    "Age":[21,22,None],
    "Salary":[22000,45000,None],
    "Performance Score" : [95,98,None]
}

df = pd.DataFrame(data)


df.dropna(axis = 0, inplace = True)
print(df)