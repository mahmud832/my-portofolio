print("=== Kalkulator Sederhana ===")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

print("\nPilih operasi:")
print("1. +")
print("2. -")
print("3. *")
print("4. /")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

if pilihan == "1":
    print("Hasil =", angka1 + angka2)
elif pilihan == "2":
    print("Hasil =", angka1 - angka2)
elif pilihan == "3":
    print("Hasil =", angka1 * angka2)
elif pilihan == "4":
    if angka2 != 0:
        print("Hasil =", angka1 / angka2)
    else:
        print("Error: Tidak bisa dibagi dengan nol!")
else:
    print("Pilihan tidak valid.")