from django.contrib import admin

from biblioteca.models import Autor, Empleado,Libro,Prestamo, Socio

class AutorAdmin(admin.ModelAdmin):
    model = Autor
    list_display = ("nombre", "apellido", "nacionalidad", "activo")
    search_fields = ("nombre", "apellido")
    list_filter = ("activo", "nacionalidad")

admin.site.register(Autor, AutorAdmin)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    """Clase que define la configuración personalizada del panel de administración para el modelo Empleado."""
    list_display = ["emp_nombre", "emp_apellido", "emp_legajo", "emp_activo"]
    search_fields = ["emp_nombre", "emp_apellido"]
    list_filter = ["emp_activo"]

class LibroAdmin(admin.ModelAdmin):
    """Configura los parametros con los que se va a mostrar un libro en el admin
    """
    model=Libro
    list_display = "lib_titulo","lib_autor","lib_descripcion","lib_isbn","lib_activo"
    search_fields = "lib_titulo","lib_descripcion","lib_isbn","lib_activo","lib_autor__nombre","lib_autor__apellido","lib_autor__nacionalidad"
    list_filter = "lib_activo","lib_autor__nombre","lib_autor__apellido","lib_autor__nacionalidad"
    

class PrestamoAdmin(admin.ModelAdmin):
    """Configura los parametros con los que se va a mostrar un Prestamo en el admin
    """
    model= Prestamo
    list_display= 'pres_fecha','pres_devolucion','socio','libro','empleado'
    search_fields= 'pres_fecha','pres_devolucion','socio__nombre','socio__apellido','libro__lib_titulo',
    'libro__lib_isbn','libro__lib_autor__nombre','libro__lib_autor__apellido','libro__lib_autor__nacionalidad',
    'empleado__emp_nombre','empleado__emp_apellido','empleado__emp_legajo'
    list_filter= 'pres_fecha','pres_devolucion'

class SocioAdmin(admin.ModelAdmin):
    model = Socio
    list_display = ("nombre", "apellido", "fecha_nacimiento", "activo")
    search_fields = ("nombre", "apellido",)
    list_filter = ("activo",)

admin.site.register(Socio,SocioAdmin)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Prestamo,PrestamoAdmin)