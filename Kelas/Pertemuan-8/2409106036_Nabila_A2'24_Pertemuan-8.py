#Error Handling dan file eksternal

# try :
#     angka = int(input("angka: "))
# except ValueError:
#     print("input tidak sesuai(wajib angka!)")
#     angka = int(input("angka: "))

# pilihan = int(input("pilihan: "))

# if pilihan == 1:
#     print("menu 1")

# elif pilihan == 2:
#     print("menu 2")

# else:
#     print("pilihan tidak ada")

# try:
#     angka = int(input("Masukkan angka: "))
# except ValueError:
#     print("Input yang anda masukkan bukan angka")
# else:
#     print(f"Angka yang kamu input: {angka}")
# finally:
#     print("Program selesai")

# try:
#     nama = input("Hello, what's your name? ")
#     if len(nama) > 5:
#         raise ValueError("Nama tidak boleh lebih dari 5ckarakter")

# except ValueError as e:
#     print(e)

def menu():
    print("""
        menu
        1.tambah
        2. Exit
        """)
def tambah(a,b):
    c= a+b
    print("hasil penjumlahan adalah:", {c})

while True:
    try: 
        menu()
        pilihan = (input("masukkan opsi menu: "))
        if pilihan == 1:
            a = int(input("masukkan angka pertama: "))
            b = int(input("masukkan angka kedua: "))
            tambah(a,b)
        if pilihan == 2:
            break
    except ValueError:
        print("opsi anda tidak ada dipilihan")
        ulang = input("apakah anda ingin kembali ke menu? {y/n}: ")
        if ulang == 'y':
            menu()
        else:
            break











