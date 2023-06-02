from django.shortcuts import render, get_object_or_404, redirect
from biblioteca.models import Empleado, Autor, Socio, Libro, Prestamo
from django.http import HttpResponse, JsonResponse
from django.utils import timezone

# Create your views here.

def activar_empleado(request, id):
    """
    Activa un registro de Empleado según el ID proporcionado.

    Parameters:
        request (HttpRequest): La solicitud HTTP recibida.
        id (int): El ID del empleado a activar.

    Returns:
        JsonResponse: Una respuesta JSON con información en caso de fallo.
        Redirect: En caso de exito, activa el empleado y redirige al listado.

    Raises:
        Http404: Si no se encuentra un empleado con el ID especificado.
    """
    empleado = get_object_or_404(Empleado, id=id)

    if empleado.emp_activo:
        response_data = { 
            "status": "info",
            "mensaje": f"El empleado {empleado.emp_nombre} {empleado.emp_apellido} ya esta activo."
        }
        return JsonResponse(response_data)
    else:
        empleado.emp_activo = True
        empleado.save()
        return redirect('listado_empleados')


def desactivar_empleado(request,id):
    """
    Desactiva un registro de empleado

    Args:
        id (int): id del empleado a desactivar

    Returns:
        JsonResponse: Una respuesta JSON con información en caso de fallo.
        Redirect: En caso de exito, desactiva el empleado y redirige al listado
    """
    empleado = get_object_or_404(Empleado, id=id)

    if empleado.emp_activo:
        empleado.emp_activo = False
        empleado.save()
        return redirect('listado_empleados')
    else:
        response_data = { 
            "status": "info",
            "mensaje": f"El empleado {empleado.emp_nombre} {empleado.emp_apellido} ya se encontraba desactivado."
        }
        return JsonResponse(response_data)

def modificar_empleado(request, id):
    """
    Modifica el registro de empleado existente.

    Args:
        id (int): id del empleado a modificar.

    Returns:
        HttpResponse: Una respuesta HTTP que renderiza el formulario para modificar un registro de empleado.
    """
    empleado = Empleado.objects.get(id=id)

    context = {
        "empleado" : empleado
    }

    if request.POST:
        emp_nombre = request.POST["nombre"]
        emp_apellido = request.POST["apellido"]
        emp_legajo = request.POST["legajo"]
        emp_activo = True if request.POST.get("activo") else False

        empleado.emp_nombre = emp_nombre
        empleado.emp_apellido = emp_apellido
        empleado.emp_legajo = emp_legajo
        empleado.emp_activo = emp_activo
        empleado.save()
        return redirect('listado_empleados')

    return render(request, 'biblioteca/empleados/modificar_empleado.html', context)

def listado_empleados(request):
    empleados = Empleado.objects.all()
    context = {
        "empleados" : empleados
    }
    return render(request, 'biblioteca/empleados/listado_empleados.html', context)

def agregar_empleado(request):
    if request.POST:
        emp_nombre = request.POST['nombre']
        emp_apellido = request.POST['apellido']
        emp_legajo = request.POST['legajo']

        Empleado.objects.create(
            emp_nombre = emp_nombre,
			emp_apellido = emp_apellido,
            emp_legajo = emp_legajo,
        )
        return redirect('listado_empleados')
    return render(request, 'biblioteca/empleados/agregar_empleado.html')

# ---------------------------------------------------------------------------
# VIEWS DEL AUTOR
# ---------------------------------------------------------------------------

def modificar_autor(request, id):
    """
    Modifica el registro de un autor existente.

    Parameters:
        request (HttpRequest): La solicitud HTTP recibida.
        id (int): ID del autor a modificar.

    Returns:
        HttpResponse: Redirige al listado de autores o renderiza el formulario para modificar un autor.

    Raises:
        Http404: Si no se encuentra ningún autor con el ID proporcionado en la base de datos.
    """
    autor = get_object_or_404(Autor, id=id)

    if request.POST:
        autor_nombre = request.POST["nombre"]
        autor_apellido = request.POST["apellido"]
        autor_nacionalidad = request.POST["nacionalidad"]
        autor_activo = True if request.POST.get("activo") else False

        autor.nombre = autor_nombre
        autor.apellido = autor_apellido
        autor.nacionalidad = autor_nacionalidad
        autor.activo = autor_activo

        autor.save()

        return redirect('listado_autores')

    return render(request, 'biblioteca/autores/modificar_autor.html', { "autor": autor })

def activar_autor(request, id):
    autor = Autor.objects.get(id=id)
    autor.activo = True
    autor.save()

    return redirect('listado_autores')

def desactivar_autor(request,id):
    """
    Desactiva un registro de autor

    Args:
        id (int): id del autor a desactivar

    Returns:
        JsonResponse: Una respuesta JSON con información en caso de fallo.
        Redirect: En caso de exito, desactiva el autor y redirige al listado
    """
    autor = get_object_or_404(Autor, id=id)

    if autor.activo:
        autor.activo = False
        autor.save()
        return redirect('listado_autores')
    else:
        response_data = { 
            "status": "info",
            "mensaje": f"El autor {autor.nombre} {autor.apellido} ya se encontraba desactivado."
        }
        return JsonResponse(response_data)
    
def agregar_autor(request):
    if request.POST:
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        nacionalidad = request.POST['nacionalidad']

        Autor.objects.create(
            nombre = nombre,
			apellido = apellido,
            nacionalidad = nacionalidad,
        )
        return redirect('listado_autores')
    return render(request, 'biblioteca/autores/agregar_autor.html')    



def listado_autores(request):
    autores= Autor.objects.all()
    context= {'autores':autores}
    return render(request, 'biblioteca/autores/listado_autores.html', context)


# ---------------------------------------------------------------------------
# VIEWS DEL SOCIO
# ---------------------------------------------------------------------------

def agregar_socio(request):
    """
    Agrega un nuevo socio a la base de datos.

    Parameters:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: Redirige al listado de socios o renderiza el formulario para agregar un socio.
    """
    if request.POST:
        socio_nombre = request.POST['nombre']
        socio_apellido = request.POST['apellido']
        socio_nacimiento = request.POST['fecha_nacimiento']

        Socio.objects.create(
            nombre = socio_nombre,
			apellido = socio_apellido,
            fecha_nacimiento = socio_nacimiento
        )
        return redirect('listado_socios')

    return render(request, 'biblioteca/socios/agregar_socio.html')


def listado_socios(request):
    """
    Muestra el listado de todos los socios.

    Returns:
        HttpResponse: Una respuesta HTTP que renderiza el listado de socios.

    """
    socios = Socio.objects.all()
    return render(request, 'biblioteca/socios/listado_socios.html', { "socios": socios })

def desactivar_socio(request, id):
    socio = Socio.objects.get(id=id)
    socio.activo = False
    socio.save()

    #return HttpResponse(f'El socio con ID {id} fue desactivado. ')
    return redirect('listado_socios')

def activar_socio(request, id):
    socio = Socio.objects.get(id=id)
    socio.activo = True
    socio.save()

    #return HttpResponse(f'El socio {socio.nombre} {socio.apellido} con ID: {id} fue activado.')
    return redirect('listado_socios')

def modificar_socio(request, id):
    """
    Modifica/Actualiza el registro de un socio existente.

    Parameters:
        request (HttpRequest): La solicitud HTTP recibida.
        id (int): ID del SOCIO a modificar.

    Returns:
        HttpResponse: Redirige al listado de socios o renderiza el formulario para modificar un socio.

    Raises:
        Http404: Si no se encuentra ningún socio con el ID proporcionado en la base de datos.
    """
    socio = get_object_or_404(Socio, id=id)

    if request.POST:
        socio_nombre = request.POST["nombre"]
        socio_apellido = request.POST["apellido"]
        socio_fecha_nacimiento = request.POST["fecha_nacimiento"]
        socio_activo = True if request.POST.get("activo") else False

        socio.nombre = socio_nombre
        socio.apellido = socio_apellido
        socio.fecha_nacimiento = socio_fecha_nacimiento
        socio.activo = socio_activo

        socio.save()

        return redirect('listado_socios')

    return render(request, 'biblioteca/socios/modificar_socio.html', { "socio": socio })

# ---------------------------------------------------------------------------
# VIEWS DE LIBROS
# ---------------------------------------------------------------------------

def listado_libros(request):
    libros= Libro.objects.all()
    context= {'libros':libros}
    
    return render(request, 'biblioteca/libros/listado_libros.html', context)

def activar_libro(request, id):
    """
    Activa un registro de un Libro según el ID proporcionado.

    Parameters:
        request (HttpRequest): La solicitud HTTP recibida.
        id (int): El ID del LIBRO a activar.

    Returns:
        JsonResponse: Una respuesta JSON con información en caso de fallo.
        
    Raises:
        Http404: Si no se encuentra un Libro con el ID especificado.
    """
    libro = get_object_or_404(Libro, id=id)
    libro.lib_activo = True
    libro.save()
    return redirect('listado_libros')

def desactivar_libro(request, id):
    """
    Desactiva un Libro según el ID proporcionado.

    Parameters:
        request (HttpRequest): La solicitud HTTP recibida.
        id (int): El ID del Libro a desactivar.

    Returns:
        JsonResponse: Una respuesta JSON con un mensaje de exito o de informacion en caso contrario.

    Raises:
        Http404: Si no se encuentra un Libro con el ID especificado.
    """
    libro = get_object_or_404(Libro, id = id)
    libro.lib_activo = False
    libro.save()
    return redirect('listado_libros')


def modificar_libro(request, id):
    """
    Modifica el registro de un libro existente.

    Parameters:
        request (HttpRequest): La solicitud HTTP recibida.
        id (int): ID del libro a modificar.

    Returns:
        HttpResponse: Redirige al listado de libros o renderiza el formulario para modificar un libro.

    Raises:
        Http404: Si no se encuentra ningún libro con el ID proporcionado en la base de datos.
    """
    libro = get_object_or_404(Libro, id=id)

    if request.POST:
        libro_titulo = request.POST["titulo"]
        libro_descripcion = request.POST["descripcion"]
        libro_isbn = request.POST["isbn"]
        libro_autor = request.POST["autor"]
        libro_activo = True if request.POST.get("activo") else False

        libro.lib_titulo = libro_titulo
        libro.lib_descripcion = libro_descripcion
        libro.lib_isbn = libro_isbn
        libro.lib_autor__id = libro_autor
        libro.lib_activo = libro_activo

        libro.save()

        return redirect('listado_libros')

    return render(request, 'biblioteca/libros/modificar_libro.html', {"libro": libro})

def agregar_libro(request):
    """
    Agrega un nuevo libro a la base de datos.

    Parameters:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: Redirige al listado de socios o renderiza el formulario para agregar un socio.
    """
    autores = Autor.objects.all()
    context= {
        'autores':autores
    }
    if request.POST:
        titulo = request.POST['titulo']
        descripcion  = request.POST['descripcion']
        isbn = request.POST['isbn']
        autor_id= request.POST['autor']

        Libro.objects.create(
            lib_titulo = titulo,
			lib_descripcion = descripcion,
            lib_isbn = isbn,
            lib_autor_id=autor_id
        )
        return redirect('listado_libros')

    return render(request, 'biblioteca/libros/agregar_libro.html',context)

# ---------------------------------------------------------------------------
# VIEWS DE PRESTAMOS
# ---------------------------------------------------------------------------

def agregar_prestamo(request):
    """
    Agrega un nuevo prestamo a la base de datos.

    Muestra el formulario de agregar prestamo con los socios activos, libros disponibles y empleados activos.
    Si se realiza una solicitud POST con los datos del prestamo, se crea un nuevo registro de prestamo.

    Parameters:
        request (HttpRequest): La solicitud HTTP recibida.

    Returns:
        HttpResponse: Respuesta HTTP que muestra el formulario de agregar préstamo o redirecciona al listado.

    """

    # Se filtran los registros para enviar solo objetos activos
    socios_activos = Socio.objects.filter(activo=True)
    libros_disponibles = Libro.objects.filter(lib_activo=True)
    empleados_activos = Empleado.objects.filter(emp_activo= True)

    context = {
        'socios': socios_activos,
        'libros': libros_disponibles,
        'empleados': empleados_activos
    }

    if request.method == 'POST':
        socio_id = request.POST.get('socio')
        libro_id = request.POST.get('libro')
        empleado_id = request.POST.get('empleado')

        prestamo = Prestamo()

        prestamo.pres_fecha = timezone.now()
        prestamo.pres_devolucion = prestamo.pres_fecha + timezone.timedelta(days=2)
        prestamo.socio = socio_id
        prestamo.libro = libro_id
        prestamo.empleado = empleado_id

        # Se guarda el registro de prestamo creado.
        prestamo.save()

        # Se desactiva el libro prestado hasta que se lo regrese.
        libro_prestado = get_object_or_404(Libro, id = libro_id)
        libro_prestado.lib_activo = False
        libro_prestado.save()
        
        # Se redirecciona hacia el listado
        # return redirect('listado_prestamos') -> Redireccionar a listado_prestamos durante el linkeado

    return render(request, 'biblioteca/prestamos/agregar_prestamo.html', context)

""" 
    View que permite Eliminar un registro de Préstamo de Libro

    Return:
        HttpResponse --> muestra un mensaje que indica que el prestamo fue eliminado
"""
def eliminar_prestamo(request, id):
    prestamo = Prestamo.objects.get(id=id)

    #Se recupera el ID del libro prestado para posteriormente activarlo
    libro = Libro.objects.get(id=prestamo.libro.id)

    #Se borra el registro del prestamo
    prestamo.delete()

    #Se activa el libro prestado
    libro.lib_activo = True
    libro.save()

    return HttpResponse(f'El prestamo con ID {id} fue eliminado.')

def listado_prestamos(request):
    """
    Muestra el listado de todos los prestamos.

    Returns:
        HttpResponse: Una respuesta HTTP que renderiza el listado de prestamos.

    """
    prestamos = Prestamo.objects.all()
    return render(request, 'biblioteca/prestamos/listado_prestamos.html', { "prestamos": prestamos })