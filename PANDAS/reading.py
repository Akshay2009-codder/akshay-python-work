import pandas as pd

data = pd.read_csv("employees.csv").head(10)

print("first 10 rows")
print(data.head(10))

print("Last 10 rows")
print(data.tail(10))
