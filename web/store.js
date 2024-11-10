import header from "./header.js";
header();

// 點擊搜尋按鈕
const selButton = document.getElementById('selButton');
selButton.onclick = function() {
    console.log('button')
}

// 開啟子頁面
const home = document.getElementById('home');
home.onclick = function() {
    window.open('home.html');
}
const registration = document.getElementById('registration');
registration.onclick = function() {
    window.open('registration.html');
}
const consult = document.getElementById('consult');
consult.onclick = function() {
    window.open('consult.html');
}