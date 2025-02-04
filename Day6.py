# Day 6 Python
# COLLECTION DATA TYPES Part 2
# Tuple Dictionary Set
# Sebuah fitur untuk mengulang suatu perintah dengan kondisi tertentu


# name = 'Adi Nugraha'
# school = "Purwadhika"
# program = "Data Science - JCDS 2602"

#================================================================

# TUPLE
# Ditandai dengan ()
# Immutable -- > tidak bisa diubah, didelete
# Dapat mengandung beberapa tipe data
# Bisa duplikat
# Berurutan, sehingga dapat diindexing

# aTuple = ('hello', 1, 2.5, True, 100, 100, 100)

# Bisa diindexing
# print(aTuple[2]) # Positive indexing
# print(aTuple[-5]) # Negative indexing

# Immutable

# Tuple 1
# tuple1 = (25)
# print(tuple1, type(tuple1)) ----- > penulisan salah, akan terbaca int

# tuple1 = (25,)
# print(tuple1, type(tuple1))

#================================================================

# Concatenating
# aTuple = ('hello', 1, 2.5, True, 100, 100, 100)
# tuple1 = (25,)

# Cara 1
# newTuple = aTuple + tuple1
# print(newTuple) 

# Cara 2 Insert (Harus dicasting ke list)
# aList = list(aTuple)
# list1 = list(tuple1)
# aList.insert(0, list1) # menambahkan pada index 0
# print(aList)

# newTuple2 = tuple(aList)
# print(newTuple2)

# Cara 3. __add__
# newTuple3 = aTuple.__add__(tuple1) # mirip extend
# print(newTuple3)

# ==============================================
# unpacking 
# list_buah  = ['apel', 'buah']
# a, b = list_buah
# print(a)

# Catatan 
# print * sebelum variable untuk menghilangkan bentuk list / tuple

# print(*newTuple3)

#==============================================

# DICTIONARY
# Ditandai dengan {'key' : 'value'}
# Immutable -- > tidak bisa diubah, didelete
# Dapat mengandung beberapa tipe data dari 'value'
# Bisa duplikat pada 'value'
# Tidak berurutan, sehingga tidak dapat diindexing
# Dapat diindexing dengan key
# Biasa digunakan ketika data yang dimiliki mempunyai grup / karakteristik yang sama


# MEMBUAT DICTIONARY
# Cara manual
# stud = {"name" : "Adi", 
#         "age" : 24, 
#         "school" : "Purwadhika", 
#         "isStudent" : True}

# Cara menggunakan dict
# stud = dict(name = "Adi", age = 24, school = "Purwadhika", isStudent = True)
# print(stud)

# Menampilkan value
# print(stud['name'])
# print(stud['school'])
# print(stud['isStudent'])

# Add data pada dictionary
# stud['hobby'] = 'Coding'
# print(stud)

#-------------------------------------------------------

# Duplicate key di dalam dictionary
# 1. Cara satu (Value dari key yang sama terganti)
# stud = {"name" : "Adi", 
#          "age" : 24, 
#          "school" : "Purwadhika", 
#          "isStudent" : True,
#          "name" : "Ahmad" }

# print(stud)

# 2. Cara kedua (Value dari key yang sama tidak terganti)
# stud_new = {"name" : ["Adi", "Ahmad"], 
#          "age" : 24, 
#          "school" : "Purwadhika", 
#          "isStudent" : True }

# print(stud_new)

# 3. Cara ketiga ---- > bisa diupdate pada object dict lama
# stud['name'] = ["Adi", "Ahmad"]
# print(type(stud["name"]))

#-------------------------------------------------------

# Method pada dictionary
# stud.keys() # Menampilkan key
# stud.values() # Menampilkan value
# stud.items() # Menampilkan key dan value

# stud = {"name" : "Adi", 
#          "age" : 24, 
#          "school" : "Purwadhika", 
#           "isStudent" : True}

# # Hanya key dari dictionary
# print(stud.keys())  

# # Hanya value dari dictionary
# print(stud.values())

# # Key dan value dari dictionary
# print(stud.items())

# # Manfaatkan pada looping
# for key in stud.items():
#     print(key)

# # Di Unpack
# for key, items in stud.items():
#     print(key, items)

# Menampilkan key
# for key in stud.keys():
#     print(key)

# Menampilkan value
# for value in stud.values():
#     print(value)

#-------------------------------------------------------

# 2D Dictionary
# menu = {
#     "ayam" : {
#         "name" : "Ayam Goreng",
#         "price" : 15000,
#         "qty" : 10
#     },
#     "bakso" : {
#         "name" : "Bakso goreng",
#         "price" : 15000,
#         "qty" : 5
#     },
#     "mie" : {
#         "name" : "Mie Godog",
#         "price" : 15000,
#         "qty" : 5
#     }
# }

# print(menu)

# Menampilkan value
# for value in menu.values():
#     print(value)

# # Hanya mengambil key 
# for key in menu.keys():
#     print(key)

# for key, values in menu.items():
#     print(key)
#     print(values)

# Menganbil bakso goreng
# print(menu["bakso"]['name'])

# # Mengambil dict mie
# print(menu["mie"])
# print(menu["mie"].values())

# # Mengambil dengan casting menjadi list
# print(list(menu.values())[2])


# ===============================================
# Soal 1
# Buat list isinya ['nasi goreng', 'pudding', 'dimsum', 'teh tarik']

# Cara manual 
# print(menu['ayam']['name'])
# print(menu['bakso']['name'])
# print(menu['mie']['name'])

# Cara method
# print(list(menu.values())[0]['name'])
# print(list(menu.values())[1]['name'])
# print(list(menu.values())[2]['name'])

# for loop 

# list_menu = []
# for item in menu.values():
#     list_menu.append(item['name'])

# print(list_menu)

# Cara dictionary comprehension
# list_menu = [item['name'] for item in menu.values()]
# print(list_menu)

# Cara range

# list_menu = []
# for item in range(3):
#     list_menu.(item(menu.values())[item]['name'])
# print(list_menu)

#-------------------------------------------------------

# Dictionary Comprehension
# Tujuan untuk efisiensi code dalam pembuatan dict

# Case 1: {1:1, 2:8, 3:27}

# case1 = {num: num**3 for num in range(1,4)}
# print(case1)

# Case 2: {1: 'Ganjil', 2: 'Genap', 3: 'Ganjil'}

# case2 = {num: 'Ganjil' if num % 2 != 0 else 'Genap' for num in range(1,6)}
# print(case2)

#-------------------------------------------------------

# SET
# Ditandai dengan {}
# Immutable
# Boleh memiliki tipe data yabg beragam
# Tidak ada duplikasi
# Tidak ada index
# Biasa digunakan untuk handling duplicate value

# aSet = {1,2,3,4,5,100,'a','aa',5}
# print(aSet)

# casting ke list --- > prosesnya jadi set dulu
# sehingga urutannya menyesuaikan dengan hasil set
# aList = list(aSet)
# print(aList)

#-------------------------------------------------------
# Loopong in set

# aSet = {1,2,3,4,5,100,'a','aa',5}

# for item in aSet:
#     print(item)

#-------------------------------------------------------
# Add data pada set

# menambahkan satu value
# aSet = {1,2,3,4,5,100,'a','aa',5}
# aSet.add(500)
# print(aSet)

# menambahkan beberapa value
# aSet = {1,2,3,4,5,100,'a','aa',5}
# aSet.update({'abe', 'ketua kelas'})
# print(aSet)

#-------------------------------------------------------
# Delete data pada set
# aSet = {1,2,3,4,5,100,'a','aa',5}

# Remove error apabila value tidak ada
# aSet.remove(1000)
# print(aSet)

# Discard tidak error jika value tidak ada
# aSet.discard(2)
# print(aSet)

#-------------------------------------------------------
# Method in SET
# Union, Interssection, Diffrence, Symmetric Diffrence 

# ganjil = {1,3,5,7,9}
# prima =  {2,3,5,7,11}

# # Union --> full outer join
# print(ganjil.union(prima))

# # Intersection --> inner join
# print(ganjil.intersection(prima))

# # Difference --> Left outer join
# # yang ada di ganjil tetapi tidak ada di prima
# print(ganjil.difference(prima))

# # Symmetric Difference --> full outer join
# # selain yang irisan dari kedua set
# print(ganjil.symmetric_difference(prima))

# -------------------------------------------------------
# DISJOINT, SUBSET, SUPERSET

setGanjil = {1,3,5,7,9}
setGenap = {2,4,6}
setAngka = {3,5}

# Disjoint --> tidak ada irisan antara kedua set
print(setGanjil.isdisjoint(setAngka))

# Subset --> ada irisan antara kedua set
print(setGanjil.issubset(setAngka))
print(setAngka.issubset(setGanjil))

# Superset --> ada irisan antara kedua set
print(setGanjil.issuperset(setAngka))
print(setAngka.issuperset(setGanjil))

