import random

print("====================================")
print("  GAME BATU - GUNTING - KERTAS   ")
print("====================================")

# Pilihan yang tersedia dalam game
pilihan_game = ["batu", "gunting", "kertas"]

while True:
    print("\nPILIHANMU:")
    print("- batu")
    print("- gunting")
    print("- kertas")
    print("- keluar (untuk berhenti bermain)")
    
    # 1. Mengambil input dari pemain
    pilihan_pemain = input("Masukkan pilihanmu: ").lower() # .lower() supaya ketikan huruf besar/kecil tetap dibaca huruf kecil
    
    # Keluar dari game jika pemain mengetik 'keluar'
    if pilihan_pemain == "keluar":
        print("\n👋 Terima kasih sudah bermain! Sampai jumpa.")
        break
        
    # Memastikan input pemain sudah benar
    if pilihan_pemain not in pilihan_game:
        print("❌ Pilihan tidak valid! Pilih antara batu, gunting, atau kertas.")
        continue # Mengulang perulangan dari atas
        
    # 2. Komputer memilih secara acak dari list pilihan_game
    pilihan_komputer = random.choice(pilihan_game)
    
    print(f"\nKamu memilih     : {pilihan_pemain}")
    print(f"Komputer memilih : {pilihan_komputer}")
    print("------------------------------------")
    
    # 3. Logika menentukan pemenang
    if pilihan_pemain == pilihan_komputer:
        print("🤝 Hasilnya: SERI / SAMA KUAT!")
        
    elif pilihan_pemain == "batu":
        if pilihan_komputer == "gunting":
            print("🎉 KAMU MENANG! Batu menghancurkan gunting.")
        else:
            print("💀 KAMU KALAH! Kertas membungkus batu.")
            
    elif pilihan_pemain == "gunting":
        if pilihan_komputer == "kertas":
            print("🎉 KAMU MENANG! Gunting memotong kertas.")
        else:
            print("💀 KAMU KALAH! Batu menghancurkan gunting.")
            
    elif pilihan_pemain == "kertas":
        if pilihan_komputer == "batu":
            print("🎉 KAMU MENANG! Kertas membungkus batu.")
        else:
            print("💀 KAMU KALAH! Gunting memotong kertas.")