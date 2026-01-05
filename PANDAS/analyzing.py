import pandas as pd

data = {
    "student":["Akshay","Sahal","Yash"],
    "subject":["Python","Java","C++"],
    "score":[90,95,80]
}

info = pd.DataFrame(data)
print(info)

# printing first column

print(info.iloc[:,0])

# printing only one column

print(info[["student"]])

# score > condition

condition = info[info["score"]>80]
print(condition)