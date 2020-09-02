from django.urls import path
from .views import *
from .api_views import *


app_name = 'acceso'

urlpatterns = [
    path('', Prueba.as_view(), name="prueba"),
    path('entradas/empleado/', EntradaEmpleadoView.as_view(), name="entrada_empleado"),
    #path('api/accesos/empleado', EntradaSalidaEmpCreateApiView.as_view()),    
    path('entradas/empleado_vehiculo/', EntradaEmpleadoVehiculoView.as_view(), name="entrada_empleado_vehiculo")
]