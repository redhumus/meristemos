# Proyecto: Archivo Orlando Fals Borda

 
Tengo dos hojas de excel:

- Datos de la colección de documentos : con las columnas: No. Índice, Serie, Subserie, No. Caja, No. de carpeta, No. de orden, Fecha extrema inicio (en formado dd-mm-aaaa), Fecha extrema Final (en formado dd-mm-aaaa), Título, Descripción, Autor o productor, Folios, Volumen (número de folios), Soporte, Signatura Topográfica anterior, Observaciones. 

- Datos de fotografías: con las columnas: No. Fotografía, Ubicación, soporte físico en Carpeta, Ubicación, soporte físico en Sobres, Categoría Principal, Sub-categoría, Autor de la Fotografía, Título de la fotografía, Descripción iconografica, Fecha de captura de la fotografía, Anotación y observación propia de la fotografía, Tema principal, Tema secundario, Tema terciario, Nombre primario de personas e instituciones N°1, Nombre secundario de personas e instituciones N°2, Nombre terciario de personas e instituciones N°3, Nombre principal de lugar, Nombre secundario de lugar, Nombre terciario de lugar, B y N, Color o Sepia, Tamaño (cms.) de la fotografía. El proyecto es desarrollar una App web que permita consultar y visualizar los datos que están en las dos hojas de excel migrados una una base de datos relacional. Cómo puedo desarrollar este proyecto?

 
Para desarrollar la aplicación web que permita consultar y visualizar los datos de las dos hojas de Excel migrados a una base de datos relacional, se pueden seguir los siguientes pasos:

1.  Crear una base de datos relacional: Para esto, se puede utilizar un sistema de gestión de bases de datos (DBMS) como MySQL, PostgreSQL, Oracle, etc. La base de datos debe tener una estructura que permita almacenar los datos de las dos hojas de Excel. Se pueden crear tablas para cada hoja de Excel, y establecer relaciones entre ellas si es necesario.
    
2.  Importar los datos de Excel a la base de datos: Para esto, se pueden utilizar herramientas como MySQL Workbench o el comando LOAD DATA INFILE de MySQL. Es importante asegurarse de que los datos se importen correctamente a la base de datos y que se respete la estructura definida en el paso anterior.
    
3.  Crear una aplicación web: Para esto, se pueden utilizar diferentes frameworks y lenguajes de programación, como Django (Python), Laravel (PHP), Ruby on Rails (Ruby), entre otros. Se debe crear una aplicación que permita a los usuarios consultar y visualizar los datos almacenados en la base de datos. La aplicación debe ser intuitiva y fácil de usar para los usuarios.
    
4.  Diseñar la interfaz de usuario: La interfaz de usuario debe ser atractiva y fácil de navegar. Se pueden utilizar librerías y frameworks de diseño como Bootstrap, Materialize, entre otros.
    
5.  Desarrollar las consultas a la base de datos: La aplicación debe permitir a los usuarios realizar consultas a la base de datos. Se deben crear consultas que permitan filtrar y ordenar los datos de acuerdo a los criterios deseados. Las consultas deben ser eficientes y optimizadas para que la aplicación tenga un buen rendimiento.
    
6.  Implementar la seguridad: Es importante implementar medidas de seguridad en la aplicación para evitar posibles ataques y vulnerabilidades. Se deben utilizar técnicas como la validación de entradas, la encriptación de contraseñas, la prevención de inyección SQL, entre otras.
    
7.  Probar la aplicación: Es importante realizar pruebas exhaustivas de la aplicación para asegurarse de que funciona correctamente y no presenta errores o fallas. Se deben realizar pruebas de funcionalidad, pruebas de usabilidad, pruebas de rendimiento, entre otras.
    

Una vez completados estos pasos, se tendría una aplicación web que permite consultar y visualizar los datos de las dos hojas de Excel migrados a una base de datos relacional. Es importante tener en cuenta que el desarrollo de una aplicación web puede ser un proceso complejo y requiere de habilidades y conocimientos en programación, diseño, bases de datos y seguridad.