library = {
    "Python101": "Available",
    "DataScience": "Available",
    "Algorithms": "Available"
}

menu= ['--------------------------------------',
       '|   Kutuphane Menusune Hosgeldiniz!   |',
       '|   1-Add Book                        |',
       '|   2-Borrow Book                     |',
       '|   3-Return Book                     |',
       '|   4-View All Books                  |',
       '|   5- Exit.                          |',
       '-------------------------------------- ']

for i in menu:
    print ('\t'.expandtabs(30), i)


secim = input("Lutfen menuden bir secim yapiniz: ")


if secim == '1':
    yeni_kitap=input("Eklenecek kitabi girniz: ")
    library[yeni_kitap]= "Avaliable"
 

if secim == '2':
    borrow_book = input("Sececeginiz kitabi giriniz: ")
    library[borrow_book]= "Borrowed"


if secim == '3':
    return_book = input("Iade edeceginiz kitabi giriniz: ")
    library[return_book]= "Avaliable"


if secim == '4':
    for key, value in library.items():
        print(key, ":", value)
 #   print("Tum kitaplar: ", library.keys())
       

if secim == '5':
    quit()



print(library) 





