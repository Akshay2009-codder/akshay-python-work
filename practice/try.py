
while True:
    print("Press q to quit")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:
        a = int(a)
        if a > 10:
            print("a > 10")
    except Exception as e:
        print(f"are bhai number input karo {e}")
print("Thank you")
