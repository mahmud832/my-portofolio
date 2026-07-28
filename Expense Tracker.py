expenses = []

while True:
    print("\n" + "=" * 40)
    print("        EXPENSE TRACKER")
    print("=" * 40)
    print("1. Tambah Pengeluaran")
    print("2. Lihat Pengeluaran")
    print("3. Total Pengeluaran")
    print("4. Hapus Pengeluaran")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Nama Pengeluaran : ")
        nominal = int(input("Nominal (Rp)     : "))

        expenses.append({
            "nama": nama,
            "nominal": nominal
        })

        print("✅ Pengeluaran berhasil ditambahkan.")

    elif pilihan == "2":
        if len(expenses) == 0:
            print("Belum ada data pengeluaran.")
        else:
            print("\n===== DAFTAR PENGELUARAN =====")

            for i, item in enumerate(expenses, start=1):
                print(f"{i}. {item['nama']} - Rp{item['nominal']:,}")

    elif pilihan == "3":
        total = 0

        for item in expenses:
            total += item["nominal"]

        print(f"\nTotal Pengeluaran : Rp{total:,}")

    elif pilihan == "4":
        if len(expenses) == 0:
            print("Belum ada data yang bisa dihapus.")
        else:
            print("\n===== DAFTAR PENGELUARAN =====")

            for i, item in enumerate(expenses, start=1):
                print(f"{i}. {item['nama']} - Rp{item['nominal']:,}")

            hapus = int(input("Masukkan nomor yang akan dihapus: "))

            if 1 <= hapus <= len(expenses):
                data = expenses.pop(hapus - 1)
                print(f"✅ {data['nama']} berhasil dihapus.")
            else:
                print("Nomor tidak valid.")

    elif pilihan == "5":
        print("Terima kasih telah menggunakan Expense Tracker.")
        break

    else:
        print("❌ Pilihan tidak valid.")