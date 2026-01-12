import pandas as pd

data = pd.DataFrame({
    "Student" : ["Ramesh","Tom","Hexon"],
    "City": ["New York","Ahemdabad","Tong"]
})

print("\n\nThe data : \n\n", data)

index = data.set_index("Student")
print("\n\nAfter setting the student as index : \n\n", index)

st = data.loc[2]
print("\n\nAcessed student : \n\n", st)

data.reset_index()
print("\n\nAfter reseting index : \n\n", data)

data.reset_index(drop=True)
print("\n\nAfter using drop = true : \n\n", data)