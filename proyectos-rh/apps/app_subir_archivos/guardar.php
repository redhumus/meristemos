<?php

 
$archivo = (isset($_FILES['archivo'])) ? $_FILES['archivo'] : null;
if ($archivo) {
   $extension = pathinfo($archivo['name'], PATHINFO_EXTENSION);
   $extension = strtolower($extension);
   $extension_correcta = (
	$extension == 'docx' or $extension == 'doc' or $extension == 'pdf' or $extension == 'md' or $extension == 'ods' or $extension == 'shx' or $extension == 'shp' or $extension == 'dbf' or $extension == 'qpj' or $extension == 'prj' or $extension == 'tiff' or $extension == 'jpg' or $extension == 'jpeg' or $extension == 'gif' or $extension == 'png' or $extension == 'gdb' );
   
   if ($extension_correcta) {
      $ruta_destino_archivo = "documentos/{$archivo['name']}";
      $archivo_ok = move_uploaded_file($archivo['tmp_name'], $ruta_destino_archivo);
		}
echo "<h2> Archivo cargado con éxito</h2></br><h2>Detalles del archivo</h2></br>";
	

}

print_r($_FILES); 

//Pasamos la otra parte que estaba en el html

//echo "archivos/{$archivo['name']}";


//Otra enesima forma mas



$directorio = opendir("archivos/"); //ruta actual
while ($archivo = readdir($directorio)) //obtenemos un archivo y luego otro sucesivamente
{
    if (is_dir($archivo))//verificamos si es o no un directorio
    {
        echo "[".$archivo . "]<br />"; //de ser un directorio lo envolvemos entre corchetes
    }
    else
    {
        echo $archivo . "<br />";
    }
}



					
				

	
 
 ?>