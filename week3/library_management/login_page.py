from book import Book, Novel, Magazine
from user import User
from library import Library

data_file = "library.json"

library = Library("My Library")

library.load(data_file)

library.add_book(Book("Ada", "Ahmet", 1900, False, None))

current_user = None


while True:

    print("-" * 60)
    print()
    print(" 1- LOGIN             ")
    print(" 2- CREATE ACOUNT     ")
    print(" 3- EXIT.             ")
    print()
    print("-" * 60)

    choice = input("Enter your choice please: ")
    if choice =="1":
        name = input("Enter a name: ")
        password = input("Enter a password: ")
        user = library.login(name,password)

        if user:
            current_user = user
            print(f"\nWelcome back, {current_user.name}!")

            while True:
                print("-" * 60)
                print()
                print(" 1- LIST ALL BOOKS ")
                print(" 2- BORROW A BOOK  ")
                print(" 3- RETURN A BOOK  ")
                print(" 4- SHOW MY BORROWED BOOKS")
                print(" 5- SAVE AND EXIT")
                print()
                print("-" * 60)
                
                option = input("Enter your choice please: ")

                if option == "1":
                    library.show_all_books()

                elif option == "2":  
                    title = input("Enter book title: ")
                    library.borrow_book(current_user, title)  

                elif option == "3":
                    title = input("Enter book title: ")
                    library.return_book(current_user, title)

                elif option == "4":
                    current_user.list_borrowed_books() 

                elif option == "5":
                    current_user = None
                    print("Logged out. Saving data...") 
                    library.save(data_file)  
                    break

                else:
                    print("Invalid option.")    
        
        else:
            print("Login failed.")

    elif choice == "2":
        name =  input("Enter a name: ")
        password = input("Enter a password: ")
        new_user = User(name,password,[])
        library.add_user(new_user)
        print("Account created!")
             
    elif choice == "3":
        library.save(data_file)
        print("Data saved.")
        break

    else:
        print("Invalid choice!")




# def borrow_by_title(user, all_books, title):
#     book_to_borrow = next((b for b in all_books if b.title == title), None)
#     if book_to_borrow:
#         user.borrow_book(book_to_borrow)
#     else:
#         print(f"Book '{title}' not found!")

    
