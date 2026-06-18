import time
import os
import sys

def cls():
     os.system('cls' if os.name == 'nt' else 'clear')


books = []

class Book():
    def __init__(self , titel ,auther ,avaible):
        self.titel = titel
        self.auther = auther
        self.avaible = avaible

    def show_all_books(self):
        print(f"Name: {self.titel}\nAuther: {self.auther}\nAvaible: {self.avaible}\n======================")

    def borrow(self):
        if self.avaible == False:
             print("The Book  Avaible")
             return
        self.avaible = False
        print(f"You Borrow The Book {self.titel}")


    def return_book(self):
         if self.avaible == True:
              print("You Cant Return Book That You Didnt Take It")
              return
         self.avaible = True
         print(f"You Return The Book {self.titel}")

    def __str__(self):
        return f"{self.titel} by {self.auther} (Available: {self.avaible})"

sod = Book("A", "A", True)
sod2 = Book("B", "B", True)

books.append(sod)
books.append(sod2)
sod.borrow()
for i in books:
        Book.show_all_books(i)

sod.return_book()



while True:
    cls()
    print("=== Library Manager ===")
    print("1. Add Book\n2. Show Info Of Book\n3. Borrow Book\n4. Return Book\n5. Quit")
    Choise = int(input(""))
    if Choise == 1:
          cls()
          print("=== Add Book ===")
          name = str(input("Name Of The Book: "))
          Auth = str(input("Auther Of The Book: ")).upper()
          Titel = Book(name,Auth,True)
          books.append(Titel)
    elif Choise == 2:
         print("=== List Of Books ===")
         for i in books:
            Book.show_all_books(i)
         input("Press Enter Back To Menu")
    elif Choise == 3:
        cls()
        print("=== Borrow Book ===")
        Titel = str(input("Name Of The Book: ")).upper()
        found = False
        for i in books:
            if i.titel.upper() == Titel:
                i.borrow()
                found = True
                break
        if not found:
            print("Book not found.")
        input("Press Enter to continue...")
    elif Choise == 4:
        cls()
        print("=== Return Book ===")
        name = input("Name Of Book").upper()
        founded = False
        for i in books:
            if i.titel == name:
                 founded = True
                 i.return_book()
        if not founded:
                print("Book not found.")
        input("Press Enter to continue...")


    elif Choise == 5:
         cls()
         print("See You Soon")
         sys.exit()
         
