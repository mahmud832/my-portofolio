mahasiswa = []

while True:
    print("\n" + "=" * 45)
    print("      SISTEM NILAI MAHASISWA")
    print("=" * 45)
    print("1. Tambah Data Mahasiswa")
    print("2. Lihat Semua Data")
    print("3. Cari Mahasiswa")
    print("4. Hapus Data Mahasiswa")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Nama Mahasiswa : ")

        tugas = float(input("Nilai Tugas : "))
        uts = float(input("Nilai UTS   : "))
        uas = float(input("Nilai UAS   : "))

        rata = (tugas + uts + uas) / 3

        if rata >= 85:
            grade = "A"
        elif rata >= 70:
            grade = "B"
        elif rata >= 60:
            grade = "C"
        elif rata >= 50:
            grade = "D"
        else:
            grade = "E"

        if rata >= 60:
            status = "LULUS"
        else:
            status = "TIDAK LULUS"

        mahasiswa.append({
            "nama": nama,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "rata": rata,
            "grade": grade,
            "status": status
        })

        print("✅ Data berhasil ditambahkan.")

    elif pilihan == "2":

        if len(mahasiswa) == 0:
            print("Belum ada data mahasiswa.")
        else:
            print("\n===== DAFTAR NILAI MAHASISWA =====")

            for i, data in enumerate(mahasiswa, start=1):
                print("-" * 40)
                print(f"Data ke-{i}")
                print(f"Nama   : {data['nama']}")
                print(f"Tugas  : {data['tugas']}")
                print(f"UTS    : {data['uts']}")
                print(f"UAS    : {data['uas']}")
                print(f"Rata   : {data['rata']:.2f}")
                print(f"Grade  : {data['grade']}")
                print(f"Status : {data['status']}")

    elif pilihan == "3":
        cari = input("Masukkan nama mahasiswa: ")

        ditemukan = False

        for data in mahasiswa:
            if data["nama"].lower() == cari.lower():
                print("\nData ditemukan")
                print(f"Nama   : {data['nama']}")
                print(f"Rata   : {data['rata']:.2f}")
                print(f"Grade  : {data['grade']}")
                print(f"Status : {data['status']}")
                ditemukan = True
                break

        if not ditemukan:
            print("❌ Mahasiswa tidak ditemukan.")

    elif pilihan == "4":

        if len(mahasiswa) == 0:
            print("Belum ada data.")
        else:
            for i, data in enumerate(mahasiswa, start=1):
                print(f"{i}. {data['nama']}")

            hapus = int(input("Nomor yang akan dihapus: "))

            if 1 <= hapus <= len(mahasiswa):
                data = mahasiswa.pop(hapus - 1)
                print(f"✅ Data {data['nama']} berhasil dihapus.")
            else:
                print("Nomor tidak valid.")

    elif pilihan == "5":
        print("Terima kasih telah menggunakan program.")
        break

    else:
        print("❌ Pilihan tidak valid.")