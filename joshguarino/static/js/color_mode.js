function toggle_color(){
    if (getComputedStyle(document.documentElement).getPropertyValue('--dark')==='black'){
        document.documentElement.style.setProperty('--dark', 'whitesmoke');
        document.documentElement.style.setProperty('--light', 'black');
        document.getElementById('color_mode').innerHTML = 'Light';
        return;
    }
    document.documentElement.style.setProperty('--dark', 'black');
    document.documentElement.style.setProperty('--light', 'whitesmoke');
    document.getElementById('color_mode').innerHTML = 'Dark';
    return;
}