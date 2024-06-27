<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Downloader</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="wrapper">

        <!-- Main Content -->
        <div class="main-content" id="main-content">
            <!-- Header Section -->
            <header class="header-bar">
                <div class="container">
                    <button class="menu-btn" onclick="toggleSidebar()">☰</button>
                    <div class="logo">
                        <img src="https://icecomputers.in/assets/images/icons/logo.png" alt="Image Downloader Logo">
                    </div>
                    <nav class="navigation">
                        <ul>
                            <li><a href="index.html">Home</a></li>
                            <li><a href="categories.html">Categories</a></li>
                            <li><a href="about.html">About Us</a></li>
                            <li><a href="contact.html">Contact Us</a></li>
                        </ul>
                    </nav>

                    <?php
                        if ($_SERVER["REQUEST_METHOD"] == "POST") 
                        {
                            $userInput = htmlspecialchars($_POST['userInput']); 
                        }
                    ?>

                    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
                        <label for="userInput">Enter some text:</label>
                        <input type="text" id="userInput" name="userInput" required>
                        <input type="submit" value="Submit">
                    </form>

                </div>
            </header>

            <!-- Main Content Section -->
            <main class="content">
                <div class="gallery">
                <?php 
                    $server = "localhost";
                    $username = "root";
                    $password = "";    
                    $database = "walldown";
        
                    $con = mysqli_connect($server, $username, $password, $database);
        
                    if(!$con)
                    {
                        die("connection to database :".mysqli_connect_error());
                    }

                    // $sql = "SELECT * FROM wallurls WHERE subcategory like '%$userInput%'";
                    $sql = "SELECT * FROM wallurls WHERE subcategory like '%$userInput%' limit 50";

                    $result = $con->query($sql);
                    $result->fetch_assoc();
                    
                    while($row = $result->fetch_assoc()) 
                    {
                        // echo "<a href=".$row['url']."><img src = ".$row['url']." width=30% alt='img not fount' ></a>";
                        echo "<div>";
                        echo '<a href ='. $row['url'] .'>';
                        echo '<div class="gallery-item"><img src='. $row['url'] .' alt="Image"></div>';
                        echo "</div>";
                    }

                    $con->close();
                ?>
                
                </div>
            </main>

            

            <!-- Footer Section -->
            <footer class="footer-bar">
                <div class="container">
                    <p>&copy; 2024 Image Downloader. All Rights Reserved.</p>
                    <nav class="footer-navigation">
                        <ul>
                            <li><a href="privacy.html">Privacy Policy</a></li>
                            <li><a href="terms.html">Terms of Service</a></li>
                            <li><a href="contact.html">Contact Us</a></li>
                        </ul>
                    </nav>
                </div>
            </footer>

        </div>
    </div>
</body>
</html>
