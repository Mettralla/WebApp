from django.contrib import admin
from .models import Autor, Empleado

# Register your models here.

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    """Clase que define la configuración personalizada del panel de administración para el modelo Empleado."""
    list_display = ["nombre", "apellido", "numero_legajo", "activo"]
    search_fields = ["nombre", "apellido"]
    list_filter = ["activo"]