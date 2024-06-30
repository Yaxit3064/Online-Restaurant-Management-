<?php
// Start session
session_start();

// Include database connection
include_once 'db_connection.php';

// Check if admin is logged in
if(!isset($_SESSION['admin_id'])) {
    header("Location: admin_login.php");
    exit();
}

// Fetch admin details
$admin_id = $_SESSION['admin_id'];
$query = "SELECT * FROM admins WHERE id = $admin_id";
$result = mysqli_query($conn, $query);
$admin = mysqli_fetch_assoc($result);

// Fetch all bookings
$query = "SELECT * FROM bookings";
$result = mysqli_query($conn, $query);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
    <!-- Add your CSS and JavaScript links here -->
</head>
<body>
    <h1>Welcome, <?php echo $admin['username']; ?></h1>
    
    <h2>All Bookings:</h2>
    <table>
        <tr>
            <th>Booking ID</th>
            <th>User ID</th>
            <th>Restaurant Name</th>
            <th>Date</th>
            <th>Time</th>
        </tr>
        <?php while($booking = mysqli_fetch_assoc($result)): ?>
        <tr>
            <td><?php echo $booking['id']; ?></td>
            <td><?php echo $booking['user_id']; ?></td>
            <td><?php echo $booking['restaurant_name']; ?></td>
            <td><?php echo $booking['booking_date']; ?></td>
            <td><?php echo $booking['booking_time']; ?></td>
        </tr>
        <?php endwhile; ?>
    </table>
    
    <h2>Manage Restaurants:</h2>
    <!-- Add functionality to manage restaurants -->
    
    <h2>Manage Users:</h2>
    <!-- Add functionality to manage users -->
    
</body>
</html>
