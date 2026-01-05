import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [18, 22, 25, 20, 30],
    "Performance": ["Good", "Average", "Excellent", "Good", "Poor"],
    "Score": [65, 72, 90, 68, 90]
}

df = pd.DataFrame(data)

printing_cn1 = df.loc[df["Score"]>70,["Name","Age"]]
print("\nprinting name and age using condition")
print(printing_cn1)


print("printing using iloc")
printing_cn2 = df.iloc[0:3,0:2]
print(printing_cn2)

updating = df.loc[df["Score"]>=85,"Performance"] = "Excellent"
print(f"after updating {df}")


change_score = df.iloc[0:2,df.columns.get_loc("Score")] = 75
print(f"after changing score {df}")

print("printing good performance student \n" ,df.loc[df["Performance"] == "Good", ["Age", "Score"]])

