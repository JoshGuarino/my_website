 const toggle_color = () => {
    let cur_color = get_cookie_value();
    if (cur_color === 'dark'){
        set_light();
        return;
    }
    set_dark();
    return;
}

const check_cookie = () => {
    let cur_color = get_cookie_value();
    if (cur_color === 'light'){
        set_light();
        return;
    }
    set_dark();
    return;
}

const set_cookie = (mode) =>{
    if (mode === 'dark'){
        document.cookie = 'color_mode=dark';
        return;
    }
    document.cookie = 'color_mode=light';
    return;    
}

const get_cookie_value = () => {
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

const set_light = () => {
    document.documentElement.style.setProperty('--dark', 'whitesmoke');
    document.documentElement.style.setProperty('--light', 'black');
    document.getElementById('color_mode').innerHTML = 'Light';
    set_cookie('light');
}

const set_dark = () => {
    document.documentElement.style.setProperty('--dark', 'black');
    document.documentElement.style.setProperty('--light', 'whitesmoke');
    document.getElementById('color_mode').innerHTML = 'Dark';
    set_cookie('dark');
}

check_cookie();