from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import (CreateAPIView, )
from .serializers import EntradaSalidaEmpSerializer
from .models import EntradaSalidaEmp
# Create your views here.

    
class Prueba(TemplateView):
    template_name = "prueba.html"

class EntradaEmpleadoView(TemplateView):
    template_name = "entrada_salida/entradas_empleado.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Entradas'                        
        return context         

    
class EntradaSalidaEmpCreateApiView(CreateAPIView):
    serializer_class = EntradaSalidaEmpSerializer
    

    
        
