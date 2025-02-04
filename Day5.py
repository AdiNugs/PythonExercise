# Day 5 Python
# COLLECTION DATA TYPES
# Sebuah fitur untuk mengulang suatu perintah dengan kondisi tertentu


# name = 'Adi Nugraha'
# school = "Purwadhika"
# program = "Data Science - JCDS 2602"

#================================================================

# list_contoh = ["hello", 1, 2.5, True, 100, 100, 100]
# print(list_contoh)

# # Indexing
# print(list_contoh[-1])
# print(list_contoh[-1:-4:-1])
# print(list_contoh[-3:])

# # Mutables
# list_contoh[0] = "hi"
# print(list_contoh)

#===================================================

# Mengecek apakah ada 3 dalam list contoh
# list_contoh = ["hello", 1, 2.5, True, 100, 100, 100]
# print(3 in list_contoh)
# print(3 not in list_contoh)
# print(1, 2.5, True in list_contoh) # (Tidak bisa) Hanya mengecek kondisi terakhir
# print((1 in list_contoh) and (5 in list_contoh))

#===================================================

# Check index dalam list
# list_contoh = ["hello", 1, 2.5, True, 100, 100, 100]

# print(list_contoh.index(2.5))
# print(list_contoh.count(100)) # yang muncul pertama

# Mencari true pada list
# for x, y in enumerate(list_contoh): # x, y karena perlu di ucpack dari tuple
#     if y is True:
#         print(x)

# Note '==' equal 'is' 
# Untuk validasi boolean menggunakan 'is'
# Supaya 1 tidak dianggap True

#===================================================

# list_contoh = ["hello", 1, 2.5, True, 100, 100, 100]
# print(len(list_contoh))

# list_contoh2 = ["hello", 1, 2.5, True, [100, 100, 100]]
# print(len(list_contoh2))

# inner_list = list_contoh2[-1]
# print(len(inner_list))

#===================================================

# Menyalin data dalam list 
# list_contoh = ["hello", 1, 2.5, True, 100, 100, 100]

#===================================================

# Referencing

# list_contoh = ["hello", 1, 2.5, True, 100, 100, 100]
# list_contoh2 = ["hello", 1, 2.5, True, [100, 100, 100]]
# inner_list = list_contoh2[-1]
# inner_list[0] = 'b'
# print(list_contoh2)

# .copy()

# list_contoh2_copy = list_contoh2.copy()
# list_contoh2_copy[0] = 'hi'
# print(list_contoh2_copy)
# print(list_contoh2)

# # using slicing and copy
# inner_list = list_contoh2[-1].copy()
# inner_list[0] = 'b'
# print(inner_list)
# print(list_contoh2)

# list_contoh_copy = list_contoh2.copy()
# inner_list_copy = list_contoh_copy[-1]
# inner_list_copy[0] = '1000'
# print(list_contoh_copy)
# print(list_contoh2)

#===================================================

# List concatenating

# listBuah = ['apel','anggur','jeruk','mangga']
# listHewan = ['macan','kucing','semut','kecoa']
# listMobil = ['mobil1','mobil2','mobil3']

# 1. Cara +
# Untuk > 1 list yang ingin digabungkan
# listGabung = listBuah + listHewan
# print(listGabung)

# 2. Cara extend
# Untuk penambahan satu list saja
# listBuah.extend(listHewan)
# print(listBuah)

# Ketika menggunakan extend, --> sudah tersimpan langsung perubahannya

#===================================================

# Add data ke dalam list

# Cara 1. Append
# listMobil = ['Toyota','Honda','BMW','Tesla', 'Hyundai']
# mobilNew = 'Wuling'

# listMobil.append(mobilNew)
# print(listMobil)
# listMobil.append('Wuling')

## add > 1 data
# listMobil = ['Toyota','Honda','BMW','Tesla', 'Hyundai']
# mobillNew = ['Wuling', 'Mercedez']
# listMobil.append(mobilNew)
# print(listMobil)     
# === > hasilnya list dalam list

# print(listMobil + mobilNew)
# === > hasilnya melebur jadi satu list


# Cara 2. Insert
# Menambahkan data pada index tertentu

# listMobil.insert(1, mobillNew)
# print(listMobil)


#===================================================

# Remove data dalam list

# Cara 1. Remove (Method)
# listNama = ['satrio','adrian','hans','abe', 'ridho']
# print(listNama)

# listNama.remove('abe')
# print(listNama)

# Cara 2. Pop (Method)
# listNama.pop(1) 
# print(listNama)

# Cara 3. del 
# del listNama[0]
# print(listNama)
# del listNama[0:2]
# print(listNama)
# del listNama (menghapus variable listNama)

# Cara 4. clear
# listNama.clear() (menghapus seluruh value dalam list)
# print(listNama)

#===================================================

# Sort list

# listMix = [1, 'Satrio', 2, 'Ridho', 3, '-'] # print(listMix.sort()) ===== > Error tidak bisa sort int
# listMix = ['1', 'Satrio', '2', 'Ridho', '3', '-']
# listMix.sort()
# print(listMix)

# #descending
# listMix.sort(reverse=True)
# print(listMix)

# List int dan float
# angka = [1, 10.4, 2, 7.8, 0.2, True]
# angka.reverse()     # ===================> membalikan index bukan value
# angka.sort()
# print(angka)

#===================================================

# List 2 dimensi

# listStud = [['Adi', 'BSD'], ['Hans', 'Kembangan'], ['Claire', 'Bintaro']]

# print(listStud)
# print(listStud[0][0])

# List 3 dimensi

# list3d = [[['Apel', 20, True], ['Mangga', 5, False]], 
#           [['Wortel', 10, False], ['Bayam', 2, True]]]

# print(list3d)

# Soal: Keluarkan 'Apel', 'Mangga', 'Wortel', dan 'Bayam'
# Manual
# print(list3d[0][0][0])
# print(list3d[0][1][0])
# print(list3d[1][0][0])
# print(list3d[1][1][0])

# Otomatis
# Cara 1
# for item in list3d:
#     for item2 in item:
#         print(item2[0])

# Cara 2 pakai tipe data string
# for item in list3d:
#     for item2 in item:
#        for item3 in item2:
#            if type(item3) is str: #Type untuk membandingkan tipe data
#                print(item3)
#===================================================

# List comprehension

# manual
# alist = [1,2,3,4]
# print(alist)

# range 
# jarak = list(range(1,5))
# print(jarak)

# loop
# Soal 1: buat list yang berisi 1 - 31 dengan for loop

# container = []
# for i in range(1,32):
#     container.append(i)
# print(container)

# ubah diatas menjadi list comperhension

# list31 = [i for i in range(1,32)]
# print(list31)

# contoh genap 1-5

# newListNumber = [number for number in range(1,7) if number % 2 == 0]
# print(newListNumber)

# Soal 2 : buat list yang berisi nilai rentang 1-31 tpai hanya genap

# Cara list comperhension
newListNumber = [number for number in range(1,32) if number % 2 == 0]
print(newListNumber)

# Soal 3 : keluarkan list yang berisi [1, 10, 100, 1000]
# Cara for manual
angka = []
for i in range(4):
    angka.append(10**i)
print(angka)      

# Cara list comperhension
angka = [10**i for i in range(4)]
print(angka)
