from django.shortcuts import render, get_object_or_404, redirect
from .models import Empleado, Autor
from django.http import JsonResponse

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

    return render(request, 'biblioteca/modificar_empleado.html', context)

def listado_empleados(request):
    empleados = Empleado.objects.all()
    context = {
        "empleados" : empleados
    }
    return render(request, 'biblioteca/listado_empleados.html', context)

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
    return render(request, 'biblioteca/agregar_empleado.html')

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

    return render(request, 'biblioteca/modificar_autor.html', { "autor": autor })

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

        Autor.objects.create(
            nombre = socio_nombre,
			apellido = socio_apellido,
            fecha_nacimiento = socio_nacimiento,
        )
        return redirect('listado_autores')

    return render(request, 'biblioteca/agregar_autor.html')