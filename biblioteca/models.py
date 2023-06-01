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

class Libro(models.Model):
    """
    Modelo que representa a un Libro.

    Este modelo se utiliza para almacenar información sobre los libros de la biblioteca.
    Los libros tienen un titulo, una descripcion, un isbn, un autor y se puede indicar si están activos o no.
    """
    lib_titulo = models.CharField(max_length=100, verbose_name='Titulo')
    lib_descripcion = models.CharField(max_length=100, verbose_name='Descripcion')
    lib_isbn = models.IntegerField(verbose_name='ISBN') #El isbn es un standard numero de 13 cifras que identifica a cada libro en el mundo
    lib_autor = models.ForeignKey(
        Autor, 
        related_name='autores',
        on_delete=models.CASCADE,
        verbose_name='Autor',
    ) 
    lib_activo = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self) -> str:
        return f"{self.lib_titulo}"

class Empleado(models.Model):
    """Modelo Empleado, donde se alamacenaran los datos de cada empleado de la bibliteca
    """
    emp_nombre= models.CharField(max_length=100,verbose_name='Nombre')
    emp_apellido= models.CharField(max_length=50,verbose_name='Apellido')
    emp_legajo= models.IntegerField(verbose_name='Legajo')
    emp_activo= models.BooleanField(default=True,verbose_name='Activo')
    
    def __str__(self):
        return f"{self.emp_nombre} {self.emp_apellido}"

class Prestamo(models.Model):
    """Modelo Prestamo, donde se registran los prestamos que se realizan a los socios"""
    pres_fecha= models.DateTimeField(verbose_name='Fecha de préstamo') # DateTimeField porque el plazo está expresado en horas
    pres_devolucion= models.DateTimeField(verbose_name='Fecha de devolución',null=True) # DateTimeField porque el plazo está expresado en horas
    socio= models.ForeignKey(Socio,
                             related_name='prestamos',
                             on_delete=models.PROTECT) 
    # Protect evita que se elimine un socio si existe un prestamo asiado a él
    libro= models.ForeignKey(Libro,
                             related_name='libros',
                             on_delete=models.PROTECT)
    # Protect evita que se elimine un Libro si existe un prestamo asiado a él
    
    empleado= models.ForeignKey(Empleado,
                                related_name='prestamos_realizados',
                                on_delete=models.PROTECT)
    
    # Protect evita que se elimine un Empleado si existe un prestamo asiado a él
    
    # Para eliminar un socio o un Empleado, primero deberiamos eliminar todos los prestamos asociados 
    # a ellos. Esto evitaria eliminar un presatamo activo al eliminar una clave foranea
    
    def __str__(self):
        return f"""
    Libro solicitado: {self.libro}
    Fecha de prestado: {self.pres_fecha}
    Devuelto: {self.pres_devolucion}
    
    Prestado a: {self.socio}
    Autorizado por: {self.empleado}"""