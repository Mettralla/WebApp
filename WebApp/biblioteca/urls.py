from django.urls import path
from . import views

urlpatterns = [
    path('empleados/activar/<int:id>/', views.activar_empleado, name='activar_empleado'),
    path('empleados/desactivar/<int:id>', views.desactivar_empleado, name='desactivar_empleado'),
    path('empleados/modificar/<int:id>', views.modificar_empleado, name='modificar_empleado')
]