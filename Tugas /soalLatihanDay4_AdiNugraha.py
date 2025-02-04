# Adi Nugraha - JCDS 2602
# Tugas Day 4

# ================== NESTED LOOP ======================

# SOAL 1

# Output
# 9 8 7 
# 6 5 4 
# 3 2 1

# start = 9

# for i in range(3):
#     for j in range(3):
#         print(start, end="  ")
#         start -= 1
#     print()                   # Cara ribet

# for i in range(9,0,-3):
#     for j in range(i, i-3, -1):
#         print(j, end="  ")
#     print()

# # SOAL 2
# # tiap angka di pangkat 2

# list_angka = [1,2,3,4,5,6,7,8,9,10]

# for item in list_angka:
#     if item % 3 == 0:
#         continue
#     print(item**2, end = " ")

# # SOAL 3

# print("\n")
# for i in range(5,0,-1):
#      for j in range(i,0,-1):
#          print("*", end = " ")
#      print() 

# # SOAL 4

# stokApel = 10
# stokJeruk = 5
# stokAnggur = 8


# apel = int(input("Masukkan jumlah apel : "))
# while apel > stokApel:
#     print("Stok apel tidak cukup")
#     apel = int(input("Masukkan jumlah apel : "))
#     continue
    
# jeruk = int(input("Masukkan jumlah jeruk : "))
# while jeruk > stokJeruk:
#     print("Stok jeruk tidak cukup")
#     jeruk = int(input("Masukkan jumlah jeruk : "))
#     continue 

# anggur = int(input("Masukkan jumlah anggur : "))
# while anggur > stokAnggur:
#     print("Stok anggur tidak cukup")
#     anggur = int(input("Masukkan jumlah anggur : "))
#     continue

# apelT = apel*10000
# jerukT = jeruk*15000
# anggurT = anggur*20000


# print("\nDetail Belanja\n")
# print(f"Apel : {apel} x 10000 = {apelT}")
# print(f"Jeruk : {jeruk} x 15000 = {jerukT}")
# print(f"Anggur : {anggur} x 20000 = {anggurT}\n")


# total = apelT + jerukT + anggurT


# print(f"Total : {total} \n")

# bayar = int(input("Masukkan jumlah uang : "))

# if bayar > total:
#     kembalian = bayar - total
#     print(f"Kembalian anda adalah {kembalian} \n")
#     print("Terima kasih")
# elif bayar < total:
#     kurang = total - bayar
#     print(f"Transaksi anda dibatalkan \n")
#     print(f"Uang anda kurang sebesar {kurang}")
# else:
#     print("Terima kasih")
    
# === TERIMA KASIH =======