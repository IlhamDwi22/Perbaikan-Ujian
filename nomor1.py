# Membuat input nilai n
n = int(input("Masukkan angka n = "))

# Inisialisasi variabel total dan i
total = 0
i = 1

# Perulangan untuk menghitung jumlah
while i <= n:
    total += i
    i += 1

# Mencetak hasil program
print(f"Jumlah bilangan dari 1 hingga {n} = {total}")