# 🌟 SD Cendekia Ceria — Website Sekolah

Website profil sekolah dasar (SD) yang ceria, responsif, dan dibangun dengan **HTML, CSS, dan JavaScript murni** (tanpa framework) — cocok untuk portofolio maupun langsung dipakai sekolah sungguhan.

**[➡️ Lihat cara menjalankan / deploy di bawah](#-cara-menjalankan)**

## ✨ Fitur

- Desain modern & ceria, dibuat khusus untuk nuansa sekolah dasar
- Navigasi responsif (menu hamburger di HP)
- Section lengkap: Beranda, Tentang, Program & Ekstrakurikuler, Galeri, Prestasi & Testimoni, Berita, PPDB (langkah pendaftaran + formulir), Kontak + peta lokasi
- Formulir pendaftaran PPDB dengan validasi sederhana (siap dihubungkan ke backend/Formspree/Google Forms)
- Tombol "kembali ke atas", header yang menempel saat scroll
- Tanpa dependensi build tools — buka langsung di browser atau host di GitHub Pages
- Ramah aksesibilitas: skip-link, fokus terlihat, `prefers-reduced-motion` dihormati

## 📁 Struktur Proyek

```
sd-cendekia-ceria/
├── index.html      # Struktur halaman & konten
├── style.css        # Semua styling (desain, warna, layout, responsif)
├── script.js         # Interaksi (menu, form, scroll)
└── README.md
```

## 🚀 Cara Menjalankan

### 1. Coba di komputer sendiri
Cukup buka file `index.html` langsung di browser — tidak perlu instalasi apa pun.

### 2. Upload ke GitHub
```bash
git init
git add .
git commit -m "Website sekolah SD Cendekia Ceria"
git branch -M main
git remote add origin https://github.com/USERNAME/NAMA-REPO.git
git push -u origin main
```

### 3. Aktifkan GitHub Pages
1. Buka repo di GitHub → tab **Settings**
2. Klik menu **Pages** di sidebar kiri
3. Pada **Source**, pilih branch `main` dan folder `/ (root)`
4. Klik **Save**
5. Tunggu 1–2 menit, website akan aktif di:
   `https://USERNAME.github.io/NAMA-REPO/`

## 🎨 Cara Mengganti Isi (untuk sekolah Anda sendiri)

| Yang ingin diganti | Di file mana |
|---|---|
| Nama sekolah, logo, tagline | `index.html` — bagian `.brand` dan `<header>` |
| Teks hero / sambutan | `index.html` — bagian `<section class="hero">` |
| Visi, misi, keunggulan | `index.html` — bagian `id="tentang"` |
| Program & ekstrakurikuler | `index.html` — bagian `id="program"` |
| Foto kegiatan (galeri) | `index.html` — bagian `id="galeri"`, ganti `<div class="pin-thumb">...</div>` dengan `<img src="assets/nama-foto.jpg" alt="...">` |
| Prestasi & testimoni | `index.html` — bagian `id="prestasi"` |
| Berita sekolah | `index.html` — bagian `id="berita"` |
| Info & jadwal PPDB | `index.html` — bagian `id="ppdb"` |
| Alamat, telepon, email, peta | `index.html` — bagian `id="kontak"` (ganti parameter `q=` pada URL peta dengan alamat sekolah Anda) |
| Warna & tampilan | `style.css` — ubah nilai di `:root { ... }` bagian atas file |

### Menghubungkan formulir PPDB agar benar-benar mengirim data
Saat ini formulir di `script.js` hanya menampilkan pesan terima kasih (belum mengirim data ke mana pun). Untuk membuatnya berfungsi penuh, Anda bisa:
- Gunakan layanan gratis seperti [Formspree](https://formspree.io) atau [Google Forms](https://forms.google.com) (tempel action URL-nya ke tag `<form>`), atau
- Hubungkan ke backend/API sekolah Anda sendiri.

## 🖼️ Menambahkan Foto Asli
Folder `assets/` sudah disiapkan kosong. Simpan foto sekolah Anda di sana (contoh: `assets/upacara.jpg`), lalu ganti placeholder emoji di bagian Galeri dengan tag `<img>` yang mengarah ke foto tersebut.

## 📄 Lisensi
Bebas digunakan dan dimodifikasi untuk keperluan portofolio maupun website sekolah sungguhan.
