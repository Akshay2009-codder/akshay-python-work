import pandas as pd

data = {
    "Student" : ["Mahesh","Ratan","Dashu","Samrat","Kiran","Fenil"],
    "Subject" : ["Python","Java","Dsa","C","Html","Php"],
    "Marks" : [98,67,45,98,97,56],
    "City" : ["Mahesana","Mahesana","Mahesana","Tharad","Tharad","Tharad"]
}

df = pd.DataFrame(data)

city_state = df.groupby("City")["Marks"].agg(
    avg_marks = "mean",
    student_count = "count",
).reset_index()

print(city_state)

subject_max = df.groupby("Subject")["Marks"].max().reset_index()
print("\nMaximum marks per subject:")
print(subject_max)