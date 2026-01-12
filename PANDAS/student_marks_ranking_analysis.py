import pandas as pd

data = {
    "Student" : ["Mahesh","Ratan","Dashu","Samrat","Kiran","Fenil"],
    "Subject" : ["Python","Java","Dsa","C","Html","Php"],
    "Marks" : [98,67,76,98,45,67],
    "City" : ["Chuva","Dhanera","Maheshana","Tharad","Sanval","Rampura"]
}

df = pd.DataFrame(data)

# sorting by marks

sorted_data = df.sort_values(by=["Marks"],ascending=False)
print("Sorted data : \n\n", sorted_data)

# getting top 3 student

print("Top 3 student : \n\n", df.nlargest(3, ["Marks"]))
