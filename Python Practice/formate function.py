users = ['Akshay', 'Alka','maulik','Sahal']

computers = ['Linux','Windows','iphone','mac']

for i in range (0, len(users)):
    print(f"{users[i]} is use {computers[i]} company's computer")


print("=" * 44)


# using formate function

for i in range (0, len(users)):
    template = ("{} is use {} comapany's computer".format(users[i], computers[i]))
    print(template.format(users[i], computers[i]))