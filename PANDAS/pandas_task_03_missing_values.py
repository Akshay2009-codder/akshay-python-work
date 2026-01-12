import pandas as pd

data = {
    "Student":["Sahal","Enderman","Farhu","pps","Yash"],
    "Subject": ["Python","java","C++","PHP","HTML"],
    "Marks":[97,67,None,76,98],
    "City":["Chadotar","Palanpur",None,"Palanpur","Jitpur"]
}

df = pd.DataFrame(data)

print("Missing value : ", df.isnull().sum())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["City"] = df["City"].fillna("unknown")


print("Filled data : ", df)


