// Smooth Scroll
document.querySelectorAll("nav a").forEach(link => {
    link.addEventListener("click", function(e){
        e.preventDefault();

        const tujuan = document.querySelector(this.getAttribute("href"));

        tujuan.scrollIntoView({
            behavior: "smooth"
        });
    });
});