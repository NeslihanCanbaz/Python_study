from book import Book
from user import User
import json
import os

class Library():
    def __init__(self,name):
        self.name = name
        self.books = []
        self.users = []

    def add_book(self,book):
        for b in self.books:
            if b.title == book.title:
                print(f"The book '{book.title}' already exixsts!")
                return
        self.books.append(book)
        print(f"The book '{book.title}' added to the library")      

    def add_user(self,user):
        for u in self.users:
            if u.name == user.name:
                print("User already exists!")
                return
        self.users.append(user)
        print(f"User '{user.name}' added to the library!")    

    def show_all_books(self):
        for book in self.books:
            print("-" * 40)
            print("Title:",book.title)
            print("Author:",book.author)
            print("Available:", not book.is_borrowed)
            print("Borrowed by:",book.borrowed_by)
            print("-" * 40)

    def login(self,name,password):
        for user in self.users:
            if user.name == name and user.password == password:
                return user
            
        print("user not found or password incorrect")
        return None
    
    def borrow_book(self,user,title):
        title = title.strip()
        for book in self.books:
            if book.title == title:
                user.borrow_book(book)
                return 
        print("Book not found")

    def return_book(self,user,title):
        title = title.strip()
        for book in self.books:
            if book.title == title:
                user.return_book(book)
                return
        print("Book not found.")         

    def save(self,file):     #save to json
        book_list =[book.to_dict() for book in self.books]
        user_list =[user.to_dict() for user in self.users]
        data ={
            "books":book_list,
            "users": user_list
        }
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False, indent=4)

    def load(self,file):      #load from json
        if not os.path.exists(file):
            return
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.books = []
        for book_data in data["books"]:
            book = Book(**book_data)
            self.books.append(book)

        self.users = []
        for user_data in data["users"]:
             # Önce borrowed_books başlıklarını boş liste yap
            borrowed_books_titles = user_data.pop("borrowed_books")
            user = User(**user_data, borrowed_books=[])  # boş liste ile yarat
            self.users.append(user)

    # Sonra borrowed_books listesini gerçek Book objeleri ile doldur
            for title in borrowed_books_titles:
                book = next((b for b in self.books if b.title == title), None)
                if book:
                    user.borrowed_books.append(book)
                    book.is_borrowed = True
                    book.borrowed_by = user.name