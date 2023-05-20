from django.contrib import admin

from biblioteca.models import Autor,Empleado,Prestamo

class AutorAdmin(admin.ModelAdmin):
    model = Autor
    list_display = ("nombre", "apellido", "nacionalidad", "activo")
    search_fields = ("nombre", "apellido")
    list_filter = ("activo", "nacionalidad")

admin.site.register(Autor, AutorAdmin)
    


class EmpleadoAdmin(admin.ModelAdmin):
    model= Empleado
    list_display = "emp_nombre", "emp_apellido", "emp_legajo"
    search_fields = ("emp_nombre", "emp_apellido", "emp_legajo")
    list_filter = "emp_nombre", "emp_apellido","emp_legajo", "emp_activo"

admin.site.register(Empleado,EmpleadoAdmin)