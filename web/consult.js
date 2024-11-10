import header from "./header.js";
header();

// 開啟子頁面
const home = document.getElementById('home');
home.onclick = function() {
    window.open('home.html');
}
const store = document.getElementById('store');
store.onclick = function() {
    window.open('store.html');
}
const consult = document.getElementById('consult');
consult.onclick = function() {
    window.open('consult.html');
}