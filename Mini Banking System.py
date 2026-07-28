saldo = 0
riwayat = []

while True:
    print("\n" + "=" * 45)
    print("         MINI BANKING SYSTEM")
    print("=" * 45)
    print("1. Cek Saldo")
    print("2. Setor Uang")
    print("3. Tarik Uang")
    print("4. Riwayat Transaksi")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        print(f"\nSaldo Anda : Rp{saldo:,}")

    elif pilihan == "2":
        setor = int(input("Masukkan jumlah setor: Rp"))

        if setor > 0:
            saldo += setor
            riwayat.append(f"Setor : Rp{setor:,}")
            print("✅ Setoran berhasil.")
        else:
            print("Jumlah tidak valid.")

    elif pilihan == "3":
        tarik = int(input("Masukkan jumlah penarikan: Rp"))

        if tarik <= saldo:
            saldo -= tarik
            riwayat.append(f"Tarik : Rp{tarik:,}")
            print("✅ Penarikan berhasil.")
        else:
            print("❌ Saldo tidak mencukupi.")

    elif pilihan == "4":
        print("\n===== RIWAYAT TRANSAKSI =====")

        if len(riwayat) == 0:
            print("Belum ada transaksi.")
        else:
            for i, transaksi in enumerate(riwayat, start=1):
                print(f"{i}. {transaksi}")

    elif pilihan == "5":
        print("Terima kasih telah menggunakan Mini Banking System.")
        break

    else:
        print("❌ Pilihan tidak valid.")