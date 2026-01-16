class Library:
    def __init__(self, books):
        self.books = books

    def display_menu(self):
        print("\n======= LIBRARY MENU ======")
        print("1. Display books")
        print("2. Borrow a book")
        print("3. Add a book")
        print("4. Exit")
        print("===========================\n")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available in the library.")
        else:
            print("Available books:")
            for book in self.books:
                print(f"- {book}")

    def borrow_book(self):
        book_name = input("Enter the name of the book to borrow: ").strip()
        if book_name in self.books:
            self.books.remove(book_name)
            print(f" You have borrowed '{book_name}'.")
        else:
            print(" Book not available.")

    def add_book(self):
        book_name = input("Enter the name of the book to add: ").strip()
        self.books.append(book_name)
        print(f" Book '{book_name}' added successfully.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.display_books()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.add_book()
            elif choice == '4':
                print(" Thank you for using the library system. Goodbye!")
                break
            else:
                print(" Invalid choice. Please try again.")



books = ["Cripto", "Python", "Operating System", "Math"]
library = Library(books)
library.run()
