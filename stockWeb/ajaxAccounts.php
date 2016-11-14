<?php

$dbhost = 'localhost';
$dbname = 'stockcompetition';
$dbuser = 'root';
$dbpwd = 'root';

$conn = new PDO('mysql:host='.$dbhost.';dbname='.$dbname.';port=3306',$dbuser,$dbpwd);
$conn->exec('set names utf8');

$data = $conn->query(" 
  SELECT teams.*,group_concat(Accounts.AccountID separator ',')  as AccountIDs
  FROM teams
  INNER JOIN Accounts on Accounts.teamID = teams.teamID
  GROUP BY teams.teamID
  ");


  $userData = [];
  while($row=$data->fetch(PDO::FETCH_ASSOC)){
    
        $userData[] = $row;
   
  }

  echo json_encode( $userData );


?>