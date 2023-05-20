from django.contrib import admin

from biblioteca.models import Autor, Empleado

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