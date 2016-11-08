//  時間更新   取id = now_time
var d = new Date();
var today;
var time;

function update_time(){
    d = new Date(); 
    today = get_today(d);
    time = get_time(d);
    $('#now_time').text(today + ' ' +  time);
    setTimeout("update_time()",1000);
}


function get_today(d){
    var day = d.getDate();
    var year =  d.getFullYear();
    var month = d.getMonth()+1; 
    return year + '/' + (month<10 ? '0' : '') + month + '/' + (day<10 ? '0' : '') + day;
}

function get_time(d){
    var hour = d.getHours();
    var minute = d.getMinutes();
    var second = d.getSeconds();
    return (hour<10 ? '0' : '') + hour + ':' + (minute<10 ? '0' : '') + minute + ':' + (second<10 ? '0' : '') + second;
}

