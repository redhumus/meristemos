<?php

//$root = realpath($_SERVER["DOCUMENT_ROOT"]); include "$var/www/html/aljibe"

$archivo = (isset($_FILES['archivo'])) ? $_FILES['archivo'] : null;
if ($archivo) {
   $extension = pathinfo($archivo['name'], PATHINFO_EXTENSION);
   $extension = strtolower($extension);
   $extension_correcta = (
$extension == 'shx' or $extension == 'docx' or $extension == 'doc' or $extension == 'pdf' or $extension == 'md' or $extension == 'ods' or $extension == 'shp' or $extension == 'dbf' or $extension == 'qpj' or $extension == 'prj' or $extension == 'tiff' or $extension == 'jpg' or $extension == 'jpeg' or $extension == 'gif' or $extension == 'png');
   if ($extension_correcta) {
      $ruta_destino_archivo = "documentos/{$archivo['name']}";
      $archivo_ok = move_uploaded_file($archivo['tmp_name'], $ruta_destino_archivo);
   }
    
}


//Otra enesima forma mas


$directorio = opendir("documentos/"); //ruta actual
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
<!DOCTYPE html>
<html>
 <head>
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
 <title> Subir archivos </title>
 </head>
 <body>  
    <?php if (isset($archivo)): ?>
       <?php if (!$extension_correcta): ?>
         <span style="color: #f00;"> La extensión es incorrecta, el archivo debe ser doc, docx, ods, pdf, md, jpg, jpeg, gif o png. </span> 
       <?php elseif (!$archivo_ok): ?>
         <span style="color: #f00;"> Error al intentar subir el archivo. </span>
      <?php else: ?>
         <strong> El archivo ha sido subido correctamente. </strong>
         <br />
         <img src="archivos/<?php echo $archivo['name'] ?>" alt="" />
      <?php  print_r($_FILES)?> 
      <?php endif ?>
   <?php endif; ?>

   
   <form name="form1" id="form1" method="post" action="index.php" enctype="multipart/form-data">
      <label>Archivo</label>
      
           
      <input type="file" name="archivo" required="required" multiple="" />
 		<input type="submit" value="Subir" /> 
	
   </form>
					
					
<!-- Un nuevo form frankestein

		<div class="container">
			<div class="panel-body">
			
				<form name="form2" id="form2" method="post" action="guarda.php" enctype="multipart/form-data">
						<h4 class="text-center">Cargar múltiples archivos</h4>
						
						<div class="form-group">
								<label class="col-sm-2 control-label">Archivos</label>				
								<div class="col-sm-8">
								<input type="file" class="form-control" id="archivo[]" name="archivo[]" multiple="" />
								</div>
								
								
								<button type="submit" class="btn btn-primary">***Cargar***</button>						
						
						</div>						
						
				</form>
				</div>		
				
		</div>
		
//Cierre frakestein
		
		
 -->
 
 
 </body>
</html>
