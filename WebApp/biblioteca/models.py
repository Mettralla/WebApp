from django.db import models

# Create your models here.

class Autor(models.Model):
    """
    Modelo que representa a un autor.

    Este modelo se utiliza para almacenar información sobre los autores de los libros.
    Los autores tienen un nombre, apellido y nacionalidad, y se puede indicar si están activos o no.
    """
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Socio(models.Model):
    """
    Modelo que representa a un socio.

    Este modelo se utiliza para almacenar información sobre los socios de la biblioteca.
    Los socios tienen un nombre, apellido, una fecha de naciemiento, y se puede indicar si están activos o no.
    """
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(auto_now=False) 
    activo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

# class Libro(models.Model):
#     """
#     Modelo que representa a un Libro.

#     Este modelo se utiliza para almacenar información sobre los libros de la biblioteca.
#     Los libros tienen un titulo, una descripcion, un isbn, un autor y se puede indicar si están activos o no.
#     """
#     titulo = models.CharField(max_length=100)
#     descripcion = models.CharField(max_length=100)
#     isbn = models.IntegerField(max_length=13) #El isbn es un standard numero de 13 cifras que identifica a cada libro en el mundo
#     autor = models.CharField(max_length=100) 
#     activo = models.BooleanField(default=True)

#     def __str__(self) -> str:
#         return f"Titulo: {self.titulo} - Autor: {self.autor} - ISBN: {self.isbn} - Descripcion: {self.descripcion} - Activo: {self.activo}"

class Empleado(models.Model):
    """Modelo Empleado, donde se alamacenaran los datos de cada empleado de la bibliteca
    """
    emp_nombre= models.CharField(max_length=100)
    emp_apellido= models.CharField(max_length=50)
    emp_legajo= models.models.IntegerField()
    emp_activo= models.models.models.BooleanField(default=True)


    