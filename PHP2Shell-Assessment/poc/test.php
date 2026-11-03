<?php
header('Content-Type: application/json');
echo json_encode([
    'status' => 'success',
    'php_version' => PHP_VERSION,
    'sapi' => PHP_SAPI,
    'architecture' => PHP_INT_SIZE * 8
], JSON_PRETTY_PRINT);
