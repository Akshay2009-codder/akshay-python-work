def gatedata ():
    import datetime
    return datetime.datetime.now()

name = str(input("Enter your name: "))
work_diat = str(input("what you want enter (workout/diat) : "))

if name == "rohan" and work_diat == "diat":
    f = open ("rohan diat", "w+")
    entering = input("enter what you dait : ")
    f.write(f"{gatedata()} : {entering}")
    f.close()
elif name == "rohan" and work_diat == "workout":
    f = open ("rohan workout", "w+")
    entering2 = input("enter what you worked : ")
    f.write(f"{gatedata()} : {entering2}")
    f.close()

elif name == "sahal" and work_diat == "diat":
    f = open ("sahal diat ", "w+")
    entering3 = input("enter what you dite : ")
    f.write(f"{gatedata()} : {entering3}")
    f.close()

elif name == "sahal" and work_diat == "workout":
    f = open ("sahal workout", "w+")
    entering4 = input("enter what you worked : ")
    f.write(f"{gatedata()} : {entering4}")
    f.close()

else:
    print("invalid input")

show = input("what are you want show (sahal dite, sahal workout, rohan dite, rohan workout)")

if show == "sahal diat":
    f = open ("sahal diat", "r")
    print(f.read())
    f.close()

elif show == "sahal workout":
    f = open ("sahal workout", "r")
    print(f.read())
    f.close()

elif show == "rohan dite":
    f = open ("rohan dite", "r")
    print(f.read())
    f.close()

elif show == "rohan workout":
    f = open ("rohan workout", "r")
    print(f.read())
    f.close()

else:
    print("invalid input")
