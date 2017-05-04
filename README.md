# Hackaton Cecen

MTE es una aplicación hecha con Django y MySQL para llevar a cabo las finanzas de un conjunto de cooperativas sociales fundadas y administradas por una organización social del mismo nombre.

Contamos con 3 tipos de usuarios (que corresponden a 3 personas físicas distintas):
  1.  Data entry
  2. Administrador general
  3. Tesorero

La persona que se encarga del data entry y el administrador general trabajan en la misma habitación, mientras que el tesorero se encuentra en otra oficina.

El data entry primero sube un ticket / informe de un pago o un cobro completando una serie de campos. Esto ingresa el ticket al sistema, colocándolo en el estado *pendiente*. Luego, el administrador evalúa si los datos subidos son correctos, llena algunos campos más (que no pueden ser completados por el data entry) y le cambia el estado al ticket. 

Este nuevo estado puede ser *aprobado* o *rechazado*. En caso de ser *rechazado*, el ticket vuelve al data entry, para que corrija los errores. Es importante notar que los campos que llena el data entry no pueden ser modificados por el administrador general, y viceversa. En caso de que el administrador cambie el estado a *pendiente*, el ticket pasa hacia el tesorero, quien efectivamente realiza la transferencia de dinero y cambia el estado del ticket a *pagado*.

Una vez que un ticket es colocado como *pagado*, este es removido de la lista de tickets a procesar y se inserta en una base de datos que contiene todos los tickets históricos.

## To do:
- Sistema de log in (3 tipos de usuarios con distintos privilegios)
- Modelo
- Cambiar la base por mysql ??

## Tecnologías utilizadas
* [Django](http://www.djangoproject.com) - Web framework de Python
* [MySQL](http://www.mysql.com) - Base de datos relacional
* [Django-Bootstrap3](https://github.com/dyve/django-bootstrap3) - Herramienta para hacer forms

## Instalación

Para correrlo, se requiere tener instalado Python y Django.

Una vez que tengamos eso, se puede clonar el proyecto en una carpeta y arrancar el server haciendo en una terminal:

```sh
cd HackatonCecen
python manage.py runserver
```

Esto nos iniciará un server en http://127.0.0.1:8000/. 

Para acceder a la app, debemos entrar desde un navegador a http://127.0.0.1:8000/tracker

