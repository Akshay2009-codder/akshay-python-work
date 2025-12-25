import random

a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))

number = random.randint(a, b)

while True:
    friend = int(input(f"Guess a number between {a} and {b}: "))
    if friend > number:
        print("Too high! Try again.")
    elif friend < number:
        print("Too low! Try again.")
    else:
        print("🎉 Congratulations! You guessed it right.")
        break

print("Thanks for playing!")
