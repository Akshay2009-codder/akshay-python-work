# write a progaram wich will keep adding a stream of number inputed by the user. the adding stop as soon usser prees q keybord

sum = 0
while(True):
    userinput = input("Enter a price : ")
    if (userinput != 'q'):
        sum = sum + int(userinput)
        print(F"order total so far {sum}")
        print("enter q to quit")

    else:
        print(f"your total bill is : {sum}")
        print("Thank you for use my calculator")
        break
