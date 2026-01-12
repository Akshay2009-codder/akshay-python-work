import pandas as pd


data = {
    "Student":["Sahal","Enderman","Farhu","pps","Yash"],
    "Subject": ["Python","java","C++","PHP","HTML"],
    "Marks":[97,67,None,76,98],
    "City":["Chadotar","Palanpur",None,"Palanpur","Jitpur"]
}

df = pd.DataFrame(data)

print("Original data : \n ", df)


encoding = pd.get_dummies(df, columns=["Subject","City"])
print("Encoding data : \n ", encoding)
