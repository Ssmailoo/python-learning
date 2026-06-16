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