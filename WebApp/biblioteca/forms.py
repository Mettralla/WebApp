from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ["emp_nombre", "emp_apellido", "emp_legajo"]
