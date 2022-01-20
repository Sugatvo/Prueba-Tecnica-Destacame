# Prueba-Tecnica-Destacame

## Descripción

Una agencia de buses necesita una plataforma para gestionar sus viajes. El sistema debe permitir que se ingresen diversos trayectos. Cada trayecto tendrá varios buses asignados a distintos horarios. Cada bus tendrá un solo chofer y varios pasajeros asignados a sus asientos. Todos los buses tienen la misma capacidad de 10 pasajeros sentados. Los asientos son numerados y se reservan para cada pasajero. El sistema debe soportar el ingreso de pasajeros a un trayecto y horario en particular, además de permitir la asignación de choferes a sus respectivos buses.

## Supuestos 

* La agencia de buses sólo realiza viajes entre ciudades de Chile.
* La agencia ofrece sus servicios en 15 terminales de buses a lo largo del país. 
* La agencia cuenta con 30 buses y 30 conductores habilitados para realizar los viajes.
* Todos los buses cuentan con las condiciones técnicas y de seguridad para realizar los viajes.
* Los trayectos son entre dos terminales de forma directa y sin recolectar pasajeros en puntos intermedios. 
* Un usuario de tipo "adminitrador" es el encargado de realizar la carga de trayectos.
* No existe una acción de pago cuando un usuario reserva el asiento de un bus en un trayecto y horario particular. 
* Un pasajero tiene que iniciar sesión con una cuenta registrada en el sistema para poder reservar asientos.


## Instalación
https://www.postgresql.org/download/


descarga y instalar https://nodejs.org/en/download/
npm install -g @vue/cli
npm install axios
npm install vuex