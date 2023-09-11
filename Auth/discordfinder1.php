<?php

require __DIR__.'/SJLDKGJLKVNA.php';

$key = NULL;

if(isset($_GET['key'])) {
    $key = $_GET['key'];
}

$db_connection = new Database();
$conn = $db_connection->__dbConnection();

$SQLStatement = "SELECT `discordid` FROM `keys` WHERE `key`='$key'";

$sth = $conn->prepare($SQLStatement);

$sth->execute();

$result = $sth->fetch();



print json_encode($result[0]);