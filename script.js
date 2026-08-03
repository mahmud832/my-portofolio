*{
margin:0;
padding:0;
box-sizing:border-box;
}

body{

font-family:Poppins,sans-serif;

background:#0f0f0f;

color:white;

}

nav{

display:flex;

justify-content:space-between;

align-items:center;

padding:20px 10%;

background:#111;

position:fixed;

width:100%;

top:0;

z-index:999;

}

.logo{

font-size:30px;

font-weight:700;

color:#ff3d3d;

}

nav ul{

display:flex;

list-style:none;

gap:35px;

}

nav a{

color:white;

text-decoration:none;

transition:.3s;

}

nav a:hover{

color:#ff3d3d;

}

.btn{

background:#ff3d3d;

padding:12px 25px;

border-radius:5px;

text-decoration:none;

color:white;

font-weight:600;

}

.hero{

height:100vh;

display:flex;

justify-content:center;

align-items:center;

text-align:center;

background:linear-gradient(rgba(0,0,0,.6),rgba(0,0,0,.6)),
url("https://images.unsplash.com/photo-1534438327276-14e5300c3a48?auto=format&fit=crop&w=1600&q=80");

background-size:cover;

background-position:center;

}

.hero h1{

font-size:65px;

margin-bottom:20px;

}

.hero p{

font-size:22px;

margin-bottom:30px;

}

.about{

padding:100px 10%;

}

.about h2{

font-size:40px;

margin-bottom:20px;

}

.programs{

padding:100px 10%;

text-align:center;

}

.cards{

display:grid;

grid-template-columns:repeat(auto-fit,minmax(250px,1fr));

gap:30px;

margin-top:50px;

}

.card{

background:#1d1d1d;

padding:40px;

border-radius:10px;

transition:.4s;

}

.card:hover{

transform:translateY(-10px);

background:#ff3d3d;

}

window.addEventListener("scroll", function () {
    const nav = document.querySelector("nav");

    if (window.scrollY > 50) {
        nav.style.background = "#000";
    } else {
        nav.style.background = "#111";
    }
});

// Letakkan di bawah sini
function calculateBMI() {

    let weight = document.getElementById("weight").value;
    let height = document.getElementById("height").value / 100;

    let bmi = weight / (height * height);

    let text = "";

    if (bmi < 18.5) {
        text = "Underweight";
    } else if (bmi < 25) {
        text = "Normal";
    } else if (bmi < 30) {
        text = "Overweight";
    } else {
        text = "Obesity";
    }

    document.getElementById("result").innerHTML =
        "BMI: " + bmi.toFixed(1) + " (" + text + ")";
}

function calculateBMI(){

let weight =
document.getElementById("weight").value;


let height =
document.getElementById("height").value / 100;


let bmi =
weight/(height*height);



let text="";


if(bmi < 18.5){

text="Underweight";

}

else if(bmi <25){

text="Normal";

}

else if(bmi <30){

text="Overweight";

}

else{

text="Obesitas";

}


document.getElementById("result").innerHTML =
"BMI : "+bmi.toFixed(1)+" ("+text+")";

}