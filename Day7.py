# Day 7 Python
# Python Function
# Suatu perintah dalam bentuk blok code yang dapat dipanggil 
# Memiliki nama, dapat menerima input dan mengeluarkan output
# Function dapat digunakan berkali - kali


# name = 'Adi Nugraha'
# school = "Purwadhika"
# program = "Data Science - JCDS 2602"

#================================================================

# BUILT IN FUNCTION

# print()
# input()
# len()
# type()
# int()
# float()
# str()
# bool()
# list()
# tuple()
# dict()
# set()
# min()
# max()
# sum()

# print("Hello World") # -- > Hello world = argument

# ----------------------------------------------------------------
# Regular function
# def nama_function(parameters):
#     return statement

# Cara 1
# def tambah(angka1, angka2):
#     return angka1 + angka2

# Cara 2
# def tambah(angka1, angka2):
#     hasil = angka1 + angka2
#     return hasil

# print(tambah(2,2))
# print(tambah('Adi', ' Nugraha'))

# ----------------------------------------------------------------
# 1. Function without input (parameters) and output (return)

# Mendefine function
# def helloWorld():
#     print("Hello World")

# helloWorld()

# Function with input (parameters) and output (return)
# def helloWorldSatu():
#     return "Hello World Satu"

# print(helloWorldSatu())

#----------------------------------------------------------------
# 2. Funciton with input parameters and output (return)

# Syntax : 
# def nama_function(parameters):
#     statement 1
#     statement 2

#----------------------------------------------------------------

# Case function 1.
# Perkenalan diri

# def perkenalanDiri(name, age, background):
#     print('Halo nama saya', name, 'umur saya', age, 'background saya', background)

# Penulisan tanpa parameter harus berurutan
# perkenalanDiri('Adi Nugraha', 24, 'Purwadhika')

# Penulisan tidak berurutan, define nama parameter
# perkenalanDiri(age = 24, background = 'Purwadhika', name = 'Adi Nugraha')

# ----------------------------------------------------------------

# Default parameter (jika user tidak memasukan parameter)
# def perkenalanDiri(name = 'Anonim', age = 'N/A', background = 'N/A'):
#     print('Halo nama saya', name, 'umur saya', age, 'background saya', background)

# perkenalanDiri('Adi Nugraha', 24)
# perkenalanDiri('Adi Nugraha')

# # Parameter yang wajib diisi
# def perkenalan(name, age = 'N/A', background = 'N/A'):
#     print('Halo nama saya', name, 'umur saya', age, 'background saya', background)

# # perkenalan() -> error

# perkenalan('Adi Nugraha')

# ----------------------------------------------------------------

# 3. Function with input parameters and output (return)
# Syntax :
# def nama_function(parameters):
#     return statement

# contoh 1 : buat function pangkat2

# angka =  int(input('Masukan angka : '))
# def pangkat2(angka):
#     return angka**2

# print(pangkat2(angka))

# contoh 2 : input angka dan pangkat

# angka =  int(input('Masukan angka : '))
# pangkat =  int(input('Masukan pangkat : '))

# def hitungPangkat (angka, pangkat):
#     return angka**pangkat

# print(hitungPangkat(angka, pangkat))

#----------------------------------------------------------------
# 1. Local variable

# Variabel yang berada di dalam function
# Berlaku hanya untuk di dalam function
# Tidak tersimpan di ram sehingga tidak dapat dipanggil
# Ketika function sudah selesai di jalankan, variabel tersebut akan hangus

# def kali(angka1, angka2):
#     hasil_kali = angka1 * angka2
#     return hasil_kali

# print(kali(2,2))

#----------------------------------------------------------------
# 2. Global variable
# Variabel yang terletak di luar function
# dapat dipanggil kembali
#


# x = 10
# def aritmatika(angka1, angka2):
#     x = x+10
#     x = (angka1 + angka2)*x
#     return x
# Error ------------------

#Solution 1 

# def aritmatika(angka1, angka2):
#     x = 10
#     x = x+10
#     x = (angka1 + angka2)*x
#     return x

#Solution 2

# x = 10
# def aritmatika(angka1,angka2):
#     global x
#     x += 10
#     return (angka1+angka2)*x

# print(aritmatika(1,2),x)
    
#-----------------------------------------
# Callback Function
# Function di dalam function

# Function kali, bagi, tambah, kurang

# def kali(num1,num2):
#     hasil = num1*num2
#     return hasil
# def bagi(num1,num2):
#     hasil = num1/num2
#     return hasil
# def tambah(num1,num2):
#     hasil = num1+num2
#     return hasil
# def kurang(num1,num2):
#     hasil = num1-num2
#     return hasil

# def kaBaTaKu(fnOperator, angka1, angka2):
#     hasilKabataku = fnOperator(angka1,angka2)
#     return hasilKabataku

# print(kaBaTaKu(kali, 9, 5))
# print(kaBaTaKu(bagi, 9, 5))
# print(kaBaTaKu(tambah, 9, 5))
# print(kaBaTaKu(kurang, 9, 5))

#---------------------------------------------------
# Calling other function
# menjadikan function sebagai suatu operasi didalam function 

# import math

# def kuadrat(diameter):
#     jariJari = (diameter/2)**2
#     return jariJari

# def luasLingkaran(r):
#     hasil = math.pi * kuadrat(r)
#     return hasil

# print(luasLingkaran(10))

#---------------------------------------------
# Recursive function
# Ada function yang sama di dalam function yang dibuat

# def menu1():
#     print("Ini menu satu, berikut adalah daftar buah")

# def menu2():
#     print("Masukan nama buah yang ingin ditambahkan")

# def menu3():
#     exit()

# def menuUtama():
#     inputMenu = int(input("Masukan menu yang akan dipilih : "))

#     if inputMenu == 1:
#         menu1()             # Calling other function
#         menuUtama()         # Recursive function
#     elif inputMenu == 2:
#         menu2()
#     else:
#         menu3()

# menuUtama()

#---------------------------------------------
# Python map and filter function

# MAP
# map() untuk memetakan hasil function dan collection data types
# tanpa mengurangi hasilnya 

# listAngka = [1,2,3,4,5]

# Outputnya : [1,8,27,64,125]
# pangkatTiga = lambda x: x**3
# print(map(pangkatTiga, listAngka)) --- > salah karena tidak di CASTING menjadi list
# print(list(map(pangkatTiga, listAngka)))

# Soal 1
# nilai = [80,70,65,100,95]
# # output : ['lulus', 'tidak lulus', 'tidak lulus', 'lulus', 'lulus']
# lulus = lambda x: 'lulus' if x > 80 else "tidak lulus"
# print(list(map(lulus, nilai)))

# # Bisa juga (grade tidak perlu disimpan)
# print(list(map(lambda x: 'lulus' if x > 80 else "tidak lulus", nilai)))


#---------------------------------------------
# LAMBDA FUNCTION
# Syntax : 
# lambda parameter: expression
# Dapat memiliki beberapa parameter
# Expression hanya 1

# 1. Cara reguler function
# def kuadrat(x):
#     return x**2

# ----->

# 2. Lambda function
# kuadratLambda = lambda x: x**2
# print(kuadratLambda(3))

# Case 1. mencari luas lingkaran dengan lambda function

# import math
# kuadratLambda = lambda x: x**2
# luasLingkaran = lambda r: math.pi * kuadratLambda(r)
# print(luasLingkaran(10))

# Memanggil kabataku dengan lambda
# kabataku = lambda fnOperator, angka1, angka2 : fnOperator(angka1,angka2)
# print(kabataku(kali,2,5))

#--------------------------------------------------
# FILTER FUNCTION
# filter() untuk memfilter hasil function dan collection data types
# dengan mengurangi hasilnya
# filter (function, collection)

# listAngka = [1,2,3,4,5]
# # output = [1,3,5]

# angkaGanjil = lambda x: 'genap' if x %2 == 0 else 'ganjil'
# print(list(filter(angkaGanjil, listAngka)))

#----------------------------------------------
# Exercise

# nilai = [80, 70, 65, 100, 95]

#1. [65, 70]
# tidakLulus = lambda x: x if x > 80 
# print(list(filter(tidakLulus, nilai)))

# tidakLulus = lambda x: x < 80
# print(list(filter(tidakLulus, nilai)))

# def tidakLulus(x):
#     return x < 80

# print(list(filter(tidakLulus, nilai)))

# tidakLulus = lambda x: x if x < 80 else False
# print(list(filter(tidakLulus, nilai)))

#2. [65, 100]

# def minMax (x):
#     return x > 65 and x < 100
# print(list(filter(minMax, nilai)))

# minMax = lambda x: x if min(nilai) == x or max(nilai) == x else False

# print(sorted(list(filter(minMax, nilai))))
