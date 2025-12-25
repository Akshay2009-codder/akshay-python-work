a = input("enter your name : ")
if a.isnumeric():
    raise Exception("number not allowed")

print(f"your name is {a}")