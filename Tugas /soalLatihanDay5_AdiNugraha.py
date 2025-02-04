# Adi Nugraha - JCDS 2602
# Tugas Day 5

# ================== LIST ======================

# SOAL 1
# Find MIN MAX Value

numbers = [41, 5, 1, 3, 89, 32]

# Menggunakan sort

numbers.sort()
print('Minimum : ',numbers[0])
print('Maximum : ',numbers[-1])

# SOAL 2

# buat list berisi [1, 4, 16, 25, 49]

# for loop biasa
angka = []
for i in range(1,8):
    if i%3 != 0:
        angka.append(i**2)
print(angka)

# list comperhension
angka = [i**2 for i in range(1,8) if i%3 != 0]
print(angka)

# SOAL 3 
# Contoh output : 
# Jumlah kata ' Aku ' dalam kalimat ada 2
# Juamlah kata 'makan' dalam kalimat ada 3
# kalimat = 'Aku baru makan nasi terus aku mau makan mie nanti malam'
# kata = kalimat.title().split()
# unique = []

# for i in kata:
#     if i not in unique:
#         unique.append(i)

# for i in unique:
#     print(f"Jumlah kata '{i}' dalam kalimat ada {kata.count(i)}")



# SOAL 4

# print('''
#       Selamat Datang di Pasar Buah
#       List Menu :
#       1. Menampilkan Daftar Buah 
#       2. Menambah Buah
#       3. Menghapus Buah
#       4. Membeli Buah
#       5. Exit Program
#       ''')

# daftarBuah = [['Apel', 20, 10000], ['Jeruk', 15, 15000], ['Anggur', 25, 20000]]

# opsi = int(input("Masukan Opsi : "))
# if opsi == 1:
#     print('Index : Nama : Stock : Harga')
#     for i in enumerate(daftarBuah):
#         print(i)
