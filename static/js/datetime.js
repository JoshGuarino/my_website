function getDateTime(){
    var date = new Date();
    var hour =  date.getHours();
    var min =  date.getMinutes();
    var sec = date.getSeconds();
    var session = "AM";
    var month = date.getMonth()
    var weekday = date.getDay();
    var day = date.getDate();
    var year = date.getFullYear();

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

    document.getElementById('clock').innerHTML = '<h2 id="time">' + hour + ':' + min + ':' + sec + ' ' + session + '<br>' + weekday + ', ' + month + ' ' + day + ', ' + year +'</h2>';
}

function startClock(){
    getDateTime();
    setInterval(function(){ getDateTime(); }, 1000);
}