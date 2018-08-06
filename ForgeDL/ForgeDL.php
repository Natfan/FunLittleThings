<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

$file = file_get_contents("./data.json");
$json = json_decode($file, TRUE);
$files_array = $json["files"];
foreach ($files as $key => $val) {
	if (is_array($val)) {
		echo "$key:\n";
	} else {
		echo "$key => $val\n";
	}
}
?>