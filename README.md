# TRABAJO  - FIN DE MODULO

##### Realizado por: 
###### *Orlando Choque Ayma*
#### Descripcion:
Este proyecto esta desarrollado en python con el framework flask y una coneccion a un SGBD postgresql e implementado en hosting: render.com con la url:
https://proyecto-modulo3.onrender.com

#### Base de datos y tablas:

* Crear la base de datos db_api_flask
* Crear la tabla de acuerdo al script (crear_tablas) incluido en el proyecto y la insercion de datos correspondientes:


*create table usuarios(
cedula_identidad numeric(8) primary key,
nombre varchar(30),
primer_apellido varchar(30),
segundo_apellido varchar(30),
fecha_nacimiento date);*

*insert into usuarios values(1234,'juan','Perez','Guzman','1960-04-12'),
(1236,'Ana','Barbara','Rodriguez','1970-11-12'),
(1237,'Jorge','Alvarez','Mamani','1990-09-01');*

#### Configuracion del archivo .env

En este archivo se guarda la informacion de la connecion a la base de datos, por lo que se debera adecuar al servidor en uso, bajo la siguiente estructura:

* PG_HOST = `'localhost'`
* PG_USER = `'postgres'`
* PG_PASSWORD = `'postgres'`
* PG_DB = `'db_api_flask'`




#### API REST para pruebas.  
Servicio que permite hacer CRUD de entidad `usuarios` mediante requests HTTP con el respectivo método y payload.
El payload soportado es en formato JSON.  
Ejemplo de serialización de un `Usuario`:  
``
{
    "cedula_identidad": 12345,
    "nombre": "Jose Luis",
    "primer_apellido": "Espinoza",
    "segundo_apellido": "Rodriguez",
    "fecha_nacimiento": "1970-11-12"
}
``

#### Métodos soportados:
* GET: obtener información de un usuario dado la cedula_identidad, todos los usuarios, promedio de edades y la version del api rest. 
* POST: crear un nuevo `Usuario`
* PUT: actualizar la información de un `Usuario` de acuerdo a la cedula_identidad
* DELETE: eliminar un `Usuario` dado la cedula_identidad

#### Para ejecutar el servidor:
* Instalar las librerias:
  *flask
psycopg2
flask_cors
python-decouple 
python-dotenv*
*>pip install flask ....*
* Para ejecutar:
  >python ./src/app.py
    
* La url del servidor es:
   https://proyecto-modulo3.onrender.com implementado en render.com.
   
#### Ejemplos  de requests
Tomando en cuenta que la api esta en un servidor render.com se procedera de la siguiente manera, la url cambiara si se utiliza otro host.
* Obtener información de todos los usuarios:  
`GET https://proyecto-modulo3.onrender.com/usuarios` 

* Obtener información de un usuario  en particular (por No. de cedula de identidad): 

    `GET https://proyecto-modulo3.onrender.com/usuarios/:1234` 

* Dar de alta un usuario:  
`POST https://proyecto-modulo3.onrender.com/usuarios` 
con el payload

* Actualizar la información de un usuario existente:  
`PUT https://proyecto-modulo3.onrender.com/usuarios/:1234` 
con el payload 

* Eliminar un usuario  
`DELETE https://proyecto-modulo3.onrender.com/usuarios/:1234`

* Muestra el  prodmedio de edades de todos los usuario:  
`GET https://proyecto-modulo3.onrender.com/usuarios/promedio-edad`

* Muestra la version del api rest:
  
    `GET https://proyecto-modulo3.onrender.com/estado`


