from datetime import datetime

print("=" * 45)
print("         KASIR SEDERHANA")
print("=" * 45)

tanggal = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

jumlah_barang = int(input("Masukkan jumlah jenis barang: "))

daftar_barang = []
total_belanja = 0

for i in range(jumlah_barang):
    print(f"\nBarang ke-{i+1}")

    nama = input("Nama Barang  : ")
    harga = int(input("Harga Barang : Rp"))
    jumlah = int(input("Jumlah Beli  : "))

    subtotal = harga * jumlah
    total_belanja += subtotal

    daftar_barang.append({
        "nama": nama,
        "harga": harga,
        "jumlah": jumlah,
        "subtotal": subtotal
    })

if total_belanja >= 100000:
    diskon = total_belanja * 0.10
else:
    diskon = 0

total_bayar = total_belanja - diskon

print("\n")
print("=" * 45)
print("              STRUK BELANJA")
print("=" * 45)
print("Tanggal :", tanggal)
print("-" * 45)

for barang in daftar_barang:
    print(f"{barang['nama']}")
    print(f"  Rp{barang['harga']:,} x {barang['jumlah']} = Rp{barang['subtotal']:,}")

print("-" * 45)
print(f"Total Belanja : Rp{total_belanja:,.0f}")
print(f"Diskon        : Rp{diskon:,.0f}")
print(f"Total Bayar   : Rp{total_bayar:,.0f}")

while True:
    uang = int(input("\nUang Pembeli : Rp"))

    if uang >= total_bayar:
        break
    else:
        print("Uang tidak cukup! Silakan masukkan lagi.")

kembalian = uang - total_bayar

print("-" * 45)
print(f"Uang Pembeli : Rp{uang:,.0f}")
print(f"Kembalian    : Rp{kembalian:,.0f}")
print("=" * 45)
print("     Terima Kasih Telah Berbelanja")
print("=" * 45)