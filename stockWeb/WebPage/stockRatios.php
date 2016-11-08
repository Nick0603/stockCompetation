<?php
	$conn = new PDO('mysql:host=localhost;dbname=stockcompetation;port=3306','root','root');
	$conn->exec('set names utf8');

	$statement = $conn->query('select * from teamRatios Order By Ratio desc');
	foreach($statement as $row){
	    echo $row['user']." ".$row['pwd']."<br>";
	}

?>