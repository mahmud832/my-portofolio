import random

angka_rahasia = random.randint(1, 100)
percobaan = 0

print("=" * 35)
print("🎯 SELAMAT DATANG DI GAME TEBAK ANGKA")
print("=" * 35)
print("Saya telah memilih angka dari 1 - 100.")
print("Coba tebak angkanya!\n")

while True:
    tebakan = int(input("Masukkan tebakanmu: "))
    percobaan += 1

    if tebakan < angka_rahasia:
        print("⬆️ Terlalu kecil!\n")

    elif tebakan > angka_rahasia:
        print("⬇️ Terlalu besar!\n")

    else:
        print("\n🎉 Selamat!")
        print(f"Angka yang benar adalah {angka_rahasia}.")
        print(f"Kamu berhasil menebak dalam {percobaan} percobaan.")
        break