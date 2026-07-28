inventory = {}

while True:
    print("\n" + "=" * 40)
    print("      INVENTORY BARANG")
    print("=" * 40)
    print("1. Tambah Barang")
    print("2. Lihat Semua Barang")
    print("3. Cari Barang")
    print("4. Update Stok")
    print("5. Hapus Barang")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        nama = input("Nama Barang : ")
        stok = int(input("Jumlah Stok : "))
        harga = int(input("Harga Barang : Rp"))

        inventory[nama] = {
            "stok": stok,
            "harga": harga
        }

        print("✅ Barang berhasil ditambahkan.")

    elif pilihan == "2":

        if len(inventory) == 0:
            print("Belum ada data barang.")
        else:
            print("\n===== DAFTAR BARANG =====")

            for nama, data in inventory.items():
                print(f"Nama  : {nama}")
                print(f"Stok  : {data['stok']}")
                print(f"Harga : Rp{data['harga']:,}")
                print("-" * 30)

    elif pilihan == "3":
        cari = input("Masukkan nama barang : ")

        if cari in inventory:
            print("\nBarang ditemukan")
            print("Nama  :", cari)
            print("Stok  :", inventory[cari]["stok"])
            print("Harga : Rp{:,.0f}".format(inventory[cari]["harga"]))
        else:
            print("❌ Barang tidak ditemukan.")

    elif pilihan == "4":
        nama = input("Nama Barang : ")

        if nama in inventory:
            stok_baru = int(input("Stok Baru : "))
            inventory[nama]["stok"] = stok_baru
            print("✅ Stok berhasil diperbarui.")
        else:
            print("❌ Barang tidak ditemukan.")

    elif pilihan == "5":
        nama = input("Nama Barang yang dihapus : ")

        if nama in inventory:
            del inventory[nama]
            print("✅ Barang berhasil dihapus.")
        else:
            print("❌ Barang tidak ditemukan.")

    elif pilihan == "6":
        print("Terima kasih telah menggunakan Inventory Barang.")
        break

    else:
        print("❌ Pilihan tidak valid.")