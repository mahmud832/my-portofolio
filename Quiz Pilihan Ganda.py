soal = [
    {
        "pertanyaan": "1. Siapa pencipta bahasa Python?",
        "pilihan": {
            "A": "Guido van Rossum",
            "B": "James Gosling",
            "C": "Dennis Ritchie",
            "D": "Bjarne Stroustrup"
        },
        "jawaban": "A"
    },
    {
        "pertanyaan": "2. Python pertama kali dirilis pada tahun?",
        "pilihan": {
            "A": "1985",
            "B": "1991",
            "C": "2000",
            "D": "1998"
        },
        "jawaban": "B"
    },
    {
        "pertanyaan": "3. Fungsi untuk menampilkan output di Python adalah?",
        "pilihan": {
            "A": "echo()",
            "B": "printf()",
            "C": "print()",
            "D": "output()"
        },
        "jawaban": "C"
    },
    {
        "pertanyaan": "4. Tipe data untuk menyimpan banyak nilai adalah?",
        "pilihan": {
            "A": "list",
            "B": "int",
            "C": "float",
            "D": "bool"
        },
        "jawaban": "A"
    },
    {
        "pertanyaan": "5. Simbol komentar satu baris di Python adalah?",
        "pilihan": {
            "A": "//",
            "B": "/* */",
            "C": "#",
            "D": "--"
        },
        "jawaban": "C"
    }
]

skor = 0

print("=" * 45)
print("        QUIZ PILIHAN GANDA")
print("=" * 45)

for nomor, data in enumerate(soal, start=1):
    print("\n" + data["pertanyaan"])

    for huruf, pilihan in data["pilihan"].items():
        print(f"{huruf}. {pilihan}")

    jawaban = input("Jawaban Anda (A/B/C/D): ").upper()

    if jawaban == data["jawaban"]:
        print("✅ Jawaban Benar!")
        skor += 20
    else:
        print(f"❌ Jawaban Salah! Jawaban yang benar adalah {data['jawaban']}.")

print("\n" + "=" * 45)
print("             HASIL QUIZ")
print("=" * 45)
print(f"Skor Anda : {skor}/100")

if skor == 100:
    print("🏆 Luar biasa! Nilai sempurna.")
elif skor >= 80:
    print("🥇 Sangat Baik!")
elif skor >= 60:
    print("👍 Baik.")
else:
    print("📚 Tetap semangat belajar!")