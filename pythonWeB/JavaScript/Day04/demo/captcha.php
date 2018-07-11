<?php
header('content-type:image/jpeg');
$image = imagecreatetruecolor(100, 30);
$white = imagecolorallocate($image, 255, 255, 255);
$black = imagecolorallocate($image, 0, 0, 0);
imagefill($image, 0, 0, $white);
imagestring($image, 5, 35, 8, mt_rand(1000,9999), $black);
imagejpeg($image);
imagedestroy($image);