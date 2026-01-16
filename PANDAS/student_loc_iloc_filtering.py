import pandas as pd

data = {
    "Student":["Sahal","Enderman","Farhu","pps","Yash"],
    "Subject": ["Python","java","C++","PHP","HTML"],
    "Marks":[97,67,None,76,98],
    "City":["Chadotar","Palanpur",None,"Palanpur","Jitpur"]
}

df = pd.DataFrame(data)

# Printing firast row using iloc

print("\nfirst row : \n " , df.iloc[0])

# printing first two rows

print("\nfirst two row : \n " , df.iloc[0:2])

# printing student thems marks are more than 80

print("\nMArks more than 80 : \n " ,df.loc[df["Marks"] > 80,["Student","Marks"]])

# seting student as an index

data_st = df.set_index("Student", drop=True)
print("Setting student as index : \n " , data_st)

# accesing one student after setting student as index

print("\nAcessing one student : \n",data_st.loc["Sahal"])