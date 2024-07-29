<?php

 //foreach  para extraer valores
// 	foreach($_FILES ["archivo"]['tmp_name'] as $key => $tmp_name)
// 	{
	
// Validar que exista el archivo
//		if($_FILES["archivo"]["name"][$key])
//		{
//			$filename = $_FILES["archivo"]["name"][$key];
//			$source = $_FILES["archivo"]["tmp_name"][$key];
		
//			$directorio = 'archivos';  //Ruta a directorio
			// Validar si la ruta existe o crearla
//			if(!file_exists($directorio))
//			{
//				mkdir($directorio,0777) or die ("No se puede crear el directorio");
//			}			
		
//		$dir=opendir($directorio); //Abrir directorio destino
//			$target_path = $directorio. '/'.$filename; // ruta de destino
			
		//Mover y validar el archivo cargado
//			if(move_uploaded_file($source, $target_path))
		//			{
	//					echo "Archivo: $filename almacenado de forma exitosa!!! <br>";
//					} else 
					
//					{
//						echo "Error, por favor intente de nuevo <br>"; 
//					}

//Metodo probado

//$root = realpath($_SERVER["DOCUMENT_ROOT"]); include "$var/www/html/aljibe/documentos"
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


//$nombre_archivo = "documentos/{$archivo['name']}";
//echo "<img src="documentos/$nombre_archivo" />"

//echo "Información del archivo"; 
echo $archivo['name'];




//Abrir directorio
//$directorio = "archivos/";  //Ruta a directorio
//$dir=opendir($directorio); //Abrir directorio destino




//Vamos a mostrar el direectorio ver 1
			
//	foreach( glob("*.*") as $directorio)
//			echo $directorio."<br />";
				
	//			echo "<p>----------------------------</p>";

//Otra forma de listar el archivo

//$aArchivos = opendir($directorio);
//while( ($archivo = readdir($aArchivos)) !== false )  {					
//echo $archivo."<br/>";					
					
//echo "<p>----------------------------</p>";
//echo "<p>Finalizado</p>";					


//otRO METODO MAS

	closedir($dir); //Cerramos directorio destino

//$homepage = file_get_contents('http://aljibe.redhumus.org/subir/archivos');
//echo $homepage;
					
				

	
 
 ?>