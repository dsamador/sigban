from django import forms
from .models import *

class EntradaEmpForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super(EntradaEmpForm, self).__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control mb-2'
        
        self.fields['empleado'].widget.attrs['autofocus'] = True

        self.fields['empleado'].queryset = Empleados.objects.filter(finca=Finca)
              
        self.fields['tipo'].empty_label = "Seleccione un tipo vehículo"
        self.fields['marca'].empty_label = "Seleccione una marca"

    class Meta:
        model = EntradaSalidaEmp
        exclude = ['hora_salida','detalle_salida','finca','estado','usuario','fecha_creacion','tipo_tabla']



