

class Book():
    def __init__(self,title,author,publication_year,is_borrowed,borrowed_by):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_borrowed = is_borrowed
        self.borrowed_by = borrowed_by

    def show_info(self):
       print("Title: ",self.title)
       print("Author: ",self.author)
       print("Publication_year: ",self.publication_year)
       print("Is borrowed: ",self.is_borrowed)
       print("Borrowed by: ",self.borrowed_by)
         
    def borrow(self,user):
        if self.is_borrowed==True:
            print("The book was already borrowed by: ",self.borrowed_by)
        else:
            print("The book is available.")
            self.is_borrowed = True        # kitabı ödünç aldık
            self.borrowed_by = user         # kullanıcıyı atadık
            print(f"{self.title} has been borrowed by {user}.")   

    def return_book(self,):
        if self.is_borrowed == False:
            print("The book is not borrowed")
        else:
            user = self.borrowed_by
            self.is_borrowed = False
            self.borrowed_by = None
            print(f"The book returned by: {user}")

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "publication_year": self.publication_year,
            "is_borrowed": self.is_borrowed,
            "borrowed_by": self.borrowed_by
    }


class Novel(Book):
    def __init__(self,title,author,publication_year,is_borrowed,borrowed_by,genre):
        Book.__init__(self,title,author,publication_year,is_borrowed,borrowed_by) 
        self.genre = genre  

class Magazine(Book):
    def __init__(self,title,author,publication_year,is_borrowed,borrowed_by, issue):
        Book.__init__(self,title,author,publication_year,is_borrowed,borrowed_by)
        self.issue = issue

