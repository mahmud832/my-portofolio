import os

file_name = "data.txt"

# Membuat file jika belum ada
if not os.path.exists(file_name):
    open(file_name, "w").close()

while True:
    print("\n" + "=" * 40)
    print("        CRUD FILE TXT")
    print("=" * 40)
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    # CREATE
    if pilihan == "1":
        data = input("Masukkan data: ")

        with open(file_name, "a") as file:
            file.write(data + "\n")

        print("✅ Data berhasil ditambahkan.")

    # READ
    elif pilihan == "2":
        with open(file_name, "r") as file:
            daftar = file.readlines()

        if len(daftar) == 0:
            print("Belum ada data.")
        else:
            print("\n===== DAFTAR DATA =====")

            for i, item in enumerate(daftar, start=1):
                print(f"{i}. {item.strip()}")

    # UPDATE
    elif pilihan == "3":
        with open(file_name, "r") as file:
            daftar = file.readlines()

        if len(daftar) == 0:
            print("Belum ada data.")
        else:
            print("\n===== DAFTAR DATA =====")

            for i, item in enumerate(daftar, start=1):
                print(f"{i}. {item.strip()}")

            nomor = int(input("Pilih nomor yang ingin diubah: "))
            data_baru = input("Masukkan data baru: ")

            if 1 <= nomor <= len(daftar):
                daftar[nomor - 1] = data_baru + "\n"

                with open(file_name, "w") as file:
                    file.writelines(daftar)

                print("✅ Data berhasil diperbarui.")
            else:
                print("Nomor tidak valid.")

    # DELETE
    elif pilihan == "4":
        with open(file_name, "r") as file:
            daftar = file.readlines()

        if len(daftar) == 0:
            print("Belum ada data.")
        else:
            print("\n===== DAFTAR DATA =====")

            for i, item in enumerate(daftar, start=1):
                print(f"{i}. {item.strip()}")

            nomor = int(input("Pilih nomor yang ingin dihapus: "))

            if 1 <= nomor <= len(daftar):
                del daftar[nomor - 1]

                with open(file_name, "w") as file:
                    file.writelines(daftar)

                print("✅ Data berhasil dihapus.")
            else:
                print("Nomor tidak valid.")

    elif pilihan == "5":
        print("Terima kasih telah menggunakan program.")
        break

    else:
        print("❌ Pilihan tidak valid.")