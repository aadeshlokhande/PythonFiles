<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "walldown";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT ID, category, subcategory, url FROM wallurls";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<tr>
                <td>" . $row["id"]. "</td>
                <td>" . $row["category"]. "</td>
                <td>" . $row["subcategory"]. "</td>
                <td><a href='" . $row["url"]. "' target='_blank'>" . $row["url"]. "</a></td>
              </tr>";
    }
} else {
    echo "<tr><td colspan='4'>No data found</td></tr>";
}
$conn->close();
?>
