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




function updateDisplayData(){
    if( location.pathname == '/index.php' || location.pathname == '/'){
        AjaxRankData();
    }else if(location.pathname == '/status.php'){
        ajaxAccounts();
    }
    setTimeout("updateDisplayData()",3000);
}

function AjaxRankData(){
    $.ajax({
      url: "/ajaxRank.php",
      type: "GET",
      dataType: "json",
      success: function(data) {
        Accounts = data;
        updateIndexPage(Accounts);
      },
      
      error: function() {
        alert("ERROR!!!");
      }
    });
}


function updateIndexPage(data){
    $("#firstRankTeamID").text('第' + data[0]['teamID'] + '組');
    $('#secondRankTeamID').text('第' + data[1]['teamID'] + '組');
    $('#thirdRankTeamID').text('第' + data[2]['teamID'] + '組');

    $("#firstRankRatio").text(data[0]['Ratio'] + '%');
    $('#secondRankRatio').text(data[1]['Ratio'] + '%');
    $('#thirdRankRatio').text(data[2]['Ratio'] + '%');

    $('#table_body').text('');

    for(i = 0; i<data.length ; i++){
        if( data[i]['Ratio'] > 0){
            var displayClass = 'danger';
        }else if(data[i]['Ratio'] == 0){
            var displayClass = 'warning';
        }else{
            var displayClass = 'success';
        }
        var body_item = "";
        body_item += "<td>" + (i+1) +"</td>"; 
        body_item += "<td>" + data[i]['teamID'] +"</td>";
        body_item += "<td ><a href = " + stockUrl + data[i]['AccountIDs'] +">" + data[i]['Name'] +"</td>";

        body_item += "<td class = 'alert alert-" + displayClass +  " '>" + data[i]['Ratio'] + '%' +"</td>";
        var body_data = $("<tr></tr>").html(body_item); 
        $('#table_body').append(body_data);

    }
}


function ajaxAccounts(){
    $.ajax({
      url: "/ajaxAccounts.php",
      type: "GET",
      dataType: "json",
      success: function(data) {
        Accounts = data;
        updateStatusPage(Accounts);
      },
      
      error: function() {
        alert("ERROR!!!");
      }
    });
}

function updateStatusPage(data){

    $('#table_body').text('');
    for(i = 0; i<data.length ; i++){
        if( data[i]['Ratio'] > 0){
            var displayClass = 'danger';
        }else if(data[i]['Ratio'] == 0){
            var displayClass = 'warning';
        }else{
            var displayClass = 'success';
        }

        var body_item = "";
        body_item += "<td>" + data[i]['teamID'] +"</td>";
        body_item += "<td><a href = " + stockUrl + data[i]['AccountIDs'] +">" + data[i]['Name'] +"</td>";
        body_item += "<td class = 'alert alert-" + displayClass +  " '>" + data[i]['Ratio'] + '%' +"</td>";
        body_item += "<td>待下版本</td>";
        var body_data = $("<tr></tr>").html(body_item); 
        $('#table_body').append(body_data);

    }
}


Accounts = [];
var stockUrl = "https://www.cmoney.tw/vt/account-profile-info.aspx?account=";
update_time();
updateDisplayData();
