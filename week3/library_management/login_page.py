from library import Library

while True:

    print("-" * 60)
    print()
    print(" 1- LOGIN             ")
    print(" 2- CREATE ACOUNT     ")
    print(" 3- EXIT.             ")
    print()
    print("-" * 60)

    choice = input("Enter your choice please: ")
    while True:

        if choice =="1":
            name = input("Enter a name: ")
            password = input("Enter a password: ")
            Library.login(name,password)

            print("-" * 60)
            print()
            print(" 1- LIST ALL BOOKS ")
            print(" 2- BORROW A BOOK  ")
            print(" 3- RETURN A BOOK  ")
            print(" 4- SHOW MY BORROWED BOOKS")
            print(" 5- SAVE AND EXIT")
            print()
            print("-" * 60)
            break

    if choice == 2:
        Library.add_user(user)

    if choice == 3:
        break






    
