from book import Book
from user import User
import json
import os

class Library():
    def __init__(self,name,books,users):
        self.name = name
        self.books = books
        self.users = users

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
            print("Title:",book.title)
            print("Author:",book.author)
            print("Available:",book.is_borrowed)
            print("Borrowed by:",book.borrowed_by)

    def login(self,name,password):
        for user in self.users:
            if user.name == name and user.password == password:
                return user
            
        print("user not found or password incorrect")
        return None

    def save(sel,file):     #save to json
        book_list =[book.to_dict() for book in self.books]
        user_list =[user.to_dict() for user in self.users]
        data ={
            "books":book_list,
            "users": user_list
        }
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False, indent=4)

    def load(self,file):      #load from json
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