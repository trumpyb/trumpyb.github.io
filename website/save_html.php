
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $websiteUrl = $_POST["websiteUrl"];

    // Fetch HTML content
    $htmlContent = file_get_contents($websiteUrl);

    // Save HTML content to a text file
    $filename = "saved_html.txt";
    file_put_contents($filename, $htmlContent);

    echo "HTML content saved successfully in $filename";
}
?>
