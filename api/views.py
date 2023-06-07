from django.http import JsonResponse
from biblioteca.models import Libro, Autor

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
    try:
        libro = Libro.objects.get(id=id)
    except Libro.DoesNotExist:
        return JsonResponse([], safe=False)

    data = [
        {
            'id': libro.id,
            'titulo': libro.lib_titulo,
            'descripcion':libro.lib_descripcion,
            'autor': f'{ libro.lib_autor.nombre } { libro.lib_autor.apellido}'
        }
    ]

    return JsonResponse(data, safe=False)

# ---------------------------------------------------------------------------
# VIEWS DEL AUTOR
# ---------------------------------------------------------------------------

def listado_autores_endpoint(request):
    """
    Endpoint para obtener un listado de autores.

    Args:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        JsonResponse: Una respuesta JSON que contiene un listado de autores con sus respectivos detalles.
    """
    autores = Autor.objects.all()
    data = []

    for autor in autores:
        data.append(
            {
                'id': autor.id,
                'nombre': autor.nombre,
                'apellido': autor.apellido,
                'nacionalidad': autor.nacionalidad,
                'activo': autor.activo
            }
        )

    return JsonResponse(data, safe=False)