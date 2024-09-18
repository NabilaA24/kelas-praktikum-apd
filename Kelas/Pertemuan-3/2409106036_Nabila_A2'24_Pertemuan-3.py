# print("""
# =======================
# Kalkulator Sederhana
# 1. +
# 2. -
# 3. *
# 4. /      
# =======================
# """)
# fitur = int(input("pilih fitur: "))
# match fitur :
#     case 1:
#         a = int(input("masukkann Angka 1 : "))
#         b = int(input("masukkan Angka 2 : "))
#         c = a + b 
#         print(f"hasil penjumlahan {c}" )

#     case 2:
#         a = int(input("masukkann Angka 1 : "))
#         b = int(input("masukkan Angka 2 : "))
#         c = a + b 
#         print(f"hasil penjumlahan {c}" )

#     case 3:
#         a = int(input("Masukkan angka 1 : "))
#         b = int(input("Masukkan angka 2 : "))
#         c = a * b 
#         print (f"hasil perkalian angka 1 dan angka 2 adalah {c}")

#     case 4:
#         a = int(input("Masukkan angka 1 : "))
#         b = int(input("Masukkan angka 2 : "))
#         c = a / b 
#         print (f"hasil pembagian angka 1 dan angka 2 adalah {c}")

#     case _: 
#         print("ga ada broww")


#studi kasus 2
# jenis_kelamin = input("Masukkan jenis kelamin anda (L/P) :")
# hasil = "Jenis Kelamin Laki-Laki" if jenis_kelamin == "L" else "Jenis Kelamin Perempuan" if jenis_kelamin == "P" else "Jenis Kelamin Tidak Diketahui"
# print(hasil)


# #Studi kasus 1
# buku = int(input("Masukkan jumlah buku = "))
# harga = int(input("Masukkan total harga buku = "))
# diskon = 0.20
# total_harga = buku * harga


# if buku >= 5 and total_harga > 100000:
#     totalee = total_harga * diskon
#     totale = total_harga - totalee
#     print(f"diskon yang diterima sebanyak {totalee:.0f}")
#     print(f"Anda harus membayar sebanyak {totale:.0f} setelah mendapat diskon 20%")
# else: print("anda tidak mendapat diskon")


nilai = int(input("masukkan nilai anda: "))
if nilai > 100 :
    print ("kondisi tak memenuhi")
elif nilai >= 80 :
    if nilai >= 90 and nilai <= 100 :
        print("Nilai anda A+" )
    if nilai >= 80 and nilai <= 89 :
        print("Nilai anda A-")

elif nilai >= 70 :
    if nilai >= 75 and nilai <= 79 :
        print("Nilai anda B+")
    if nilai >= 70 and nilai <= 74 : 
        print("Nilai anda B-")

else : 
    print("kondisi tidak memenuhi")




