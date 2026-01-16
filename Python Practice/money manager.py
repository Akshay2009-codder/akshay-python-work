def gatedata():
    import datetime
    return datetime.datetime.now()

print("\n===WELCOME TO MONEY MANAGER===\n")
print("When your shopping is completed, enter 'q' to quit.\n")

while True:
    why = input("why spend money? : ")
    if why.lower() == "q":
        print("Thank you for your time")
        break

    money = input("how much money you spend? : ")
    if money.lower() == "q":
        print("Thank you for your time")
        break

    if not money.isdigit():
        print("Invalid input! Please enter numbers only for money.\n")
        continue


    with open("info.txt", "a") as f:
        f.write(f"{gatedata()} : {why} -- {money}\n")

print("\n================================")
