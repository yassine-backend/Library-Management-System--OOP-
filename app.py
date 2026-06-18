
import os
import sys


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if not self.available:
            print("Book is not available.")
            return

        self.available = False
        print(f"You borrowed '{self.title}'.")

    def return_book(self):
        if self.available:
            print("This book is already in the library.")
            return

        self.available = True
        print(f"You returned '{self.title}'.")

    def show_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Available: {self.available}")
        print("-" * 25)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        if not self.books:
            print("No books found.")
            return

        for book in self.books:
            book.show_info()

    def find_book(self, title):
        for book in self.books:
            if book.title.upper() == title.upper():
                return book
        return None


library = Library()

library.add_book(Book("Python", "John Smith"))
library.add_book(Book("How To Be Smart", "Robert Martin"))


while True:
    cls()

    print("=== Library Management System ===")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Quit")

    try:
        choice = int(input("\nChoice: "))

        if choice == 1:
            cls()

            title = input("Book Title: ").strip()
            author = input("Author: ").strip()

            if not title or not author:
                print("Invalid input.")
                input("\nPress Enter...")
                continue

            library.add_book(Book(title, author))

            print("Book added successfully.")
            input("\nPress Enter...")

        elif choice == 2:
            cls()

            print("=== Book List ===\n")
            library.show_books()

            input("\nPress Enter...")

        elif choice == 3:
            cls()

            title = input("Book Title: ")

            book = library.find_book(title)

            if book:
                book.borrow()
            else:
                print("Book not found.")

            input("\nPress Enter...")

        elif choice == 4:
            cls()

            title = input("Book Title: ")

            book = library.find_book(title)

            if book:
                book.return_book()
            else:
                print("Book not found.")

            input("\nPress Enter...")

        elif choice == 5:
            cls()
            print("Goodbye.")
            sys.exit()

        else:
            print("Invalid choice.")
            input("\nPress Enter...")

    except ValueError:
        print("Please enter a number.")
        input("\nPress Enter...")