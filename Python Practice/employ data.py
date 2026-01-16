employ = {}

days = int(input("you want how many days report : "))


for i in range(days):
    name = input("Enter employee name : ")
    hour = input("Enter how many hours worked : ")
    employ[name] = hour

print(employ)

max_hours = max(employ)

print("mostly worked employee : ", max_hours)


