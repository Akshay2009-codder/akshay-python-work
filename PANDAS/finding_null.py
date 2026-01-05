import pandas as pd

data = {
    "student":["Akshay","Sahal","Yash"],
    "subject":["Python","Java","C++"],
    "score":[90,95,80],
    "city":["Tharad","Chadotar", None]
}

info = pd.DataFrame(data)
print(info)

print(info.head())
print(info.info())
print(info.isnull().any(axis=1))