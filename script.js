// ===== Tahun otomatis di footer =====
document.getElementById('year').textContent = new Date().getFullYear();

// ===== Menu mobile =====
const navToggle = document.getElementById('navToggle');
const mainNav = document.getElementById('mainNav');

navToggle.addEventListener('click', () => {
  const isOpen = mainNav.classList.toggle('open');
  navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
});

mainNav.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    mainNav.classList.remove('open');
    navToggle.setAttribute('aria-expanded', 'false');
  });
});

// ===== Tombol kembali ke atas =====
const backToTop = document.getElementById('backToTop');

window.addEventListener('scroll', () => {
  if (window.scrollY > 480) {
    backToTop.classList.add('visible');
  } else {
    backToTop.classList.remove('visible');
  }
});

backToTop.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

// ===== Formulir PPDB (contoh — belum terhubung ke server) =====
const ppdbForm = document.getElementById('ppdbForm');
const formNote = document.getElementById('formNote');

ppdbForm.addEventListener('submit', (e) => {
  e.preventDefault();

  if (!ppdbForm.checkValidity()) {
    formNote.textContent = 'Mohon lengkapi semua kolom yang wajib diisi.';
    formNote.style.color = 'var(--color-cherry)';
    return;
  }

  const nama = document.getElementById('namaAnak').value;
  formNote.textContent = `Terima kasih! Pendaftaran ${nama} sudah kami terima. Tim kami akan menghubungi Anda lewat WhatsApp/email dalam 1x24 jam.`;
  formNote.style.color = 'var(--color-sun)';
  ppdbForm.reset();

  // Catatan pengembang:
  // Form ini masih statis (belum tersambung ke backend/email).
  // Untuk membuatnya benar-benar mengirim data, hubungkan ke layanan
  // seperti Formspree, Google Forms, atau backend Anda sendiri.
});
