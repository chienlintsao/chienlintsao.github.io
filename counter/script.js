const r_counter = document.getElementById("r_counter");
const g_counter = document.getElementById("g_counter");
const b_counter = document.getElementById("b_counter");

let r_count = 0;
let g_count = 0;
let b_count = 0;

$("#r_increment-btn").click(function(){
    r_count++;
    r_counter.innerText = r_count;
});

$("#r_reduce-btn").click(function(){
    r_count--;
    r_counter.innerText = r_count;
});

$("#g_increment-btn").click(function(){
    g_count++;
    g_counter.innerText = g_count;
});

$("#g_reduce-btn").click(function(){
    g_count--;
    g_counter.innerText = g_count;
});

$("#b_increment-btn").click(function(){
    b_count++;
    b_counter.innerText = b_count;
});

$("#b_reduce-btn").click(function(){
    b_count--;
    b_counter.innerText = b_count;
});

$("#reset-btn").click(function(){
    r_count = 0;
    g_count = 0;
    b_count = 0;
    r_counter.innerText = r_count;
    g_counter.innerText = g_count;
    b_counter.innerText = b_count;
});