export default function header() {
    // 點擊右側bar伸縮按鈕
    const toggle = document.getElementById('toggle');  //右側bar伸縮按鈕
    const sec = document.getElementById('sec');        //section
    const nav = document.getElementById('navigation'); //右側bar
    toggle.onclick = function() {
        sec.classList.toggle('active');
        nav.classList.toggle('active');
    }

    // 換光暗
    const mode = document.getElementById('mode');
    try {  // 若有父頁面
        window.darklight = opener.darklight;  // 同步自身與父頁面光暗值
        if(opener.darklight == 'light') {     // 若進來的父頁面是光，就換一次畫面光暗
            mode.classList.toggle('darkLight');
            sec.classList.toggle('darkLight');
            nav.classList.toggle('darkLight');
        }
    } catch(e) {  // 第一次開啟
        console.log(e.message);
        window.darklight = 'dark';
    }
    mode.onclick = function() {
        if(window.darklight == 'light') {  // 換自身的光暗值
            window.darklight = 'dark';
        } else if(window.darklight == 'dark') {
            window.darklight = 'light';
        }
        // 換畫面光暗
        mode.classList.toggle('darkLight');
        sec.classList.toggle('darkLight');
        nav.classList.toggle('darkLight');
    }
}
// export default header;