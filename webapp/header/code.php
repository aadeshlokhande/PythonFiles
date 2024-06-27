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
?>

<?php 

    // $category = "lion";
    // $subcategory = "bhoosdt";
    // $url= "asdkjhadsashkdjasdadsa.sco";

    // $sql =  "INSERT INTO `wallurls` (`category`, `subcategory`, `url`) VALUES ('$category', '$subcategory', '$url');";
    // if ($con -> query($sql) == true)
    // {
    //     echo "<br>done dona done";
    // }
    // else
    // {
    //     echo "Error $sql <br> $con->error";
    // }
    // $con->close();
?>

<?php 
    $sql =  "SELECT * FROM wallurls";

    $result = $con->query($sql);
    $result->fetch_assoc();
    
    while($row = $result->fetch_assoc()) 
    {
        // echo "id: " . $row["ID"]. " - Name: " . $row["category"]. " " . $row["subcategory"]. " url:". $row["url"] ."<br>";
        echo "<a href=".$row['url']."><img src = ".$row['url']." width=30% alt='img not fount' ></a>";
    }

    $con->close();
?>
