# Day 3 Python
# PYTHON LOOPS, CONDITIONAL STATEMENTS
# Sebuah fitur untuk mengulang suatu perintah dengan kondisi tertentu


# name = 'Adi Nugraha'
# school = "Purwadhika"
# program = "Data Science - JCDS 2602"
# import math

# umur = int(input("Masukkan umur anda : "))

# if umur >= 18 and umur < 30:
#     print("Anda sudah berusia 18 tahun")
# elif umur >= 30:
#     print("Anda sudah berusia 30 tahun")
# else:
#     print("Anda belum berusia 18 tahun")

# BOOLEAN

# condition1 = True
# condition2 = False

# print(condition1, condition2)

# COMPARISON OPERATOR
# >, <, >=, <=, ==, !=

# print(condition1 == condition2)

# LOGICAL OPERATOR
# and, or, not

# x = 17
# y = 34

# print(x > y and x < y)
# print((x > y) and (x < y)) #Bisa juga seperti ini

# print(x > y or x < y)
# print((x > y) or (x < y)) #Bisa juga seperti ini


# print(not(x > y))


#===============================================================
# CONDITIONAL STATEMENTS

# IF ELSE STATEMENT

# x = int(input("Masukkan angka : "))

# if x % 2 == 0:
#     print(f"{x} adalah bilangan genap")
# else:
#     print(f"{x} adalah bilangan ganjil")

# if x >= 17:
#     print(f"berhasil membuat SIM")
# else:
#     print(f"Tidak berhasil membuat SIM")


# # IF ELIF ELSE STATEMENT

# umur = int(input("Masukkan umur anda : "))

# if umur >= 18 and umur < 60:
#     print("Anda sudah berusia 18 tahun atau lebih")
# elif umur >= 60:
#     print("Anda sudah berusia 60 tahun atau lebih")
# else:
#     print("Anda masih dibawah umur atau sudah tiada")


#=================================================================

# LOOPING STATEMENTS (Pengulangan sampai kondisi terpenuhi)

# FOR LOOP (Pengulangan sampai kondisi terpenuhi) ===================================

# Looping using range

# for x in range(1,101):
#     print('Saya ingin belajar data science')

# Looping using list

# for item in [1,2,3,4,5]:
#     print(item) # Cara 1

# print(list(range(1,11))) # Cara 2

# # increment
# for item in range(1,21,2):
#     print(item)

# # decrement
# for item in range(10,0,-1):
#     print(item)

# Soal, masukan range angka 1-20 apabila kelipatan 5 maka print angka adalah kelipatan 5
# for item in range(1,21):
#     if item % 5 == 0:
#         print(f'{item} adalah kelipatan 5')
#     else:
#         print(f'{item}')

# WHILE (Pengulangan sampai kondisi false) ===================================

# i = int(input("Masukkan angka : "))

# while i <= 10: # While biasanya menggunakan kondisi
#     print('Saya ingin belajar')
#     i += 1

# Contoh While loop
# num = 1
# while num <= 100:
#     print(num, 'yaudah', sep =" ")
#     num += 1


# Cetak 1-100 hanya genap
# num = 1  
# while num <= 100:
#     if num % 2 == 0:
#         print(num, sep =" ")
#     num +=1                        # Cara 1

# Algoritma password character max 6 and alphanumeric
# Contoh password123

# password = str(input("Masukkan password : "))

# while not(len(password) == 6 and password.isalnum()):
#     print("Password tidak berhasil, masukan password lagi : ")
#     password = str(input("Masukkan password : "))
# else:
#     print("Berhasil")



# while len(password) <= 6 and (password.isalnum() == True):
#     print("Password tidak berhasil, masukan password lagi")
#     password = int(input("Masukkan password : "))
    
# else:
#     print("Berhasil")

# CATATAN =======================================================
# Pakai kurung bulat () -> Tuple, function, math operation
# print()
# string.lower()
# (4 + 5)**2
# Pakai kurung siku [] -> Subseting, indexing, slicing, list
# Kurung keriting {}
# Dictionary
# set
# Pakai format string / fstring f"Ini adalah {angka}"

#===============================================================
#==========================LATIHAN==============================

# nilai = int(input("Masukkan nilai : "))

# if nilai >= 90 and nilai <= 100:
#     Grade = "A"
# elif nilai >= 80 and nilai < 90:
#     Grade = "B"
# elif nilai >= 70 and nilai < 80:
#     Grade = "C"
# elif nilai >= 60 and nilai < 70:
#     Grade = "D"
# elif nilai >= 50 and nilai < 60:
#     Grade = "E"
# else:
#     Grade = "F"

# print(f"Nilai anda {nilai}, Grade {Grade}")

# SOAL 1 ===================================================

# x = int(input("Masukkan angka : "))

# if x % 2 == 0:
#     print(f"Angka {x} adalah bilangan genap")
# else:
#     print(f"Angka {x} adalah bilangan ganjil")

# SOAL 2 ===================================================
# rentang 1 - 100 ganjil genap

# Cara 1
# x = int(input("Masukkan angka : "))

# if x >= 1 and x <= 100:
#     if x % 2 == 0:
#         print(f"Angka {x} adalah bilangan genap")
#     else:
#         print(f"Angka {x} adalah bilangan ganjil")
# else:
#     print("Bilangan yang diinput tidak sesuai")

# # Cara 2
# y = int(input("Masukkan angka : "))
# if (x >= 1 and x <= 100) and (y % 2 == 0): # bisa seperti ini 
#     print(f"Angka {y} adalah bilangan genap")
# elif (1 <= y <= 100) and (y % 2 != 0): # atau bisa seperti ini
#     print(f"Angka {y} adalah bilangan ganjil")
# else:
#     print("Bilangan yang diinput tidak sesuai")



# GRADE VS UNIV (IF ELIF WITH LOGICAL OPERATOR EXAMPLE)
# nilai = int(input("Masukkan nilai : "))
# domisili = str(input("Domisili [ Jabodetabek / non Jabodetabek ]: ")).lower()

# if nilai >= 90 and nilai <= 100:
#     Grade = "A"
#     if domisili == "jabodetabek":
#         print("Selamat anda mendapatkan beasiswa")
#     else:
#         print("Selamat anda mendapatkan PTN")
# elif nilai >= 80 and nilai < 90:
#     Grade = "B"
#     if domisili == "jabodetabek":
#         print("Selamat anda mendapatkan beasiswa")
#     else:
#         print("Selamat anda mendapatkan PTN")
# elif nilai >= 70 and nilai < 80:
#     Grade = "C"
#     if domisili == "jabodetabek":
#         print("Anda tidak mendapatkan beasiswa")
#     else:
#         print("Maaf anda tidak mendapatkan PTN")
# elif nilai >= 60 and nilai < 70:
#     Grade = "D"
#     if domisili == "jabodetabek":
#         print("Anda tidak mendapatkan beasiswa")
#     else:
#         print("Maaf anda tidak mendapatkan PTN")
# elif nilai >= 50 and nilai < 60:
#     Grade = "E"
#     if domisili == "jabodetabek":
#         print("Anda tidak mendapatkan beasiswa")
#     else:
#         print("Maaf anda tidak mendapatkan PTN")
# else:
#     Grade = "F"

# print(f"Grade anda adalah {Grade}")