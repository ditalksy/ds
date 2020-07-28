import sys

def menuUtama():
    while True:
        print("""
        ### DAFTAR BELANJA ###

        Pilih nomor untuk tindakan yang anda ingin pilih:

        1. Baca daftar belanja
        2. Tambah barang
        3. Ubah barang
        4. Hapus barang
        5. Keluar
        6. Hapus daftar
        """)

        seleksi = input("Masukkan pilihan: ")

        #Baca daftar belanja
        if seleksi == "1":
            bacaDaftar()

        #Tambah barang
        elif seleksi == "2":
            tambahBarang()

        #Ubah daftar
        elif seleksi == "3":
            ubahBarang()
            

        #Hapus barang
        elif seleksi == "4":
            hapusBarang()

        #Keluar
        elif seleksi == "5":
            sys.exit()

        #Hapus daftar
        elif seleksi == "6":
            hapusDaftar()

        else:
            print ("Pilihan tidak valid.")

daftarBelanja = ["susu","roti","beras","air","mentega","tepung"]
def bacaDaftar():
    if len(daftarBelanja)==0:
        print("Daftar belanja kosong.")
    else:
        print()
        print("---DAFTAR BELANJA---")
        for i in daftarBelanja:
            print("* "+i)

def tambahBarang():
    barang = input("Masukkan nama barang untuk ditambah ke daftar belanja: ").lower()
    if barang in daftarBelanja:
        duplikat = input(f"{barang} sudah ada di daftar belanja. Apakah ingin menyimpan duplikat? Y/N: ")
        if duplikat == "y":
            daftarBelanja.append(barang)
            print(f"{barang} telah dimasukkan ke dalam daftar belanja.")
        elif duplikat == "n":
            print(f"{barang} tidak dimasukkan ke dalam daftar belanja.")
        else:
            print("Perintah salah. Kembali ke Menu Utama.")
    else:
        daftarBelanja.append(barang)
        print(f"{barang} telah dimasukkan ke dalam daftar belanja.")

def ubahBarang():
    daftarBelanjaBaru = []
    barangLama = input('Masukkan nama barang lama: ')
    barangBaru = input('Masukkan nama barang baru: ')
    for i in daftarBelanja:
        barangBaru=i.replace(barangLama,barangBaru)
        daftarBelanjaBaru.append(barangBaru)
        print(f"{barangLama} telah diganti menjadi {barangBaru}.")
    else:
        print(f"{barangLama} tidak terdaftar di daftar belanja.")
    
def hapusBarang():
    barang = input("Masukkan nama barang untuk dihapus dari daftar belanja: ").lower()
    for i in daftarBelanja:
        if (i==barang):
            daftarBelanja.remove(barang)
            print(f"{barang} telah dihapus dari dalam daftar belanja.")
        else:
            pass
    else:
        print(f"{barang} tidak terdaftar di daftar belanja.")

def hapusDaftar():
    daftarBelanja.clear()
    print("Daftar belanja telah dihapus. Daftar belanja kosong.")

#Untuk me-run Menu Utama
menuUtama()