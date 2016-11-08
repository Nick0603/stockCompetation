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
  ORDER BY Ratio desc;
  ");


	$userData = [];
	while($row=$data->fetch(PDO::FETCH_ASSOC)){
	  
	      $userData[] = $row;
	 
	}

  echo json_encode( $userData );
?>