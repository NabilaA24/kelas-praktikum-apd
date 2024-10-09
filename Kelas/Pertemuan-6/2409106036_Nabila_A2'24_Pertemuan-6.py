# daftar_buku = {}

# daftar_buku["Buku1"] = "Harry Potter"

# print(daftar_buku)

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#     }
# }

# print(Biodata["Social Media"]["Discord"])
# print(Biodata["KRS"][1])
# print(Biodata.get('KRS'))

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

#tanpa menggunakan items
# for i in Nilai:
#     print(i)

# print("")
#menggunakan items
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")
#untuk i dan j dapat diganti nama variabel lain, contoh i itu mapel dan j itu nilai

# print(Nilai)

# Nilai['sejarah'] = 100
#atau mau mengganti nilai yang ada bisa misal Nilai['Fisika'] = 100

# Nilai.update({'Biologi' : 80})

# del Nilai['Kimia']
# print(Nilai)

# simpan =Nilai.pop('Fisika')
# print(Nilai)
# print(simpan)

# print("Jumlah data = ", len(Nilai))

# Buku = {
#     "No Longer Human" : "Osamu Dazai",
#     "Harry Potter" : "J.K. Rowlings",
#     "Hamlet" : "William Shakespeare"
# }
# pinjam = Buku.copy()
# print("Dictionary yang Telah Disalin : ", pinjam)

# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #menggunakan keys
# for i in Nilai.keys():
#     print(i)

# print("")

# #menggunakan value
# for i in Nilai.values():
#     print(i)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

# Musik = {
#     "The Chainsmoker" : ["All we Know", "The Paris"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best of Me", "Memories"]
# }
# #i nya bis adi ubah j juga, dan song tu juga 
# for penyanyi, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }

# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
# print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# #Sebelum Dilakukan Perubahan
# print(mahasiswa)
# #Menambahkan Item pada Nested Dictionary
# mahasiswa[101]["Angkatan"] = 2023
# print(mahasiswa)

# #Mengubah Item pada Nested Dictionary
# mahasiswa[101]["Nama"] = "Rizal"
# print(mahasiswa)

# #Menghapus Item pada Nested Dictionary
# del mahasiswa[101]["Umur"]
# print(mahasiswa)

#Studi kasus 1

mahasiswa = {
904 : {"Nama" : "Ken", "Umur" : 16, "NIM" : 5, "Jurusan" : 'Informatika', "Angkatan" : 34}
}

#menambah
mahasiswa.update({"Hobi" : "Gym"})
print(mahasiswa)

#mengubah
mahasiswa["Nama"] = "Ken"
mahasiswa.update({'Nama' : "Bilqis"})
print(mahasiswa)

#menghapus
del mahasiswa[904]["Umur"]
print(mahasiswa)


#studi kasus
# Nilai = {
# "Matematika" : 90,
# "Fisika " : 80,
# "B. Inggris" : 80,
# "Kimia" : 70,

# }

# total = sum
