 <?php

$dbhost = 'localhost'; #sql304.byethost5.com
$dbname = 'stockcompetition';#b5_19130911_stockcompetation
$dbuser = 'root';#b5_19130911
$dbpwd = 'root';#a4z$m^4x6t

$conn = new PDO('mysql:host='.$dbhost.';dbname='.$dbname.';port=3306',$dbuser,$dbpwd);
$conn->exec('set names utf8');
$data = $conn->query(" 
  SELECT teams.*,group_concat(Accounts.AccountID separator ',')  as AccountIDs
  FROM teams
  INNER JOIN Accounts on Accounts.teamID = teams.teamID
  GROUP BY teams.teamID
  ");

  $Accounts = $data->fetchAll();
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="5;URL=status.php">"
    <title>StockCompetation</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="css/dashboard.css" rel="stylesheet">
    <script src="js/jquery-3.1.0.min.js"></script>

  </head>

  <body onload= "update_time()" >


    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">模擬投資競賽</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav navbar-right">
            <li><a href=""></a></li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-3 col-md-2 sidebar">
          <ul class="nav nav-sidebar">
            <li><a href="index.php">排名狀況</a></li>
            <li class="active"><a href="status.php">各組概況</a></li>
            <li><a href="#"></a></li>
            <li><a href="#"></a></li>
          </ul>
        </div>
        <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
          <h2 class="sub-header"　id="check_result">投資狀況</h2>
          <div class="table-responsive">
            <table class="table table-striped">
              <thead id="table_head">
                <tr>
                  <td>組別</td>
                  <td>隊伍名稱</td>
                  <td>投資報酬率</td>
                  <td>購買證券</td>
                </tr>
              </thead>
              <tbody id="table_body">
                <?php
                  foreach($Accounts as $Account){
                    $Ratio = number_format($Account['Ratio'],2);
                    echo "<tr>";
                      echo "<td>".$Account['teamID']."</td>";
                      echo "<td><a href='https://www.cmoney.tw/vt/account-profile-info.aspx?account=".$Account['AccountIDs']."'>可連結但新未新增名字</td>";
                      if($Account['Ratio'] == -1000){
                        echo "<td>無法讀取</td>";
                      }else{
                        echo "<td>".$Ratio."%</td>";
                      }
                      echo  "<td>待新增</td>";
                    echo "</tr>";
                  }
                ?>
              </tbody>
            </table>
          </div>
    
    <script src="js/main.js"></script>
  </body>
</html>
