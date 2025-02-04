# Day 4 Python
# PYTHON NESTED LOOPS
# Sebuah fitur untuk mengulang suatu perintah dengan kondisi tertentu


# name = 'Adi Nugraha'
# school = "Purwadhika"
# program = "Data Science - JCDS 2602"

#================================================================
#enumerate, zip, nested loop, loop control, loop drawing

# List 1 dimensi

# list_buah = ['Jeruk','Apel','Mangga','Anggur','Kecapi','Pepaya']

# Mencetak Jeruk, Mangga, Pepaya
# print(list_buah[0], list_buah[4], list_buah[5])

# # Cara 1

# for item in range(len(list_buah)):
#         if item % 2 != 0:
#             print(list_buah[item])  

# # Cara 2

# for item in list_buah:
#     if list_buah.index(item) % 2 != 0:
#         print(item)

# # Cara 3
# #(Range Start, Stop, Step)
# for item in range(1, len(list_buah), 2):
#     print(list_buah[item])

# # Keluarkan buah yang diawali huruf A

# for item in list_buah:
#     if item[0].lower() == 'a':
#         print(item) 

# inclass question kalau misalkan contain huruf a di dalam suatu kata di list
# list_buah = ['Jeruk','Apel','Mangga','Anggur','Kecapi','Pepaya']

# for item in list_buah:
#     if 'a' in item.lower():
#         print(item)

#==ENUMERATE======================================================
#Untuk mengambil pasangan index dan item pada suatu list
#Output : Tuple

# list_buah = ['Jeruk','Apel','Mangga','Anggur','Kecapi','Pepaya']

# for item in enumerate(list_buah):
#     print(item)

# Untuk unpacking

# Basic
# for index, item in enumerate(list_buah):
#     print(index, item)

# Rapih
# for index, item in enumerate(list_buah):
#     print(f"{index}. {item}")     

#======LIST 2 DIMENSI=============================================

# list_2d = [['a', 100], ['b', 200], ['c', 300]]

# #manual 
# # print(list_2d[1][1])

# # for item in list_2d:
# #     for sub_item in item:
# #         print(sub_item)

# # for loop (enumerate)
# # for index, item in enumerate(list_2d):
# #     print(item[0])
# #     print(item[1])

# # for loop nested
# for index, item in enumerate(list_2d):
#     for sub_index, sub_item in enumerate(item):
#         print(sub_item)
       
        

#unpacking
# for item in list_2d:
#     for sub_item in item:
#         print(sub_item)

# === ZIP ====================================
# Memasangkan item antara 2 list 

# list_mobil = ['toyota', 'bmw', 'tesla']
# list_negara = ['jepang', 'jerman', 'USA']

# Mobil toyota dari jepang
# Mobil bmw dari jerman
# Mobil tesla dari USA

# Manual 

# For loop biasa

# for item in range(0,3):
#     print(f"{list_mobil[item]} dari {list_negara[item]}")

# # ZIP ==================================

# list_gabungan = list(zip(list_mobil, list_negara)) # Agar bisa terlihat casting zip dengan list 
# print(list_gabungan)

# for x in (list_gabungan):
#     print(f"{x[0]} dari {x[1]}")

# STATEMENT CONTROL (Break, Continue, Pass) ============================
# BREAK ======
#print 1 - 100 dan stop saat angka 26
# for x in range(1,101):
#     if x == 27:
#         break
#     print(x)

# kalimat = 'waktu saya pulang, saya pengen mampir ke resto padang'
#ketika meemukan huruf g proses berhenti
# for item in kalimat:
#     if item.lower() == 'g':
#         break
#     print(item, end = "     ")

# CONTINUE ===== (Practical di data frame)
# print 1 - 100 dan skip angka 26
# for x in range(1,101):
#     if x == 13:
#         continue
#     print(x, end = " ")


# PASS
# place holder untuk do nothing pada looping statement
# no_hp = '0812-567-78890'

# for item in no_hp:
#     if item == '-':
#         pass
#     print(item, end = "")


# soal
# no_hp = '0812-567-78890'

# for item in no_hp:
#     if item == '-':
#         continue
#     print(item, end = "")


# hapus semua '-' dari nomor handphone dalam list 
# no_hp = ['0812-567-78890', '0812-567-78890','0812-567-78890'] 

# for item in no_hp:
#     for sub_item in item:
#         if sub_item == '-':
#             continue
#         print(sub_item, end = "")
#     print()

#==============================================================

# NESTED LOOP
# Mengerjakan inner loop duluan dan outer loop setelah inner loop selesai

# For dalam for
# Suapan 1 
# nasi
# sayur 
# lauk

# suapan = ['nasi', 'sayur', 'lauk']
# # Menggunakan for
# for item in range(1,9):
#     for sub_item in suapan:
#         print(sub_item) 
#     print(f'suapan ke {item}') # Cara 1


# for item in range(1,9):
#     print(f'suapan ke {item}')
#     for sub_item in suapan:
#         print(sub_item)        # Cara 2

# # For dalam while

# piring = 1
# while piring <= 7:
#     print(f'suapan ke {piring}')
#     piring += 1
#     for item in suapan:
#         print(item)
    
# LOOP DRAWING ===========================================
# for loop

# Kasus 1
# User bisa input angka
# contoh : 3
# * * * *
# * * * *
# * * * *

# angka = int(input("Masukan angka : "))

# for x in range(angka):
#     for y in range(1,5):
#         print("*", end = " ")
#     print()
    
 