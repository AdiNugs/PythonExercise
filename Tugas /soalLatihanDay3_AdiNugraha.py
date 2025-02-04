import math

# Adi Nugraha - JCDS 2602
# Tugas Day 3

# ================== CONDITIONAL STATEMENT ======================

# SOAL 1

angka = int(input("Masukan angka : "))

if angka % 2 == 0:
    print(f"Angka {angka} tergolong bilangan GENAP")
else:
    print(f"Angka {angka} tergolong bilangan GANJIL")

# SOAL 2

massa = int(input("Masukan massa (kg) : "))
tinggi = int(input("Masukan tinggi (cm) : "))
imt = massa / (tinggi/100)**2

if imt < 18.5:
    print(f"{imt}, Berat badan kurang")
elif imt >= 18.5 and imt <= 24.9:
    print(f"{imt}, berat badan ideal")
elif imt >= 25 and imt <= 29.9:
    print(f"{imt}, berat badan ideal")
elif imt >= 30 and imt <= 39.9:
    print(f"{imt}, berat badan berlebih")
else:
    print(f"{imt}, obesitas")

# SOAL 3

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


print(f"Total : {total} \n")

bayar = int(input("Masukkan jumlah uang : "))

if bayar > total:
    kembalian = bayar - total
    print(f"Kembalian anda adalah {kembalian} \n")
    print("Terima kasih")
elif bayar < total:
    kurang = total - bayar
    print(f"Transaksi anda dibatalkan \n")
    print(f"Uang anda kurang sebesar {kurang}")
else:
    print("Terima kasih")

# ================== LOOPING STATEMENT ======================

# SOAL 1

# only show word with starting letter 'k'
kalimat = "Kamu harus menampilkan hanya kata yang berawalan huruf k pada kalimat ini"

kata = kalimat.split(" ")

print("Kata yang berawalan k adalah : \n")

for i in range(len(kata)):
    if kata[i].startswith("k") or kata[i].startswith("K"):
        print(kata[i])
        
print('\nTerima kasih :)')

# # SOAL 2

for item in range (1, 51):
    if item % 3 == 0:   
        print(item)

# SOAL 3

# tampilkan kata yang berjumlah genap

kalimat2 =  'Tampilkan kata yang memiliki jumlah karakter berjumlah genap pada kalimat ini'

kata2 = kalimat2.split(" ")

for i in range(len(kata2)):
    if len(kata2[i]) % 2 == 0:
        print(kata2[i])
    
# SOAL 4


for item in range (1, 101):
    if item % 3 == 0 and item % 5 != 0:   
        print(f"{item} kelipatan 3")
    elif item % 5 == 0 and item % 3 != 0:
        print(f"{item} kelipatan 5")
    elif item % 5 == 0 and item % 3 == 0:
       print(f"{item} kelipatan 3 & 5")
    else:
        print(item)

# SOAL 5

# List [12, 15, 1, 7, 4, 100] find highest number without using max() function

angka = [12, 15, 1, 7, 4, 100]

maks = 0 
for i in angka:
    if maks <= i:
        maks = i
print(maks)






