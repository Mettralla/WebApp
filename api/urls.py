from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.listado_libros_endpoint, name='api_listado_libros'),
]