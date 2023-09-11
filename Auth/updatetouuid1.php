<?php

require __DIR__.'/SJLDKGJLKVNA.php';

$UUID = NULL;

$db_connection = new Database();
$conn = $db_connection->__dbConnection();

if(isset($_GET['UUID'])) {
    $UUID = $_GET['UUID'];
}

if(isset($_GET['key'])) {
    $checkkey = $_GET['key'];
}

$checkkey = $_GET['key'];
if(strlen($checkkey) !== 36){
    $finalresult = "false";
}else{
    $key = $_GET['key']; 
}



$SQLStatement = "UPDATE `keys` SET `UUID`='$UUID'WHERE `key`='$key'";

$sth = $conn->prepare($SQLStatement);

$sth->execute();

$result = $sth->fetchAll();

