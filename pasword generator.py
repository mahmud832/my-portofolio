import random
import string

print("=" * 35)
print("🔐 PASSWORD GENERATOR")
print("=" * 35)

panjang = int(input("Masukkan panjang password: "))

karakter = (
    string.ascii_letters +   # Huruf besar & kecil
    string.digits +          # Angka
    string.punctuation       # Simbol
)

password = ""

for i in range(panjang):
    password += random.choice(karakter)

print("\nPassword berhasil dibuat!")
print("Password:", password)