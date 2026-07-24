print("====================================")
print("     APLIKASI TO-DO LIST SEDERHANA  ")
print("====================================")

# Tempat menyimpan daftar kegiatan (awalnya kosong)
daftar_kegiatan = []

while True:
    # 1. Menampilkan Menu Utama
    print("\nMENU APLIKASI:")
    print("1. Lihat Daftar Kegiatan")
    print("2. Tambah Kegiatan Baru")
    print("3. Hapus Kegiatan")
    print("4. Keluar")
    
    # Mengambil pilihan menu dari pengguna
    pilihan = input("Pilih menu (1/2/3/4): ")
    print("------------------------------------")
    
    # 2. Logika Menu 1: Melihat Daftar Kegiatan
    if pilihan == "1":
        if len(daftar_kegiatan) == 0:
            print("📭 Daftar kegiatanmu masih kosong!")
        else:
            print("📝 DAFTAR KEGIATANMU:")
            # Menggunakan enumerate agar muncul nomor urut (1, 2, 3, dst)
            for nomor, kegiatan in enumerate(daftar_kegiatan, 1):
                print(f"{nomor}. {kegiatan}")
                
    # 3. Logika Menu 2: Menambah Kegiatan
    elif pilihan == "2":
        kegiatan_baru = input("Masukkan kegiatan baru: ")
        daftar_kegiatan.append(kegiatan_baru) # .append() berfungsi menambah data ke dalam list
        print(f"✅ '{kegiatan_baru}' berhasil ditambahkan!")
        
    # 4. Logika Menu 3: Menghapus Kegiatan
    elif pilihan == "3":
        if len(daftar_kegiatan) == 0:
            print("❌ Tidak ada kegiatan yang bisa dihapus.")
        else:
            print("📝 PILIH NOMOR YANG INGIN DIHAPUS:")
            for nomor, kegiatan in enumerate(daftar_kegiatan, 1):
                print(f"{nomor}. {kegiatan}")
                
            nomor_hapus = int(input("\nMasukkan nomor kegiatan yang sudah selesai: "))
            
            # Memastikan nomor yang dimasukkan ada di dalam daftar
            if 0 < nomor_hapus <= len(daftar_kegiatan):
                # .pop() berfungsi menghapus data berdasarkan indeksnya (indeks dimulai dari 0, makanya dikurang 1)
                kegiatan_dihapus = daftar_kegiatan.pop(nomor_hapus - 1)
                print(f"🗑️ '{kegiatan_dihapus}' telah dihapus dari daftar!")
            else:
                print("❌ Nomor tidak valid!")
                
    # 5. Logika Menu 4: Keluar dari Aplikasi
    elif pilihan == "4":
        print("👋 Terima kasih sudah menggunakan aplikasi To-Do List! Sampai jumpa.")
        break # Menghentikan perulangan while True
        
    else:
        print("❌ Pilihan tidak tersedia, silakan masukkan angka 1 sampai 4.")