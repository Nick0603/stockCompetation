<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>StockCompetition</title>

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
            <table class="table">
              <thead id="table_head">
                <tr>
                  <td>組別</td>
                  <td>隊伍名稱</td>
                  <td>投資報酬率</td>
                  <td>購買證券</td>
                </tr>
              </thead>
              <tbody id="table_body">
              </tbody>
            </table>
          </div>
    
    <script src="js/main.js"></script>
  </body>
</html>
