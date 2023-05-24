from django.urls import path
from . import views

urlpatterns = [
    path('empleados/activar/<int:id>/', views.activar_empleado, name='activar_empleado'),
    path('empleados/desactivar/<int:id>', views.desactivar_empleado, name='desactivar_empleado'),
    path('empleados/modificar/<int:id>', views.modificar_empleado, name='modificar_empleado'),
    path('empleados/listado', views.listado_empleados, name='listado_empleados'),
    path('empleados/crear', views.agregar_empleado, name='crear_empleado'),

    path('autores/modificar/<int:id>', views.modificar_autor, name="modificar_autor"),

    path('socios/nuevo', views.agregar_socio, name='crear_socio'),
    path('socios/listado', views.listado_socios, name='listado_socios'),
]