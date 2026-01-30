from book import Book
import json



class User():
    def __init__(self,name,password,borrowed_books):
        self.name = name
        self.password = password
        self.borrowed_books = borrowed_books

    def borrow_book(self,book):
        if book.is_borrowed == True:
            print("The book was already borrowed.")
        else:
            book.borrow(self.name)
            self.borrowed_books.append(book)

    def return_book(self,book):
        if book not in self.borrowed_books:
            print("You did not borrow this book.")
        else:
            book.return_book()
            self.borrowed_books.remove(book)
            

    def list_borrowed_books(self):
        if not self.borrowed_books:
            print("You have no borrowed books.")
        else:
            for book in self.borrowed_books:
                print("title:", book.title, "|Author:" ,book.author )


    def to_dict(self):
        return {
        "name": self.name,
        "password": self.password,
        "borrowed_books": [book.title for book in self.borrowed_books]
    }
    

# # Test için kullanıcı
# test_user = User("Ayşe", "123",[])

# # Örnek kitaplar
# all_books = [
#     Book("Ada", "Ahmet", 1900, False, None),
#     Book("Deniz", "Mehmet", 1920, False, None)
# ]

# # Ödünç alma testi
# #borrow_by_title(test_user, all_books, "Ada")  # Tek satırla ödünç al

# # Kullanıcının ödünç aldığı kitapları listele
# #test_user.list_borrowed_books()
