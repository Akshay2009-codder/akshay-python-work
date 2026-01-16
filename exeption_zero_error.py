while True:
    print("Enter q to exit")
    a = input("Enter a number : ")
    if a == "q":
        break
    b = input("Enter another number : ")
    if b == "q":
        break

    try:
        a = int(a)
        b = int(b)
        print(a / b)
    except ZeroDivisionError:
        print("any digit cannot be divided by zero")
    except ValueError:
        print("Please enter a valid number")
print("Thank you for using this program")