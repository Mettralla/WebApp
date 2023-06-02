from django.forms import model_to_dict
from django.shortcuts import get_object_or_404, render
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

def libro_por_id(request, id):
    """
    Endpoint para visualizar un libro a traves de su id.
    
    Returns:
        JsonResponse: Una respuesta JSON que contiene los detalles del libro seleccionado.
    """
    libro = get_object_or_404(Libro, id=id)
    data = []
    data.append(
        {'id': libro.id,
        'titulo': libro.lib_titulo,
        'descripcion':libro.lib_descripcion,
        'autor': f'{ libro.lib_autor.nombre } { libro.lib_autor.apellido}'})
    return JsonResponse(data, safe=False)