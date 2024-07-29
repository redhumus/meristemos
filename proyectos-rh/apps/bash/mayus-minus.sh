#!/bin/bash

#Herramienta que transforma texto de mayúsculas a minúsculas y viceversa

echo "'|>>>>>>>>>>>>>>>>>>>>  <<<<<<<<<<<<<<<<<<<<|\n'
'|------------------------------------------|\n'
'|*********Este es un desarrollo de*********|\n'
'|**********La Mica Prieta Software*********|\n'
'|     COPYLEFT 2022 - Licencia GPL V.3     |\n'
'|------------------------------------------|\n'
'|>>>>>>>>>>>>>>>>>>>>  <<<<<<<<<<<<<<<<<<<<|\n'"



echo "Ingrese una cadena de texto:"
read texto

echo "¿Desea convertir el texto a mayúsculas o minúsculas? ( 1 para mayúsculas, 2 para minúsculas)"
read opcion

if [[ $opcion == "1" ]]; then
  texto_transformado=$(echo $texto | tr '[:lower:]' '[:upper:]')
elif [[ $opcion == "2" ]]; then
  texto_transformado=$(echo $texto | tr '[:upper:]' '[:lower:]')
else
  echo "Opción no válida"
  exit 1
fi

echo "Texto transformado: $texto_transformado"
