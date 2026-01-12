import pandas as pd

data = {
    "Student":["Sahal","Enderman","Farhu","Pps","Yash"],
    "Subject": ["Python","Java","C++","PHP","Foml"],
    "Marks":[97,67,89,76,98],
    "City":["Chadotar","Palanpur","Radhanpur","Palanpur","Jitpur"]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

print(df["Student"])

print(df["Marks"])

df.info()
df.describe()