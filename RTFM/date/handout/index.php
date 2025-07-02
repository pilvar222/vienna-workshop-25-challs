<?php
// Get date format from user parameter, default to day of the week
$format = isset($_GET['format']) ? $_GET['format'] : 'l';

// Get the current date based on the format
$currentDate = date($format);

// Read the content from the appropriate day file
$dayContent = file_get_contents("days/" . $currentDate . ".txt");

?>
<!DOCTYPE html>
<html>
<head>
    <title>Daily Date Display</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            max-width: 600px; 
            margin: 50px auto; 
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Daily Date Display</h1>        
        <p><?php echo $dayContent; ?></p>
    </div>
</body>
</html> 