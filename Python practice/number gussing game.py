import random

print("🎮 Welcome to my number guessing game")
print("=====================================")

while True:  # Loop for play again
    pc = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            num = int(input("\nGuess a number from 1 to 100: "))
            attempts += 1

            if num == pc:
                print("🎉 You guessed correctly!")
                break
            elif num > pc:
                print("Too high! Try again.")
            elif num < pc:
                print("Too low! Try again.")
        except:
            print("❌ Please enter a valid number")

    print(f"\n✅ You guessed the number in {attempts} attempts.")
    print("Thank you for playing AK's game!")

    again = input("\nWould you like to play again? (press 'y' for yes) and press any key for brack: ").lower()
    if again != "y":
        print("\n👋 Thanks for playing. Goodbye!")
        break

print("\n===============================")
