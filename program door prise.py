import random
import time


def main():
    print("========================================")
    print("      PROGRAM UNDIAN ACAK DOORPRIZE     ")
    print("========================================")

    # Masukkan daftar nama peserta di sini
    peserta = ["mahmud", "rasty", "nadia", "Dedi", "Elsa", "Fahmi", "Gita", "Hendra"]

    print(f"Total peserta saat ini: {len(peserta)} orang.")
    print(f"Daftar nama: {', '.join(peserta)}")

    while len(peserta) > 0:
        pilihan = input(
            "\nTekan [Enter] untuk mengacak pemenang (atau ketik 'q' untuk keluar): "
        ).lower()

        if pilihan == "q":
            break

        print("\nMengocok nama...")
        time.sleep(1.5)  # Efek dramatis menunggu 1.5 detik

        # Memilih pemenang secara acak
        pemenang = random.choice(peserta)

        print("========================================")
        print(f"🎉 SELAMAT! Pemenang doorprize adalah: {pemenang} 🎉")
        print("========================================")

        # Hapus pemenang dari daftar agar tidak keluar lagi
        peserta.remove(pemenang)
        print(f"Sisa peserta yang belum menang: {len(peserta)} orang.")

    if len(peserta) == 0:
        print("\nSemua peserta sudah mendapatkan doorprize!")

    print("\nProgram undian selesai. Terima kasih!")


if __name__ == "__main__":
    main()
