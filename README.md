<p align="center">
<img src=https://drive.google.com/uc?export=view&id=1XOqik5P0CnPdmt452a-BoI_Jj6cTYeL1 alt="Banner">
</p>
<h3 align="center">Caso de Negocio N°2 - Biblioteca App</h3>

---

<p align="center"> Como parte de un equipo de desarrolladores, recibimos el pedido del departamento de Producto para desarrollar una aplicación para dar funcionalidades a una biblioteca, la cual permitirá a sus usuarios consultar el catálogo de libros, y un listado de los préstamos de libros realizados a sus socios.
<br> 
</p>

---

## 📝 Tabla de Contenidos
- [Consigna](#problem_statement)
    - [Objetivo](#our_goals)
    - [Requerimientos Generales](#requirements)
    - [Modelo](#database)
    - [Requerimientos Tecnicos](#tech_req)
- [Instalación/Ejecucion](#getting_started)
- [Vista Previa](#preview)
- [Tecnologias](#tech_stack)
- [Autor](#authors)

## 🧐 Consigna <a name = "problem_statement"></a>

### Nuestro objetivo 🎯 <a name = "our_goals"></a>
El objetivo consiste en desarrollar una aplicación web que permita registrar los libros que la biblioteca ofrece, registrar empleados y socios, realizar el préstamo de algún libro a un socio y visualizar diferentes tipos de listados. Por último, se pide la posibilidad de acceder a la información de los servicios a través de un endpoint en donde se podrán consultar todos los libros disponibles y poder filtrarlos por el id en donde se visualizará el detalle completo del mismo.

### Requerimiento general 📖 <a name = "requirements"></a>

El requerimiento general que será transversal a todo el desarrollo del será la implementación de todas las funcionalidades básicas para poder **registrar los libros, socios y empleados, poder listarlos y almacenar toda esa información en la base de datos**, las cuales son:

- CRUD de autores, más el listado correspondiente. En el listado se deben visualizar solo los autores activos, y se debe ofrecer la posibilidad de restaurar registros no activos.
- CRUD de libros, más el listado correspondiente. En el listado se deben visualizar solo los libros activos, y se debe ofrecer la posibilidad de restaurar registros no activos. Al crear/actualizar un registro, solo se debe permitir seleccionar autores activos (relación libro-autor).
- CRUD de socios, más el listado correspondiente. En el listado se deben visualizar solo los socios activos, y se debe ofrecer la posibilidad de restaurar registros no activos.
- CRUD de empleados, más el listado correspondiente. En el listado se deben visualizar solo los empleados activos, y se debe ofrecer la posibilidad de restaurar registros no activos.
- CRUD de préstamos de libros, más el listado correspondiente. Al crear/actualizar un registro, solo se debe permitir seleccionar libros/socios/empleados activos.
- API para visualizar todos los libros que la empresa ofrece:
https://localhost:8000/api/libros
- API para visualizar el detalle de un libro:
https://localhost:8000/api/libros/<libro_id>
- Se deben poder visualizar todos los modelos desde el Admin de Django.
- En el Admin permitir realizar búsquedas por nombre de Libro
- En el Admin permitir realizar búsquedas por nombre y apellido para Socio,
Autor y Empleado.
- Documentar el proyecto (archivo README) indicando todo lo que hay que hacer para ponerlo en marcha, además de todas las funcionalidades disponibles.


### Modelo 💾 <a name = "database"></a>
<br>

![modelo](https://drive.google.com/uc?export=view&id=15WpnYT1KBapNUwiOu8AQeY1SiPOBGN91)

### Requerimientos técnicos ⛏️ <a name = "tech_req"></a>
- Framework Django para el desarrollo de la aplicación
- Bases de datos SQLite para almacenar datos
- Utilización del ORM de Django
- Utilizar Jinja2 como sistema de templates
- Uso de Bootstrap para aplicar estilo a los templates.
- Utilizar GitHub como repositorio del código del proyecto
- Documentación del proyecto

## 🏁 Instalación/Ejecución <a name = "getting_started"></a>

Crear entorno virtual

```bash
python -m venv env
```

Activar entorno

```bash
env\Scripts\activate.bat
```

Clonar el repositorio

```bash
git clone git@github.com:Mettralla/WebApp.git
```

Ir al directorio del proyecto

```bash
cd WebApp
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Realizar migraciones

```bash
python manage.py migrate
```

Iniciar server

```bash
python manage.py runserver
```

## 🎈 Vista Previa <a name="preview"></a>

Placeholder

## ⛏️ Tecnologias <a name = "tech_stack"></a>

- Django 4.2.1
- asgiref 3.6.0
- Jinja2 3.1.2
- MarkupSafe 2.1.2
- sqlparse 0.4.4
- tzdata 2023.3

## ✍️ Autores <a name = "authors"></a>
- [Daniel Tejerina](https://github.com/Mettralla)
- [Hernan Fresco](https://github.com/frescoh)
- [Mercedes del Pilar Toledo](https://github.com/PilarToledoMT)
- [Rodrigo Gonza](https://github.com/rodrigonza92)

***
# Api <a name = "title"></a>

## Descripción <a name = "description"></a>

Esta Api permite visualizar todos los autores y libros que la biblioteca ofrece, y además se puede visualizar el detalle de un libro, todo en formato JSON.

## Instalación <a name = "getting_started"></a>

-Crear entorno virtual `python -m venv env`

-Activar entorno `env\Scripts\activate.bat`

-Clonar el repositorio `git clone git@github.com:Mettralla/WebApp.git`

-Ir al directorio del proyecto `cd WebApp`

-Instalar dependencias `pip install -r requirements.txt`

-Realizar migraciones `python manage.py migrate`

## Ejecución <a name = "run_the_app"></a>

-Iniciar server `python manage.py runserver`

## URL de Acceso

<http://127.0.0.1:8000/api>

## Funcionalidades

### Obtener el listado de autores de la BD.

    -Método: GET
    -Request: <http://127.0.0.1:8000/api/autores>
    -Response: 
    HTTP/1.1 200  Se muestra de manera exitosa una respuesta JSON que contiene un listado de autores con sus respectivos detalles.
    Status: 200 OK
    Content-Type: text/html; charset=utf-8

![Listado de autores](https://drive.google.com/uc?export=view&id=1uakMClYRQe4vJszYN2_XJq8JD0ei9qMv)

### Obtener el listado de libros de la BD.

    -Método: GET
    -Request: <http://127.0.0.1:8000/api/libros>
    -Response: 
    HTTP/1.1 200  Se muestra de manera exitosa una respuesta JSON que contiene un listado de libros con sus respectivos detalles.
    Status: 200 OK
    Content-Type: text/html; charset=utf-8

![Listado de libros](https://drive.google.com/uc?export=view&id=1PD09VdREeYkYG5cAop58zjwz3AfcGGBY)

### Obtener un libro del listado de libros de la BD.
    
    -Método: GET
    -Parámetros: id (URL)
    -Request: <http://127.0.0.1:8000/api/libros/libros/<int:id>>
    -Response: 
    HTTP/1.1 200  Se muestra de manera exitosa una respuesta JSON que contiene un libro con sus respectivos detalles.
    Status: 200 OK
    Content-Type: text/html; charset=utf-8

    []

![Libro](https://drive.google.com/uc?export=view&id=1eYBeJZeREvIAPbNG6mpyV1qUTFdxJwxi)
