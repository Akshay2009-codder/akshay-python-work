class Bank:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Insufficient balance")
        else:
            print("Invalid amount")

    def display_menu(self):
        print("\n=== WELCOME TO BANK ===")
        print("1. Check Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Exit")
        print("========================\n")

    def check_balance(self):
        print("Current Balance:", self.balance)


def main():
    bank1 = Bank()

    while True:
        bank1.display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            bank1.check_balance()

        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))
            bank1.deposit(amount)

        elif choice == "3":
            amount = int(input("Enter amount to withdraw: "))
            bank1.withdraw(amount)

        elif choice == "4":
            print("Thanks for using our banking system.")
            break

        else:
            print("Invalid choice. Please try again.")

main()
