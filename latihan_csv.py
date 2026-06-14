import csv

data_belanja = [
    ["nama", "jumlah", "kategori"],
    ["ayam geprek", 20000, "makanan"],
    ["alpukat", 15000, "buah"],
    ["es teh", 10000, "minuman"]
]

with open("belanja.csv",mode='w') as file:
    writer = csv.writer(file)
    writer.writerows(data_belanja)


with open("belanja.csv", mode='r') as file:
    reader = csv.reader(file)
    for baris in reader:
        print(baris)


 