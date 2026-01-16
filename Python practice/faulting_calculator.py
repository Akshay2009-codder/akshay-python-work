wrong_ans = {
    (45, "*", 3): 555,
    (56, "+", 9): 77,
    (56, "/", 6): 4,
}

while True:
    print("\n--- Welcome to the Faulty Calculator ---")
    print("Enter 'q' to quit.")
    num_1 = (input("Enter a number: "))
    if num_1 == "q":
        break
    operator_a = input("Enter an operator from (+,-,*,/) : ")
    if operator_a == "q":
        break
    num_2 = (input("Enter another number: "))
    if num_2 == "q":
        break

    try:
        num_1 = int(num_1)
        num_2 = int(num_2)

        if (num_1, operator_a, num_2) in wrong_ans:
            print(f"your ans is : {wrong_ans[(num_1, operator_a, num_2)]}")

        else:
            if operator_a == "+":
                print(f"your ans is : {num_1 + num_2}")
            elif operator_a == "-":
                print(f"your ans is : {num_1 - num_2}")
            elif operator_a == "*":
                print(f"your ans is : {num_1 * num_2}")
            elif operator_a == "/":
                print(f"your ans is : {num_1 / num_2}")
            else:
                print("Please enter a valid operator")
    except:
        print("Please enter a valid number")

print("\nThank you for using my calculator")