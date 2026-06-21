from datetime import datetime
import random as rn
import math

def hari_ini():
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year

    name_month = {
        1 : "januari",
        2 : "februari",
        3 : "maret",
        4 : "april",
        5 : "mei",
        6 : "Juni",
        7 : "juli",
        8 : "agustus",
        9 : "september",
        10 : "oktober",
        11 : "november",
        12 : "desember"
    }
    print(f"Hari ini: {day} {name_month[month]} {year}")

def jam_sekarang():
    hour = datetime.now().hour
    minute = datetime.now().minute

    print(f"Jam sekarang: {hour:02d}:{minute:02d}")

def angka_acak():
    for i in range(5):
        angka = rn.randint(1, 10)
        print(f"angka acaknya adalah: {angka}")

def angka_kuadrat():
    while True:
        try:
            hasil = int(input("Masukkan angka: "))
            break

        except ValueError:
            print("harap masukkan angka")
    angka = math.sqrt(hasil)
    print(f"Akar kuadrat: {angka:.2f}")

hari_ini()
jam_sekarang()
angka_acak()
angka_kuadrat()
