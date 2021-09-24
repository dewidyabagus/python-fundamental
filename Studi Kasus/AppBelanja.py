# Modul interaksi dengan sistem operasi
from os import system
from sys import platform
# Modul untuk menjeda jalannya aplikasi
from time import sleep
# Modul untuk pewarnaan cetakan
from colorama import Fore, Style

# variabel yang digunakan untuk menyimpan daftar belanjaan
# dalam bentu tipe data list
daftar = list()

# Daftar fungsi
def layarBersih():
    # Membersihkan layar command line dan dikembalikan
    # pengaturan semula
    print(Style.RESET_ALL)
    if (platform in ['linux', 'linux2']):
        system("clear")
    else:
        system("cls")

def cetakDaftar():
    # Menampilkan daftar belanjaan dalam daftar
    layarBersih()
    print("============ Daftar Belanjaan ============\n")
    if (len(daftar) > 0):
        for index in range(len(daftar)):
            print(Fore.GREEN + "%d. %s." % (index + 1, daftar[index]))
    else:
        print(Fore.GREEN + "Daftar belanjaan kosong")

    print(Style.RESET_ALL)

def masukanDaftar():
    # Menambahkan barang belanjaan ke daftar
    while True:
        cetakDaftar()
        pilih = input("Tambah item y / n kembali: ").strip()
        if (pilih == "y"):
            # Proses penambahan barang
            item = input("\nMasukan Nama Barang: ")
            if (item.strip()):
                daftar.append(item.strip())
            else:
                print(Fore.RED + "Upps!, Nama barang tidak boleh kosong")
                sleep(3) # berhenti 3 second
        elif (pilih == "n"):
            break

def lihatDaftar():
    # Menampilkan daftar belanjaan dan prompt untuk
    # kembali ke menu awal
    while True:
        cetakDaftar()
        # untuk kembali ke menu awal masukan q
        if (input("Masukan q untuk kembali: ").strip() == "q"):
            break

def hapusDaftar():
    # Menghapus barang pada daftar berdasarkan index 
    # yang di masukan pada prompt
    while True:
        cetakDaftar()
        # masukan index yang ingin dihapus
        pilih = input("Hapus item y / n kembali: ").strip()
        if (pilih == "y"):
            index = int(input("\nNo. urut barang yang dihapus: "))
            try:
                daftar.pop(index-1)
            except IndexError:
                print(Fore.RED + "Upps!, No. urut barang tidak diketemukan")
                sleep(3)
        elif (pilih == "n"):
            break

### PROGRAM UTAMA ###
while True:
    layarBersih()
    # menampilkan daftar menu
    print("============ Aplikasi Daftar Belanja ============\n")
    print("1. Masukan Daftar Belanja Baru.\n")
    print("2. Hapus Belanja Dari Daftar.\n")
    print("3. Lihat Daftar Belanja.\n")
    print("4. Keluar Aplikasi.\n")
    print("=================================================\n")
    
    closeProgram = False

    try:
        menu = int(input("Pilih Menu Sesuai Urutan: "))

        if (menu not in [1, 2, 3, 4]):
            raise ValueError()
        elif (menu == 1):
            masukanDaftar()
        elif (menu == 2):
            hapusDaftar()
        elif (menu == 3):
            lihatDaftar()
        else:
            closeProgram = True
    
    except ValueError:
        print(Fore.RED + "Upss!, kode menu tidak diketemukan.")
        sleep(3)

    except KeyboardInterrupt:
        layarBersih()
        closeProgram = True if \
            input("Apakah anda ingin mengakhiri program y / lainnya kembali menu utama: ").strip() == "y" \
                else False
    
    if (closeProgram):
        print("Good Bye !!!")
        sleep(5)
        break
