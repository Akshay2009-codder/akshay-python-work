import pandas as pd
import numpy as np

# ================= RAW DATA =================
data = {
    "Student_ID": [101, 102, 103, 104, 105, 101, 106, 107, 108, 109, 110, 111],
    "Student_Name": ["Aman", "Riya", "Kunal", "Meena", "Arjun", "Aman", "Sonal", "Ravi", "Neha", "Pooja", "Dev", "Isha"],
    "Maths": [78, 105, 67, -5, None, 78, 88, 92, 45, None, 39, 100],
    "Science": [82, 90, None, 55, 110, 82, -10, 85, 60, 73, None, 95],
    "English": [75, 88, 92, None, 66, 75, 80, -20, 58, 77, 44, 102],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Delhi", "Pune", "Delhi", "Mumbai", "Pune", "Delhi", "Mumbai"],
    "Join_Date": ["2023-06-12", "2023-07-01", "2023-06-20", "2023-07-05", "2023-06-18",
                  "2023-06-12", "2023-07-10", "2023-06-25", "2023-07-02", "2023-06-30",
                  "2023-07-08", "2023-06-15"]
}

df = pd.DataFrame(data)

# ================= INVALID VALUE HANDLING =================
subjects = ["Maths", "Science", "English"]

for col in subjects:
    df[col] = df[col].where(df[col].between(0, 100), np.nan)

# ================= DUPLICATE HANDLING =================
df = df.sort_values(by=subjects, ascending=False)
df = df.drop_duplicates(subset="Student_ID", keep="first")

# ================= FILL MISSING VALUES =================
for col in subjects:
    df[col] = df[col].fillna(df[col].mean())

# ================= NUMPY VALIDATION =================
marks_array = df[subjects].to_numpy()

subject_means = np.nanmean(marks_array, axis=0)
subject_stds = np.nanstd(marks_array, axis=0)

# ================= DATETIME HANDLING =================
df["Join_Date"] = pd.to_datetime(df["Join_Date"])
df["Join_Year"] = df["Join_Date"].dt.year
df["Join_Month"] = df["Join_Date"].dt.month

# ================= FEATURE ENGINEERING =================
df["Total_Marks"] = df[subjects].sum(axis=1)
df["Average_Marks"] = df[subjects].mean(axis=1)

df["Result"] = df["Average_Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

# ================= RANKING =================
df["Rank"] = df["Total_Marks"].rank(method="dense", ascending=False)

# ================= AGGREGATION =================
city_avg = df.groupby("City")["Average_Marks"].mean()

# ================= TOP STUDENTS =================
top_students = df.nlargest(3, "Total_Marks")

# ================= FINAL OUTPUT =================
print(df)
print("\nCity-wise Average Marks:\n", city_avg)
print("\nTop 3 Students:\n", top_students)
print("\nSubject Means (NumPy):", subject_means)
print("Subject Std Dev (NumPy):", subject_stds)
print("\nFinal Shape:", df.shape)
print(df.info())
