import random

print("====================================")
print("       GAME TEBAK KATA RAHASIA      ")
print("====================================")

# 1. Daftar kata yang bisa dipilih acak oleh komputer
daftar_kata = ["python", "komputer", "kalkulator", "sublime", "program"]
kata_rahasia = random.choice(daftar_kata)

# Membuat list huruf yang berhasil ditebak (awalnya diisi garis bawah "_" sepanjang kata rahasia)
huruf_tertebak = ["_"] * len(kata_rahasia)
kesempatan = 6

print(f"Komputer sudah memilih satu kata misterius!")
print(f"Petunjuk kata: {' '.join(huruf_tertebak)}")
print(f"Kamu punya {kesempatan} kesempatan salah.\n")

# 2. Loop game berjalan selama kesempatan masih ada dan masih ada huruf yg belum ditebak
while kesempatan > 0 and "_" in huruf_tertebak:
    tebakan = input("Tebak 1 huruf: ").lower()
    print("------------------------------------")
    
    # Validasi agar pemain hanya memasukkan 1 huruf
    if len(tebakan) != 1 or not tebakan.isalpha():
        print("❌ Masukkan satu huruf saja ya!")
        continue
        
    # 3. Logika jika huruf tebakan ada di dalam kata rahasia
    if tebakan in kata_rahasia:
        print(f"🎯 Bagus! Huruf '{tebakan}' ada di dalam kata.")
        # Mengisi garis bawah dengan huruf yang benar
        for i in range(len(kata_rahasia)):
            if kata_rahasia[i] == tebakan:
                huruf_tertebak[i] = tebakan
    else:
        # Jika tebakan salah, kurangi kesempatan
        kesempatan -= 1
        print(f"❌ Salah! Huruf '{tebakan}' tidak ada di dalam kata.")
        print(f"Sisa kesempatanmu: {kesempatan}")
        
    # Menampilkan progress kata saat ini
    print(f"Kata saat ini: {' '.join(huruf_tertebak)}\n")

# 4. Menentukan akhir game (Menang/Kalah)
if "_" not in huruf_tertebak:
    print(f"🎉 SELAMAT! Kamu berhasil menebak kodenya! Katanya adalah: {kata_rahasia}")
else:
    print(f"👻 Game Over! Kesempatanmu habis. Kata yang benar adalah: {kata_rahasia}")