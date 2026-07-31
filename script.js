/* ==========================
   BACK TO TOP BUTTON
========================== */

const topBtn = document.getElementById("topBtn");

window.onscroll = function () {

    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
        topBtn.style.display = "block";
    } else {
        topBtn.style.display = "none";
    }

};

topBtn.onclick = function () {

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

};


/* ==========================
   SCROLL ANIMATION
========================== */

const hiddenElements = document.querySelectorAll("section, .card, .feature, .testi-card");

hiddenElements.forEach((el) => {
    el.classList.add("hidden");
});

const observer = new IntersectionObserver((entries) => {

    entries.forEach((entry) => {

        if (entry.isIntersecting) {
            entry.target.classList.add("show");
        }

    });

}, {
    threshold: 0.2
});

hiddenElements.forEach((el) => observer.observe(el));


/* ==========================
   NAVBAR CHANGE COLOR
========================== */

const nav = document.querySelector("nav");

window.addEventListener("scroll", () => {

    if (window.scrollY > 80) {

        nav.style.background = "#2d2d2d";
        nav.style.padding = "15px 8%";

    } else {

        nav.style.background = "rgba(0,0,0,.7)";
        nav.style.padding = "20px 8%";

    }

});


/* ==========================
   ACTIVE MENU
========================== */

const sections = document.querySelectorAll("section");
const navLinks = document.querySelectorAll(".nav-links a");

window.addEventListener("scroll", () => {

    let current = "";

    sections.forEach((section) => {

        const sectionTop = section.offsetTop - 120;
        const sectionHeight = section.clientHeight;

        if (pageYOffset >= sectionTop) {
            current = section.getAttribute("id");
        }

    });

    navLinks.forEach((link) => {

        link.classList.remove("active");

        if (link.getAttribute("href") === "#" + current) {
            link.classList.add("active");
        }

    });

});


/* ==========================
   GALLERY HOVER EFFECT
========================== */

const images = document.querySelectorAll(".gallery img");

images.forEach((img) => {

    img.addEventListener("mouseover", () => {

        img.style.transform = "scale(1.08)";

    });

    img.addEventListener("mouseout", () => {

        img.style.transform = "scale(1)";

    });

});


/* ==========================
   BUTTON ANIMATION
========================== */

const buttons = document.querySelectorAll(".btn");

buttons.forEach((btn) => {

    btn.addEventListener("mouseenter", () => {

        btn.style.transform = "translateY(-5px)";

    });

    btn.addEventListener("mouseleave", () => {

        btn.style.transform = "translateY(0)";

    });

});


console.log("Cafe Mahmud Website Ready ☕");