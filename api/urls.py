from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.listado_libros_endpoint, name='api_listado_libros'),
    path('libros/<int:id>', views.libro_por_id, name='api_libro_por_id'),

    path('autores/', views.listado_autores_endpoint, name='api_listado_autores'),
]