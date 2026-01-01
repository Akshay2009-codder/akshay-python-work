import pandas as pd

data = {
    "Name":["Sahal","Yash","Farhan"],
    "Age":[18,17,17],
    "city":["chadotar",'ratanpur','radhanpur']
}

df = pd.DataFrame(data)
print(df)

#df.to_csv('Info.csv',index=False)

#df.to_csv('Info.json',index=False)

df.to_csv('Info.exel',index=False)