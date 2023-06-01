from django.shortcuts import render
from django.http import JsonResponse
from biblioteca.models import Libro

# Create your views here.

def listado_libros_endpoint(request):
    """
    Endpoint para obtener un listado  de libros.
    
    Args:
        request (HttpRequest): La solicitud HTTP recibida.
    
    Returns:
        JsonResponse: Una respuesta JSON que contiene un listado de libros con sus respectivos detalles.
    """
    libros = Libro.objects.all()
    data = []
    
    for libro in libros:
        data.append(
            {
                'id': libro.id,
                'titulo': libro.lib_titulo,
                'autor': f'{ libro.lib_autor.nombre } { libro.lib_autor.apellido}'
            }
        )
    
    return JsonResponse(data, safe=False)
