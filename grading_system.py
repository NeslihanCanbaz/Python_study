
students ={}

ogrenci_sayisi = int(input("Kac ogrenci olacak: "))

for i in range(ogrenci_sayisi):
    isim = input("Ogrenci ismi giriniz: ")
    notlar = input("Ogrencinin notlarini giriniz: ")
    students[isim] = list(map(int,notlar.split()))

print(students)    


genel_ort = []

ortalamalar ={}

for key in students:
   ort = int(sum(students[key])/len(students[key]))
   genel_ort.append(ort)
   ortalamalar[ort]= key
         
print("Ogrencilerin ortalamalari: ", ortalamalar)

#print(genel_ort)



print(ortalamalar[max(genel_ort)], " isimli ogrencinin ortalamasi en yuksek ve: " ,  max(genel_ort))





