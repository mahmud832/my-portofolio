const darkModeBtn = document.getElementById("darkModeBtn");

// Cek apakah sebelumnya dark mode aktif
if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark-mode");
    darkModeBtn.textContent = "☀️";
}

// Saat tombol diklik
darkModeBtn.addEventListener("click", function () {

    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {
        darkModeBtn.textContent = "☀️";
        localStorage.setItem("theme", "dark");
    } else {
        darkModeBtn.textContent = "🌙";
        localStorage.setItem("theme", "light");
    }

});