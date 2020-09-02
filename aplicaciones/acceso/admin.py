from django.contrib import admin
from .models import *

# Register your models here.

class TipoTablaAdmin(admin.ModelAdmin):
	list_display  = ('id','tipo')



admin.site.register(TipoTabla,TipoTablaAdmin)
admin.site.register(Empresas)
admin.site.register(Fincas)
admin.site.register(Cargos)
admin.site.register(TipoEmpleado)
admin.site.register(Empleados)
admin.site.register(Color)
admin.site.register(SemanaAnio)
admin.site.register(EntradaSalidaEmp)
admin.site.register(Programacion)
admin.site.register(Labores)
admin.site.register(Procesos)
admin.site.register(DetalleProgramacion)
admin.site.register(FuncionesEmpleados)
admin.site.register(FuncionesXEmpleados)
admin.site.register(Visitantes)
admin.site.register(EntradaSalidaVisitas)
admin.site.register(EntradaVehiculos)
