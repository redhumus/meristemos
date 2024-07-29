<?php
    // accepted file extensions
    $extensions = array("pdf","mp3","zip","rar");
 
   // file name to download incluyendo el .pdf para nuestro caso
    $file = $_GET["file"].".pdf";
 
    // file size
    $size = filesize($file);
 
    // Prevent go throught directories
    if(strpos($file,"/")!==false){
        die("Permission denied to change directory, please, especify only$
    }
 
    // test the file estension
    $ftmp = explode(".",$file);
    $fExt = strtolower($ftmp[count($ftmp)-1]);
    if(!in_array($fExt,$extensions)){
        die("ERROR: File extension not recognized: $fExt");
    }
 
    // if it was ok, let's download it
    header("Content-Transfer-Encoding: binary");    
    header("Content-type: application/octet-stream");
    header("Content-Disposition: attachment; filename=$file");
    header("Content-Length: $size");
    $fp=fopen("$file", "r");
    fpassthru($fp);
?>

