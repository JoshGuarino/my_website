function toggle_color(){
    let cur_color = get_cookie_value();
    if (cur_color === 'dark'){
        set_light();
        return;
    }
    set_dark();
    return;
}

function check_cookie(){
    let cur_color = get_cookie_value(); console.log(cur_color);
    if (cur_color === 'light'){
        set_light();
        return;
    }
    set_dark();
    return;
}

function set_cookie(mode){
    if (mode === 'dark'){
        document.cookie = 'color_mode=dark';
        return;
    }
    document.cookie = 'color_mode=light';
    return;    
}

function get_cookie_value(){
    let cookie_arr = document.cookie.split(';');
    let color_value = '';
    cookie_arr.forEach(cookie => {
        let cur_cookie = cookie.split('=');
        if (cur_cookie[0] === 'color_mode'){
            color_value = cur_cookie[1];
        }
    });
    return color_value;
} 

function set_light(){
    document.documentElement.style.setProperty('--dark', 'whitesmoke');
    document.documentElement.style.setProperty('--light', 'black');
    document.getElementById('color_mode').innerHTML = 'Light';
    set_cookie('light');
}

function set_dark(){
    document.documentElement.style.setProperty('--dark', 'black');
    document.documentElement.style.setProperty('--light', 'whitesmoke');
    document.getElementById('color_mode').innerHTML = 'Dark';
    set_cookie('dark');
}