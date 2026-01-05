import pandas as pd

data = {
    "Time":[1,2,3,4,5,6],
    "Value":[10,20,None,40,None,60]
}


df = pd.DataFrame(data)

df["Value"] = df["Value"].interpolate(method="linear")
print(df)