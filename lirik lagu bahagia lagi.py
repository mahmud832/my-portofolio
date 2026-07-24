import time

judul = "Bahagia Lagi"

lirik = [
    "Bila nanti kita berdua telah bahagia lagi",
    "Tiada lagi ruang tempat untuk",
    "Ku terlatih mengerti kala sedih temani",
    "Ku tak masalah asal kau di sini",
    "Dan mungkin kita berdua 'kan tertawa lagi",
    "Tangis air mata akan pergi",
    "Ini 'kan terlewati, tak ada yang sendiri",
    "Kupastikan kita bahagia lagi",
    "Kupastikan kita bahagia lagi"
]

print(f"🎵 {judul} 🎵\n")

for baris in lirik:
    print(baris)
    time.sleep(1.5)  # jeda 1,5 detik antar baris