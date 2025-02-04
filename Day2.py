# Day 2 Python
# PYTHON VARIABLE
# Sebuah fitur untuk menyimpan suatu nilai

# name = 'Adi Nugraha'
# school = "Purwadhika"
# program = "Data Science - JCDS 2602"

# welcome = '''Selamat datang di program Data Science 
# hari jum'at '''

# print(name, school, program)
# print(welcome)
# print(type(name)) #Check data type

#================================================================

# Case Styling
# 1. Camel Case

# myfruit = "Grape"
# myfruit = "Apple" #Overwrite
# print(myfruit)

# 2. Snake Case

# my_fruit = "Grape"
# print(my_fruit)
# print(type(my_fruit)) #Check data type 

#================================================================

# Data Type

# nama = "Adi Nugraha"
# umur = 24
# ukuranSepatu = 43.5

# 1. String
 # String + Variable
# print("Hello "+nama+"!")
# print("Hello",nama,"!")
# print(f"Hello {nama}!") # F-String

# 2. Integer

# print(f'Umur {nama} adalah {umur}' )
# print(type(umur))
# 3. Float

# print (f'Ukuran sepatu {nama} adalah {ukuranSepatu}')
# print(type(ukuranSepatu))

# 4. Boolean
# boolean1 = True
# boolean2 = False

#================================================================

# Soal nomor 1
# Tentukan hasil dari 5 + 2 : (1/2)
#Keluarkan print hasil
#Keluarkan tipe data

# jawaban = 5 + 2 / (1/2)
# print(jawaban)
# print(type(jawaban))

#================================================================

# Collection Data Tyoe
# 1. List --> Mutable

# listJob = ["Data Science", "Data Analyst", "Data Engineer"]
# stud = ["Adi", 24, "Purwadhika", True]
# print(type(stud))
# print(stud[1])
# print(stud[-1])

# listJob[0] = "Data Scientist"  # Mengganti value
# listJob.append("Data Architect") # Menambahkan value kedalam list
# print(listJob)

# # 2. Tuple --> Immutable

# tupleJob = ("Data Science", "Data Analyst", "Data Engineer")
# print(type(tupleJob))
# print(tupleJob[1])  

# # 3. Dictionary (KEY : VALUE)
# stud = {"name" : "Adi", "age" : 24, "school" : "Purwadhika", "isStudent" : True}
# print(type(stud))
# print(stud["isStudent"])

# # Dictionary + List

# studAdded = {"name" : ["Adi", "Ahmad"], "age" : [24, 25], "school" : "Purwadhika", "isStudent" : True}
# print(studAdded["name"])
# print(studAdded["name"][1])

#================================================================

# Range

# myRange = range(1,5)
# print(myRange)
# print(type(myRange))
# print(list(myRange))

# print(list(range(5, 11))) 

#================================================================

# # Set (Unordered)

# mySet = {'Adi', 'Ahmad', 'Ando'}
# print(mySet)
# print(type(mySet))

# # None

# kosong = None
# print(kosong)
# print(type(kosong))

#================================================================
#================================================================

# ARITHMETIC OPERATOR

# math.ceil(x)
# math.floor(x)
# math.fabs(x) (absolut number)
# math.pow(x,y) (x pangkat y)
# math.sqrt(x) (akar x)   
# math.pi

# x = 125000000
# y = 125e6
# y2 = 125e-6

# print(x,y)
# print(y2)
# print(125/1000000)

# Jumlah, Kurang, Kali, Bagi, Modulus, Pangkat, Floor(ke yang terendah)

# a = 12
# b = 4
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)
# print(a//b)

# ASSIGNMENT OPERATOR

# a += b # a = a + b
# print(float(a)) # Type Casting

# a %= b # a = a % b
# print(a)

# x = 4.7
# print(round(x)) # Round number

#================================================================

# MATH MODULE
# import math as m # Menggunakan alias 'm'
# from math import ceil # Tidak perlu menggunakan math.

# x = 12.7
# print(m.ceil(x))
# print(ceil(x))

#================================================================

# CASTING

# x = 123.45
# y = 12345
# print(int(x)) # FLoat to Integer
# print(float(y)) # Integer to Float
# print(str(y))   # Integer to String
# print(len(str(x))) # Length

# postCode = 22456
# postCode = str(postCode) # Integer to String
# print(type(postCode))

#================================================================

# ESCAPE CHARACTER

# txt = "Salam kenal murid "purwadhika", mari kita belajar bersama" # Error
# txt = "Salam kenal murid \"purwadhika\", mari kita belajar bersama"
# print(txt)

#\n = New Line
#\t = Tab
#\b = Backspace
#\f = Form Feed
#\r = Carriage Return

#================================================================

# STRING METHOD

# x = "Adi Nugraha"

# x = len(x)

# x = x.upper()


# x = x.lower()


# x = x.capitalize()


# x = x.title()


# x = x.swapcase()


# x = x.replace("Adi", "Adi Nugraha")


# x = x.split(" ")

#================================================================

# STRING SLICING

# x = "Adi Nugraha"

# print(x[0])
# print(x[2:])
# print(x[2:5])
# print(x[:2])
# print(x[-1])
# print(x[-2:])
# print(x[-2:-1])

#================================================================

# CHECK STRING

# x = "Adi Nugraha"

# print("Adi" in x)
# print("Adi" not in x)

#================================================================

# STRING METHOD (Print)

# text = "Saya belajar data science"


# # Count how many in string
# print(text.count("a"))
# print(text.count("Saya"))               

# # Check string length
# print(len(text))

# # Split string
# print(text.split(" "))

# # Join string
# print(" ".join(text))

# # Lower
# print(text.lower())

# # Upper
# print(text.upper()) 

# # Title
# print(text.title())


# # soal
# Keluarkan Sci
# KEluarkan science
#keluarkan ata
# keluarkan ecne
# keluarkan Sine

# x = "Data Science"
# print (x[-7:-4])
# print(x[4:])
# print(x[1:4])
# print(x[-1:-5:-1])
# print(x[5::2])

#================================================================

# USER INPUT

# vol balok (p*l*t)
# p = 3
# l = 2
# t = 5
# print(f"Volume balok adalah {p*l*t}")

# input dari user
# p = int(input("Masukkan panjang balok : "))
# l = int(input("Masukkan lebar balok : "))
# t = int(input("Masukkan tinggi balok : "))
# print(f"Volume balok adalah {p*l*t}")

# Latihan

# buat program yang bisa membuat perhitungan luas lingkaran (pi*r^2)
# Inputnya diameter

# import math 

# diameter = int(input("Masukkan diameter lingkaran : "))
# print(f"Luas lingkaran adalah {math.pi*(diameter/2)**2}")

# soal 5

apel = int(input("Masukkan jumlah apel : "))
jeruk = int(input("Masukkan jumlah jeruk : "))
anggur = int(input("Masukkan jumlah anggur : "))

apelT = apel*10000
jerukT = jeruk*15000
anggurT = anggur*20000

print("\nDetail Belanja\n")
print(f"Apel : {apel} x 10000 = {apelT}")
print(f"Jeruk : {jeruk} x 15000 = {jerukT}")
print(f"Anggur : {anggur} x 20000 = {anggurT}\n")


total = apelT + jerukT + anggurT
print(f"Total : {total} ")