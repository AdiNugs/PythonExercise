import math

# Adi Nugraha - JCDS 2602
# Tugas Day 2

# Soal 1
print("\n === JAWABAN SOAL 1 === \n")

x,y,z = 4,3,2

print((x+y*z/x*z)**2)

#================================================================

# # Soal 2
print("\n === JAWABAN SOAL 2 === \n")

k = int(input("Silahkan masukkan angka berapapun : "))

print(f"kuadrat dari {k} = ", k**2)

#================================================================

# Soal 3    
print("\n === JAWABAN SOAL 3 === \n")

hari = 485
tahun = hari // 360
bulan = (hari%360) // 30
sisa = (hari%360) % 30

print(f"{hari} hari")
print(f"{tahun} tahun {bulan} bulan {sisa} hari")

#================================================================

# Soal 4
print("\n === JAWABAN SOAL 4 === \n")

totalUsia = 49
# rasio =  4 / 10
andi = ((4 / 14) * totalUsia)  + 2
budi = ((10 / 14) * totalUsia) + 2

print("Usia Andi adalah", int(andi))
print("Usia Budi adalah", int(budi))

#=================================================================

# Soal 5
print("\n === JAWABAN SOAL 5 ===\n")

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

print("\n === Terima Kasih :) ===\n")

#========================TERIMA KASIH=============================