import pandas as pd

students = pd.DataFrame({
    "Student_id":[1,2,3,4,5],
    "Student":["Sahal","Enderman","Farhu","pps","Yash"],
    "City":["Chadotar","Palanpur","Radhanpur","Maheshana","Jitpur"]

})

marks = pd.DataFrame({
    "Student_id":[1,2,3,4,5],
    "Subjects":["Python","Java","Php","DSA","Html"],
    "Marks" : [56,75,44,67,54]
})

inn_join = pd.merge(students, marks, on="Student_id", how="inner")
print("\n inner join : \n ", inn_join)

lef_join = pd.merge(students, marks, on="Student_id", how="left")
print("\n lef join : \n ", lef_join)