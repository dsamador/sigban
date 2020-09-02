from django.urls import path
from .views import (Prueba, EntradaEmpleadoView, EntradaSalidaEmpCreateApiView,)
from .api_views import *


app_name = 'acceso'

urlpatterns = [
    path('', Prueba.as_view(), name="prueba"),
    path('entradas/empleado/', EntradaEmpleadoView.as_view(), name="entrada_empleado"),
    #path('api/accesos/empleado', EntradaSalidaEmpCreateApiView.as_view()),    
    
]