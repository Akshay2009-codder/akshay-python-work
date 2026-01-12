import pandas as pd

data = {
    "Student":["Sahal","Enderman","Farhu","Pps","Yash"],
    "Subject": ["Python","Java","C++","PHP","Foml"],
    "Marks":[97,67,89,76,98],
    "City":["Chadotar","Palanpur","Radhanpur","Palanpur","Jitpur"]
}

df = pd.DataFrame(data)

scored_student = df[df["Marks"]>85]
print("Student gated morethen 95 : \n\n" ,scored_student)

from_palanpur = df[df["City"]=="Palanpur"]
print("Student from palanpur :\n\n ", from_palanpur)

student_between_value = df[df["Marks"].between(70,90)]
print("Student between value : \n\n", student_between_value)
