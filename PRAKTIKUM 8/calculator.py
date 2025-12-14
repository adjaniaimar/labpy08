try:
    a = int(input("Input bilangan pertama  : "))
    b = int(input("Input bilangan kedua    : "))
except ValueError:
    print("ERROR! BILANGAN HARUS BERUPA ANGKA")
    exit()

print("Operasi")
print("1. Penambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("===========================")

c = input("Pilih operasi : ")

try:
    if c == "1":
        h = a + b
    elif c == "2":
        h = a - b
    elif c == "3":
        h = a * b
    elif c == "4":
        h = a / b
    else:
        raise Exception("ERROR! OPERASI TIDAK VALID")
except ZeroDivisionError:
    print("ERROR! TIDAK BISA MEMBAGI NOL")
    exit()
except Exception as e:
    print(e)
    exit()

print("Hasil dari operasi adalah :", h)