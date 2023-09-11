<?php

class Database {
    private $db_host;
    private $db_name;
    private $db_user;
    private $db_password;

    public function __construct() {
        if (strpos($_SERVER['HTTP_HOST'], 'strato')) {
            $this->db_host='';$this->db_name='';
            $this->db_user='';$this->db_password='';
        } else if (strpos($_SERVER['HTTP_HOST'], 'vibe')) {
            $this->db_host='';$this->db_name='';
            $this->db_user='';$this->db_password='';
        }
        else { 
            $this->db_host='127.0.0.1';$this->db_name='s25228_stormsploever';
            $this->db_user='root';$this->db_password=''; 
        }
    }
    
    public function __dbConnection() {
        try{
            $conn = new PDO('mysql:host='.$this->db_host.';dbname='.$this->db_name,$this->db_user,$this->db_password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            return $conn;
        }
        catch(PDOException $e){
            echo "Connection error: ".$e->getMessage(); 
            exit;
        }     
    }
}
?>