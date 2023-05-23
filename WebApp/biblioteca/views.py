from django.shortcuts import render, get_object_or_404, redirect
from .models import Empleado
from django.http import JsonResponse

# Create your views here.

def activar_empleado(request, id):
    """
    Activa un registro de Empleado según el ID proporcionado.

    Parameters:
        request (HttpRequest): La solicitud HTTP recibida.
        id (int): El ID del empleado a activar.

    Returns:
        JsonResponse: Una respuesta JSON con un mensaje de éxito o información.

    Raises:
        Http404: Si no se encuentra un empleado con el ID especificado.
    """
    empleado = get_object_or_404(Empleado, id=id)

    if empleado.emp_activo:
        response_data = { 
            "status": "info",
            "mensaje": f"El empleado {empleado.emp_nombre} {empleado.emp_apellido} ya esta activo."
        }
    else:
        empleado.emp_activo = True
        empleado.save()
        response_data = { 
            "status": "success",
            "mensaje": f"El empleado {empleado.emp_nombre} {empleado.emp_apellido} ha sido activado."
        }

    # Mas adelante redireccionaremos hacia la lista de empleados
    # return redirect('lista_empleados')
    # Por ahora regresara un mensaje en formato JSON
    return JsonResponse(response_data)

def desactivar_empleado(request,id):
    """
    Desactiva un registro de empleado

    Args:
        id (int): id del empleado a desactivar

    Returns:
        JSON: Mensaje de salida
    """
    empleado = get_object_or_404(Empleado, id=id)

    if empleado.emp_activo:
        empleado.emp_activo = False
        empleado.save()
        response_data = { 
            "status": "success",
            "mensaje": f"El empleado {empleado.emp_nombre} {empleado.emp_apellido} ha sido desactivado con éxito."
        }
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
        emp_activo = request.POST["activo"]

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
            #activo = True,
        )
        return redirect('listado_empleados')
    return render(request, 'biblioteca/agregar_empleado.html')