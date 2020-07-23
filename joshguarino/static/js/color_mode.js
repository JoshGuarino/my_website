function toggle_color(){
    if (getComputedStyle(document.documentElement).getPropertyValue('--dark')==='whitesmoke'){
        document.documentElement.style.setProperty('--dark', 'black');
        document.documentElement.style.setProperty('--light', 'whitesmoke');
        return;
    }
    document.documentElement.style.setProperty('--dark', 'whitesmoke');
    document.documentElement.style.setProperty('--light', 'black');
    return;
}