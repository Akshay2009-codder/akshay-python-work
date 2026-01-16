fruits = ["apple","banana","chiku","paineple","mango","bit","jabun","mausambi","jam"]


while True:
    user_input = str(input("What you want to serch in fruits ( if finish write exit) : "))
    if user_input.lower() == "exit".lower():
        break

    suggetion = []
    for fruit in fruits:
        if user_input in fruit:
            suggetion.append(fruit)

    if suggetion:
       print("suggetion")
       for s in suggetion:
           print()
           print("-",s)

    else:
        print("No suggestion found")
print("\nThanks for visiting")



