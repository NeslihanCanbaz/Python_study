students = {}

for i in range(3):
    name = input("Öğrenci adı: ")
    grade1 = int(input("1. not: "))
    grade2 = int(input("2. not: "))
    grade3 = int(input("3. not: "))

    students[name] = [grade1, grade2, grade3]

print("\nOrtalamalar:")

best_student = ""
best_avg = 0

for name in students:
    avg = sum(students[name]) / 3
    print(name, "ortalama:", avg)

    if avg > best_avg:
        best_avg = avg
        best_student = name

print("\nEn yüksek ortalama:", best_student, best_avg)