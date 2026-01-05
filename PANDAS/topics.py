import pandas as pd

# info = {
#     "Name":["Akshay","Yash","Rudra","Sahal","Farhan","Anas","Prgyan","Badal"],
#     "Age":[18,23,24,24,24,24,24,24],
#     "Performance": [78,98,78,90,98,78,98,78]
#
# }
#
# df = pd.DataFrame(info)
# print(df)

df = pd.read_csv("employees.csv")
print(df)

print(df.describe())

print(df.shape)
print(df.columns)