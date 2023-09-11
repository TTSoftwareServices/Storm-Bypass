<?php

if(isset($_GET['myversion'])) {
    $myversion = $_GET['myversion'];
}

$newestversion = "2.1";


if($newestversion === $myversion){
    print json_encode("true");

}else{
    print json_encode("false");
}