<?php
header('Content-Type: application/json');

// MySQL connection details
$host = 'localhost';
$username = 'test';
$password = 'test';

// Attempt to connect to MySQL server
try {
    $connection = new mysqli($host, $username, $password);
    if ($connection->connect_error) {
        throw new Exception('Connection failed: ' . $connection->connect_error);
    } else {
        $response = [
            'success' => true,
            'message' => 'Connection successful'
        ];
        echo json_encode($response);
        exit;
    }
} catch (Exception $e) {
    $response = [
        'success' => false,
        'message' => $e->getMessage()
    ];
    echo json_encode($response);
    exit;
}
?>
