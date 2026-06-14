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

def expanse():
    while True:
        print("\n=== Expanse Tracker ===")
        print("1. Tambah Pengeluaran")
        print("2. Lihat Pengeluaran")
        print("3. Total per Kategori")
        print("4. Keluar")
        print("5. Bantuan")

        hasil = int(input("Pilih menu: "))

        if hasil == 1:
            print("Tambah Pengeluaran")

        elif hasil == 2:
            print("Lihat Pengeluaran")

        elif hasil == 3:
            print("Total per Kategori")

        elif hasil == 4:
            print("Keluar dari Program")
            break

        elif hasil == 5:
            print("Panduan penggunaan Expanse Tracker")

        else:
            print("Pilihan tidak valid")

expanse()

 ''' pengeluaran = []

kategori = input("Masukkan kategori: ")
jumlah =int(input("Masukan jumlah"))

print("kategori:", kategori)
print("jumalah", jumlah)

pengeluaran.append(data)

print(pengeluaran) '''

