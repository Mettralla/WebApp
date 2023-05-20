from django.contrib import admin

from biblioteca.models import Autor

class AutorAdmin(admin.ModelAdmin):
    model = Autor
    list_display = ("nombre", "apellido", "nacionalidad", "activo")
    search_fields = ("nombre", "apellido")
    list_filter = ("activo", "nacionalidad")

admin.site.register(Autor, AutorAdmin)
    


