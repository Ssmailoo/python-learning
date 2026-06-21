# kalkulator BMI sederhana
'''def hitung_bmi(berat_kg, tinggi_m):
    bmi = berat_kg / (tinggi_m ** 2)
    return round(bmi, 2) 

berat = float(input("Berat (kg): "))
tinggi = float(input("Tinggi (m): "))

hasil hitung_bmi(berat, tinggi)
print(f"BMI anda: {hasil}")

if hasil < 18.5:
    print("Kategori : underweight")
elif hasil < 25:
    print("Kategori : normal")
elif hasil < 30:
    print("Kategori : Overweight")
else:
    print("Kategori : Obese") '''

import csv
import os
from datetime import datetime

NAMA_BULAN = {
    1:"Januari",
    2:"Februari",
    3:"Maret",
    4:"April",
    5:"Mei",
    6:"Juni",
    7:"Juli",
    8:"Agustus",
    9:"September",
    10:"Oktober",
    11:"November",
    12:"Desember"
}
pengeluaran = []

def expense():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Tambah Pengeluaran")
        print("2. Lihat Pengeluaran")
        print("3. Total per Kategori")
        print("4. Keluar")
        print("5. Bantuan")

        while True:
            try:
                hasil = int(input("Pilih menu: "))
                break
            except ValueError:
                print("Harap untuk memasukkan angka")


        if hasil == 1:
            tambah_pengeluaran()

        elif hasil == 2:
            lihat_pengeluaran()

        elif hasil == 3:
            total_per_kategori()

        elif hasil == 4:
            print("Keluar dari Program")
            break

        elif hasil == 5:
            print("""
            ===== EXPENSE TRACKER =====
            1. Tambah Pengeluaran
            → Menambahkan data pengeluaran baru.
            → Masukkan nama, jumlah, dan kategori.
            2. Lihat Pengeluaran
            → Menampilkan semua pengeluaran yang telah disimpan.

            3. Total per Kategori
            → Menampilkan total pengeluaran untuk setiap kategori.

            4. Keluar
            → Menyimpan data dan menutup aplikasi.

            Catatan:
            - Data akan disimpan ke file "expenses.csv".
            - Saat aplikasi dibuka kembali, data lama akan dimuat otomatis dari file CSV.""")


        else:
            print("Pilihan tidak valid")

def tambah_pengeluaran():
    while True:
        nama = input("masukkan nama: ")
        if nama == "":
            print("Nama tidak boleh kosong")
        else:
            break
    while True:
        try:
            jumlah = int(input("Masukkan jumlah: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0")
            else:
                break
        except ValueError:
            print("Masukkan Angka")
    kategori = input("masukkan kategori: ")

    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    tanggal = (f"{day} {NAMA_BULAN[month]} {year}")

    data = {
        "nama": nama,
        "jumlah": jumlah,
        "kategori": kategori,
        "tanggal": tanggal
    }

    pengeluaran.append(data)
    simpan_ke_csv()

def lihat_pengeluaran():
    if not pengeluaran:
        print("Belum ada pengeluaran")

    else:
        for i in pengeluaran:
            print(f"Nama: {i['nama']}, Jumlah: {i['jumlah']}, Kategori: {i['kategori']}, Tanggal: {i['tanggal']}")

def total_per_kategori():
    total = {}
    for item in pengeluaran:
        kategori = item["kategori"]
        jumlah = item["jumlah"]

        if kategori in total:
            total[kategori] = total[kategori] + jumlah

        else:
            total[kategori] = jumlah
    for kategori, jumlah in total.items():
        print(f"Kategori: {kategori}, Jumlah: {jumlah}")
def simpan_ke_csv():
    with open("projects/expense-tracker/data/expenses.csv", mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=["nama", "jumlah", "kategori", "tanggal"])
        writer.writeheader()
        writer.writerows(pengeluaran)
def muat_dari_csv():
    if os.path.exists("projects/expense-tracker/data/expenses.csv"):
        with open("projects/expense-tracker/data/expenses.csv", mode='r') as file:
            reader = csv.DictReader(file)
            for baris in reader:
                baris["jumlah"] = int(baris["jumlah"])
                pengeluaran.append(baris)
if __name__ == "__main__":
    muat_dari_csv()
    expense()