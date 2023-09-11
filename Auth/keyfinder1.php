<?php

require __DIR__.'/SJLDKGJLKVNA.php';

$key = NULL;

$db_connection = new Database();
$conn = $db_connection->__dbConnection();

$SQLStatement = "SELECT * FROM `keys`";

$sth = $conn->prepare($SQLStatement);

$sth->execute();

$result = $sth->fetchAll();

function hasValue($arr, $val) {
    foreach($arr as $currentArr) {
        $status = in_array($val, $currentArr);

        if ($status === true) {
            break;
        } 
    };

    return [
        'status' => $status,
        'value' => $val
    ];
}

if(isset($_GET['key'])) {
    $key = $_GET['key'];
}


print json_encode(hasValue($result, $key));