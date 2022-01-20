# Prueba-Tecnica-Destacame

## Descripción

Una agencia de buses necesita una plataforma para gestionar sus viajes. El sistema debe permitir que se ingresen diversos trayectos. Cada trayecto tendrá varios buses asignados a distintos horarios. Cada bus tendrá un solo chofer y varios pasajeros asignados a sus asientos. Todos los buses tienen la misma capacidad de 10 pasajeros sentados. Los asientos son numerados y se reservan para cada pasajero. El sistema debe soportar el ingreso de pasajeros a un trayecto y horario en particular, además de permitir la asignación de choferes a sus respectivos buses.

## Supuestos 

* La agencia de buses sólo realiza viajes entre ciudades de Chile.
* La agencia ofrece sus servicios en 5 terminales de buses a lo largo del país. 
* La agencia cuenta con buses y conductores habilitados para realizar los viajes.
* Todos los buses cuentan con las condiciones técnicas y de seguridad para realizar los viajes.
* Los trayectos son entre dos terminales de forma directa y sin recolectar pasajeros en puntos intermedios. 
* Un usuario de tipo "manager" es el encargado de realizar la carga de trayectos, viajes, terminales y choferes.
* No existe una acción de pago cuando un usuario reserva el asiento de un bus en un trayecto y horario particular. 
* Un pasajero tiene que iniciar sesión con una cuenta registrada en el sistema para poder reservar asientos.
* Los trayectos son sólo entre terminales, por lo tanto, su número es limitado a la combinación de terminales. 

## Modelo de datos

La base de datos se crea a partir de los requerimientos planteados y los supuestos realizados. Cabe destacar que se opta por utilizar el sistema de autenticación y permisos nativo de Django. Por lo que para diferenciar los tipos de usuario, se crean grupos: "Passenger", "Driver" y "Manager" en vez de crear tablas independientes. Además de crear los permisos necesarios que requiere cada tipo de usuario.   

![Image text](https://github.com/Sugatvo/Prueba-Tecnica-Destacame/blob/main/base_de_datos.png)

## Configuración 
### Instalando Python
1. El primer paso corresponde a instalar la última versión de python (3.9.1). Para hacer esto, dirigirse a la página web <https://www.python.org/downloads/> y descargue el archivo que correspondiente con las especificaciónes de su sistema.
2. Luego, siga las instrucciones de instalación de la página. 

### Instalando las librerias de Python
1. Abrir un terminal (Command Promp en Windows).
2. Usar el commando "cd" y navegar al directorio en donde se encuentra requirements.txt.
3. Instalar las dependencias requeridas utilizando el comando `pip install -r requirements.txt` en el terminal.
> Nota: Es recomendado instalar todos los paquetes en un entorno virtual. La documentación oficial se encuentra disponible en el siguiente link: <https://docs.python.org/3/library/venv.html>

### Instalando PostgreSQL
El sistema de gestión de base de datos que utiliza el proyecto es PostgresSQL. El cual se puede descargar mediante el siguiente link: <https://www.postgresql.org/download/>
1. Siga las instrucciones para instalar PostgresSQL.
2. Agregue las variables de entorno al path del sistema.
2. Cuando este listo, abra un terminal (Command Promp en Windows). 
3. Use el comando "cd" para navegar a la carpeta en donde el repositorio fue guardado.
4. Conectarse al usuario por defecto de PostgreSQL con el siguien comando: `psql -U postgres`.
5. Use la contraseña configurada en el proceso de instalación.
6. Crear la base de datos con el siguiente comando:
```
CREATE DATABASE bus_agency;
```
6. Salir de psql con el comando \q.
7. Ejecutar comando: `psql -d bus_agency -f busagency.sql -U postgres ` para importar base de datos.
8. Ahora la base de datos está lista. 
9. Por último, agregar configuración en el archivo: "~/Prueba-Tecnica-Destacame/bus_agency/bus_agency/settings.py".


### Instalando Vue.js, Axios, Router, Vuex
1. Para adquirir Vue.js, lo primero que se tiene que hacer corresponde a instalar Node.js/npm. Por lo tanto, descarguelo a través del siguiente link: https://nodejs.org/en/download/.
2. Siga las intrsucciones para instalar Node.js/npm.
3. Abra un terminal y dirijase al directorio del frontend: "~/Prueba-Tecnica-Destacame/bus_agency/bus_frontend/".
4. Luego para instala Vue.js, ingresar el comando `npm install -g @vue/cli`.
5. Instalar axios con: `npm install axios`.
6. Instalar Vuex Router con: `npm install vue-router`.
7. Instalar Vuex Store con: `npm install vuex`.

### ¿Como iniciar el proyecto?

1. Abrir un terminal.
2. Iniciar entorno virtual (si es que fue creado).
3. Navegar al directorio: "~/Prueba-Tecnica-Destacame/bus_agency/" donde se encuentra el archivo manage.py.
4. Iniciar backend a través del siguiente comando: ` python manage.py runserver`.
5. Abrir otro terminal.
6. Navegar al directorio: "~/Prueba-Tecnica-Destacame/bus_agency/bus_frontend".
7. Ejecutar el comando: `npm run serve`.
8. Ir a la dirección url que se muestra en el terminal. Debiese ser: "http://localhost:8080/"

## Testing
Para evaluar y comprobar el comportamiento del backend del sistema. Se crean 222 test para validar que las respuestas HTTP corresponden con las deseadas y, en concreto, se testean los siguiente tipos de request: GET, POST, OPTION, PUT, PATCH, DELETE de todos los modelos. Asegurando que:  

* Solo un usuario de tipo "Manager" puede editar, borrar y actualizar los terminales, trayectos, viajes y choferes del sistema. 
* Un usuario de tipo "Passenger" solo puede leer, borrar y escribir los objectos de los que es dueño.
* Mantener la información personal privada.
* Denegar cualquier tipo de request sin autenticación que cambie los modelos.

Para **ejecutar** los test:
1. Abrir terminal.
2. Instalar pytest-django con el siguiente comando:`pip install pytest-django`.
3. Navegar al directorio en donde se encuentra el archivo manage.py
4. Ejecutar el siguiente comando: `pytest bus_backend/test`.
