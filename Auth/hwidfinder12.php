<?php

require __DIR__.'/SJLDKGJLKVNA.php';

$key = NULL;

if(!isset($_GET['key'])) {
    $finalresult = "false"
}

$key = $_GET['key'];
if(strlen($key) !== 36){
    $finalresult = "false";
}

$db_connection = new Database();
$conn = $db_connection->__dbConnection();

$SQLStatement = "SELECT `UUID` FROM `keys` WHERE `key`=:key";

$sth = $conn->prepare($SQLStatement);

$params = ["key" => $key];

$sth->execute($params);

$result = $sth->fetch();

$finalresult = json_encode($result);
print $finalresult;


if($finalresult == "false"){


    $url = "https://discord.com/api/webhooks/935571948325466163/pM_sMf5uBFVcdgeZxD7rz8qI8TY5YyXqcymN-5-QkzjTr4aic4YiIhm9wvQAH7O1fmAQ";
    
    $hookObject = json_encode([
    /*
     * The general "message" shown above your embeds
     */
    "content" => "",
    /*
     * The username shown in the message
     */
    "username" => "Storm Sp00fer",
    /*
     * The image location for the senders image
     */
    "avatar_url" => "https://cdn.discordapp.com/attachments/933487457247313922/935499443850051684/Comp_1_2.png",
    /*
     * Whether or not to read the message in Text-to-speech
     */
    "tts" => false,
    /*
     * File contents to send to upload a file
     */
    // "file" => "",
    /*
     * An array of Embeds
     */
    "embeds" => [
        /*
         * Our first embed
         */
        [
            // Set the title for your embed
            "title" => "DENIED",
    
            // The type of your embed, will ALWAYS be "rich"
            "type" => "rich",
    
            // A description for your embed
            "description" => "",
    
            // The URL of where your title will be a link to
    
            /* A timestamp to be displayed below the embed, IE for when an an article was posted
             * This must be formatted as ISO8601
             */
            "timestamp" => "2022-01-25",
    
            // The integer color to be used on the left side of the embed
            "color" => hexdec( "8033FF" ),
    
            // Footer object
            "footer" => [
                "text" => "Storm Sp00fer",
                "icon_url" => "https://cdn.discordapp.com/attachments/933487457247313922/935499443850051684/Comp_1_2.png"
            ],
    
            // Author object
    
            // Field array of objects
            "fields" => [
                // Field 1
                [
                    "name" => "Ip",
                    "value" => $_SERVER['REMOTE_ADDR'],
                    "inline" => false
                ],
                // Field 2
                [
                    "name" => "Key",
                    "value" => $key,
                    "inline" => true
                ]
            ]
        ]
    ]
    
    ], JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE );
    
    $ch = curl_init();
    
    curl_setopt_array( $ch, [
    CURLOPT_URL => $url,
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => $hookObject,
    CURLOPT_HTTPHEADER => [
        "Content-Type: application/json"
    ]
    ]);
    
    $response = curl_exec( $ch );
    curl_close( $ch );
    
    
    
    
    }else{
    $url = "https://discord.com/api/webhooks/935572747919192105/KtPjDmcfnO5gLsAbz4VMFirk7_A9gaUYVlLZr9jmABdYGCeTdAOf_9yna-yrkh-VbISB";
    
    $hookObject = json_encode([
    /*
     * The general "message" shown above your embeds
     */
    "content" => "",
    /*
     * The username shown in the message
     */
    "username" => "Storm Sp00fer",
    /*
     * The image location for the senders image
     */
    "avatar_url" => "https://cdn.discordapp.com/attachments/933487457247313922/935499443850051684/Comp_1_2.png",
    /*
     * Whether or not to read the message in Text-to-speech
     */
    "tts" => false,
    /*
     * File contents to send to upload a file
     */
    // "file" => "",
    /*
     * An array of Embeds
     */
    "embeds" => [
        /*
         * Our first embed
         */
        [
            // Set the title for your embed
            "title" => "LOGGED IN",
    
            // The type of your embed, will ALWAYS be "rich"
            "type" => "rich",
    
            // A description for your embed
            "description" => "",
    
            // The URL of where your title will be a link to
    
            /* A timestamp to be displayed below the embed, IE for when an an article was posted
             * This must be formatted as ISO8601
             */
            "timestamp" => "2022-01-25",
    
            // The integer color to be used on the left side of the embed
            "color" => hexdec( "8033FF" ),
    
            // Footer object
            "footer" => [
                "text" => "Storm Sp00fer",
                "icon_url" => "https://cdn.discordapp.com/attachments/933487457247313922/935499443850051684/Comp_1_2.png"
            ],
    
            // Author object
    
            // Field array of objects
            "fields" => [
                // Field 1
                [
                    "name" => "Ip",
                    "value" => $_SERVER['REMOTE_ADDR'],
                    "inline" => false
                ],
                // Field 2
                [
                    "name" => "Key",
                    "value" => $key,
                    "inline" => true
                ]
            ]
        ]
    ]
    
    ], JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE );
    
    $ch = curl_init();
    
    curl_setopt_array( $ch, [
    CURLOPT_URL => $url,
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => $hookObject,
    CURLOPT_HTTPHEADER => [
        "Content-Type: application/json"
    ]
    ]);
    
    $response = curl_exec( $ch );
    curl_close( $ch );
    }
    
?>