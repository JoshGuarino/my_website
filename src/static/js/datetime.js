const getDateTime = (param) => {
    let date = new Date();
    let hour =  date.getHours();
    let min =  date.getMinutes();
    let sec = date.getSeconds();
    let session = "AM";
    let month = date.getMonth();
    let weekday = date.getDay();
    let day = date.getDate();
    let year = date.getFullYear();

    if(hour == 0){
        hour = 12;
    }
    
    if(hour > 12){
        hour = hour - 12;
        session = "PM";
    }
    
    hour = (hour < 10) ? "0" + hour : hour;
    min = (min < 10) ? "0" + min : min;
    sec = (sec < 10) ? "0" + sec : sec;

    switch(month){
        case 0:
        month = 'January';
        break;
        case 1:
        month = 'February';
        break;
        case 2:
        month = 'March';
        break;
        case 3:
        month = 'April';
        break;
        case 4:
        month = 'May';
        break;
        case 5:
        month = 'June';
        break;
        case 6:
        month = 'July';
        break;
        case 7:
        month = 'August';
        break;
        case 8:
        month = 'September';
        break;
        case 9:
        month = 'October';
        break;
        case 10:
        month = 'November';
        break;
        case 11:
        month = 'December';
        break;
    }

    switch(weekday){
        case 0:
        weekday = 'Sunday';
        break;
        case 1:
        weekday = 'Monday';
        break;
        case 2:
        weekday = 'Tuesday';
        break;
        case 3:
        weekday = 'Wednesday';
        break;
        case 4:
        weekday = 'Thursday';
        break;
        case 5:
        weekday = 'Friday';
        break;
        case 6:
        weekday = 'Saturday';
        break;
    }

    let copyright_elems = document.querySelectorAll('.copyright'); 
    copyright_elems.forEach(element => {
        element.innerHTML = `© 2019-${year} Josh Guarino`;
    });

    if(param ==="home"){
        document.getElementById('clock').innerHTML = `<h2 id="time">${hour}:${min}:${sec} ${session}<br>${weekday}, ${month} ${day}, ${year}</h2>`;
        document.getElementById('nav_clock').innerHTML = `${hour}:${min}:${sec} ${session}`;
        return;
    }
    document.getElementById('nav_clock').innerHTML = `${hour}:${min}:${sec} ${session}`;
    return;
};

const startClock = (param) => {
    getDateTime(param);
    setInterval(function(){ getDateTime(param); }, 1000);
};