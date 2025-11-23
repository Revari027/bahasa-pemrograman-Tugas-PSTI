# ------------------------------------
# KONSTANTA (Constants)
# ------------------------------------
MAX_DATA = 100   # Maksimal data

# ------------------------------------
# ARRAY/LIST untuk menyimpan data
# ------------------------------------
mahasiswa_list = []

# ------------------------------------
# SUBPROGRAM / FUNCTION
# ------------------------------------

# Menambah data mahasiswa
def tambah_mahasiswa():
    print("\n=== Tambah Data Mahasiswa ===")

    nama = input("Masukkan Nama Mahasiswa: ")
    jurusan = input("Masukkan Jurusan: ")
    matkul = input("Masukkan Mata Kuliah yang Diampu: ")
    ipk = float(input("Masukkan IPK (0.0 - 4.0): "))

    # Expression validasi
    if not (0.0 <= ipk <= 4.0):
        print("IPK tidak valid!")
        return

    # Menyimpan dalam bentuk dictionary (objek data)
    if len(mahasiswa_list) < MAX_DATA:
        data = {
            "nama": nama,
            "jurusan": jurusan,
            "matkul": matkul,
            "ipk": ipk
        }
        mahasiswa_list.append(data)
        print("Data berhasil disimpan!")
    else:
        print("Data sudah penuh!")


# Menampilkan seluruh data mahasiswa
def tampilkan_mahasiswa():
    print("\n=== Daftar Data Mahasiswa ===")

    if len(mahasiswa_list) == 0:
        print("Belum ada data yang tersimpan.")
        return
    
    for i, mhs in enumerate(mahasiswa_list):
        print(f"\nData ke-{i+1}")
        print(f"Nama      : {mhs['nama']}")
        print(f"Jurusan   : {mhs['jurusan']}")
        print(f"Mata Kuliah: {mhs['matkul']}")
        print(f"IPK       : {mhs['ipk']}")


# Menghitung rata-rata IPK
def rata_rata_ipk():
    print("\n=== Rata-rata IPK ===")
    if len(mahasiswa_list) == 0:
        print("Belum ada data IPK.")
        return
    
    # Expression perhitungan
    total = sum(mhs["ipk"] for mhs in mahasiswa_list)
    rata = total / len(mahasiswa_list)

    print(f"Rata-rata IPK dari semua mahasiswa: {rata:.2f}")


# ------------------------------------
# PROGRAM UTAMA
# ------------------------------------

def main():
    while True:
        print("\n===== MENU SISTEM DATA MAHASISWA =====")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Semua Data")
        print("3. Hitung Rata-Rata IPK")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tampilkan_mahasiswa()
        elif pilihan == "3":
            rata_rata_ipk()
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

# Jalankan program
main()
