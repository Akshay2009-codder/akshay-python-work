import pandas as pd

data = {
    "Name": ["Raman","Kaman","Dhavan"],
    "Age": [12,17,34],
    "Salary": [8000,9000,6000]
}

df = pd.DataFrame(data)

df.sort_values(by=["Age","Salary"], ascending=[False,False], inplace=True)
print(df)
