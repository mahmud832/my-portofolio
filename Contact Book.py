contacts = {}

while True:
    print("\n" + "=" * 35)
    print("📒 CONTACT BOOK")
    print("=" * 35)
    print("1. Tambah Kontak")
    print("2. Lihat Semua Kontak")
    print("3. Cari Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Nama: ")
        nomor = input("Nomor HP: ")

        contacts[nama] = nomor

        print("✅ Kontak berhasil ditambahkan!")

    elif pilihan == "2":

        if len(contacts) == 0:
            print("Belum ada kontak.")
        else:
            print("\n===== DAFTAR KONTAK =====")

            for nama, nomor in contacts.items():
                print(f"Nama : {nama}")
                print(f"Nomor: {nomor}")
                print("-" * 25)

    elif pilihan == "3":
        cari = input("Masukkan nama kontak: ")

        if cari in contacts:
            print("\nKontak ditemukan")
            print("Nama  :", cari)
            print("Nomor :", contacts[cari])
        else:
            print("❌ Kontak tidak ditemukan.")

    elif pilihan == "4":
        hapus = input("Nama yang ingin dihapus: ")

        if hapus in contacts:
            del contacts[hapus]
            print("✅ Kontak berhasil dihapus.")
        else:
            print("❌ Kontak tidak ditemukan.")

    elif pilihan == "5":
        print("Terima kasih telah menggunakan Contact Book.")
        break

    else:
        print("Pilihan tidak valid!")