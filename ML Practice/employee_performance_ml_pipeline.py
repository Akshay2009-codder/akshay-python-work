import numpy as np
import pandas as pd

data = {
    "Emp_ID": [201, 202, 203, 204, 205, 206, 207, 203, 208, 209, 210, 211, 212],
    "Employee": ["Raj", "Simran", "Amit", "Neha", "Karan", "Pooja", "Vikas",
                 "Amit", "Anjali", "Rohit", "Mehul", "Ira", "Suresh"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance",
                   "IT", "HR", "Finance", "IT", "HR", "Finance"],
    "Experience_Years": [3, 8, -1, 5, None, 2, 12, -1, 6, 15, None, 4, 7],
    "Monthly_Salary": [45000, 60000, 52000, None, 58000, 47000,
                       110000, 52000, -30000, 90000, None, 55000, 75000],
    "Performance_Score": [78, 88, None, 92, 60, 81, 95, None, 45, 85, 70, -10, 100],
    "Join_Date": ["2021-05-10", "2018-03-15", "2020-07-01", "2019-11-20",
                  "2022-01-05", "2021-09-18", "2015-06-30", "2020-07-01",
                  "2019-04-12", "2016-08-25", "2023-02-10", "2020-10-05",
                  "2017-12-01"]
}

df = pd.DataFrame(data)

# make data valid

df["Experience_Years"] = df["Experience_Years"].where(df["Experience_Years"].between(0,60), np.nan)
df["Monthly_Salary"] = df["Monthly_Salary"].where(df["Monthly_Salary"].between(44000,91000), np.nan)
df["Performance_Score"] = df["Performance_Score"].where(df["Performance_Score"].between(0,100), np.nan)

# droping duplicate

df.drop_duplicates(subset=["Emp_ID"], inplace=True)


# filling null values

# print(df.isnull().sum())

df["Experience_Years"] = df["Experience_Years"].fillna(df["Experience_Years"].mean())
df["Monthly_Salary"] = df["Monthly_Salary"].fillna(df["Monthly_Salary"].mean())
df["Performance_Score"] = df["Performance_Score"].fillna(df["Performance_Score"].mean())

# making join Date time

df["Join_Date"] = pd.to_datetime(df["Join_Date"])

# adding a column find joined year

df["Joined_Year"] = df["Join_Date"].dt.year

# adding new column joined date

df["Joining_Month"] = df["Join_Date"].dt.month

# adding new column joining day

df["Joining_day"] = df["Join_Date"].dt.day

# making columnt that show how employee is (Excellent , good , midium )

df["Employee_work"] = df["Performance_Score"].apply(
    lambda score:
    "Excellent" if score >= 80 else
    "Good" if 60 <= score < 80 else
    "Midium" if 40 <= score < 60 else
    "Poor" if 0 <= score < 40 else
    "Unknown"

)

# Giving rank to Employee

df["Rank"] = df["Performance_Score"].rank(ascending=False, method="dense")

# finding  mean of data

mean_performance = np.mean(df["Performance_Score"])
mean_experience = np.mean(df["Experience_Years"])
mean_salary = np.mean(df["Monthly_Salary"])

print("Mean of performance score : ", mean_performance)
print("Mean of experience years : ", mean_experience)
print("Mean of monthly salary : ", mean_salary)

# finding std of data

std_performance = np.std(df["Performance_Score"])
std_experience = np.std(df["Experience_Years"])
std_salary = np.std(df["Monthly_Salary"])

print("Standard deviation of performance score : ", std_performance)
print("Standard deviation of experience years : ", std_experience)
print("Standard deviation of monthly salary : ", std_salary)

# performing numerical operation
df["Salary_per_Experience"] = df["Monthly_Salary"] / df["Experience_Years"]

# Grouping data Department wise


dept_agg = df.groupby("Department").agg(
  Total_Employee = ("Emp_ID", "count"),
  Avg_Experiance = ("Experience_Years", "mean"),
  Avg_Salary = ("Monthly_Salary", "mean"),
  Avg_performance = ("Performance_Score", "mean"),
  Avg_Salary_per_Experience = ("Salary_per_Experience", "mean"),
).reset_index()

print(dept_agg)



