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