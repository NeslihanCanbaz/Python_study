# metin = input("bri kelime giriniz: ")

# for harf in metin:
#     print(harf)


# i = 0
# while i <len(metin):
        
#     print(metin[i])
#     i+=1
    
     # 1-100 arasinda 3 e ve 4 e tam bolunen sayilar   

# for i in range(100):
#     if i % 3 == 0 and i % 4 == 0:
#         print(i)

#kullanici sayi girsin pozitif mi negatif mi bak

# sayi = int((input("Bir sayi giriniz: ")))

# if sayi < 0 :
#     print(sayi , "negatiftir.")
# elif sayi > 0:
#     print(sayi, "pozitiftir.")
# else:
#     print(sayi , "sifirdir.")            
       
# sayi tahmin oyunu

# sayi = 7
# deneme = 0
# while True:
#     deneme +=1
#     tahmin =int(input("tahminizi giriniz: "))
#     if tahmin < sayi:
#         print("daha buyuk bir sayi giriniz")      
#     elif tahmin > sayi:
#         print("Daha kucuk bir sayi giriniz")          
#     else:   
#         print("Tebrikler dogru bildiniz")       
#         break
# print(deneme, ". denemede bildiniz")

#hesap amkinesi

# sayi1 = int(input("birinci sayiyi giriniz: "))
# sayi2 = int(input("ikinci sayiyi giriniz: "))
# islem = (input("lutfen bir islem giriniz: "))

# if islem == '+':
#     print(sayi1 + sayi2)
# elif islem == '-':
#     print(sayi1 - sayi2)
# elif islem == '*': 
#     print(sayi1*sayi2)
# elif islem == '/':
#     print(sayi1/sayi2)                


#sayi tek mi cift mi

# sayi = int(input("Bir sayi giriniz: "))

# if sayi % 2 == 0:
#     print(sayi, "Bir cift sayidir.")
# elif sayi == 0:
#     print(sayi , "sifir sayisi girdiniz.")    
# else: 
#     print(sayi, "Bir tek sayidir.")    

#vucud kitle endeksi hesaplama



# boy = float(input("Lutfen boyunuzu giriniz: "))
# kilo = float(input("Lutfen kilonuzu giriniz: "))

# bmi = kilo / (boy**2)

# if bmi < 18.5:
#     print("Bu kisi zayif")
# elif 18.5 <=  bmi  < 25:
#     print("Bu kisi normal sinirlarda")
# elif 25 <= bmi < 29.9:
#     print("Bu kisi fazla kilolu")
# else:
#     print("Bu kisi obez")       

# students = ["Ali", "Ayse", "Mehmet"]

# ages = [14, 15, 14]

# for i in range(len(students)):
#     print(students[i] ,"-",  ages[i], "yasindadir")
    
#     #print(f"{students[i]} - {ages[i]} yasindadir ")
  

#cift asiyalin karelerini listeye ekle

# liste=[]

# for i in range(1,21):
#     if i % 2 ==0:
#         kare = i*i
#         liste.append(kare)

# print(liste)

#fav film listesi


# filmler = []
# for i in range(3):
#     films = input("Lutfen 3 film giriniz: ")
#     filmler.append(films)



# print(filmler) 
# print(filmler[0])
# print(filmler[-1])  
# print(len(filmler)) 


#kargo takip 

# t = ()

# isim = "ali"
# no = 123
# sehir = "Amsterdam"

# t = ("Ali", "123", "Amsterdam")

# print(t)

#set

# isimler = ["Ali", "Zeynep", "Ali", "Fatma"]

# kume = set(isimler)

# print(kume)



#kelime analizi

# cumle = input("bir cumle giriniz: ")

# bosluksuz_cumle = cumle.replace(" ","")

# print(len(bosluksuz_cumle))

# kelime_sayisi= cumle.split()

# print(len(kelime_sayisi))

# benzersiz_kelimeler = set(kelime_sayisi)

# print(benzersiz_kelimeler)

# en_uzun=max(kelime_sayisi , key=len)

# print(en_uzun)

###############################dictionary

#harf sayaci

# cumle = input("Bir cumle giriniz:")

# s = {}


# for i in cumle:
#     if i.isalpha():
#         s[i]=s.get(i,0)+1

# print(s)

#kullanici bilgi kaydi

kullanici_bilgileri={'ad': [],
                     'yas': [],
                     'sehir': []}

for i in range(2):
    ad = input("Adiniz: ")
    yas = input("Yas: ")
    sehir = input("sehir: ")

    kullanici_bilgileri['ad'].append(ad)    
    kullanici_bilgileri['yas'].append(yas)
    kullanici_bilgileri['sehir'].append(sehir)






print(kullanici_bilgileri)

