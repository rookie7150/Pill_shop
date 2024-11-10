import header from "./header.js";
header();

// 開啟子頁面
const store = document.getElementById('store');
store.onclick = function() {
    window.open('store.html');
}
const registration = document.getElementById('registration');
registration.onclick = function() {
    window.open('registration.html');
}
const consult = document.getElementById('consult');
consult.onclick = function() {
    window.open('consult.html');
}