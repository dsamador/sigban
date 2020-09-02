from .models import (
    EntradaSalidaEmp, EntradaSalidaVisitas,
    )
from rest_framework import serializers


class EntradaSalidaEmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntradaSalidaEmp
        fields = ('__all__')



""" Serializador para crear una entrada de visita """
#Cuando se va a crear un serializador que nos permite insertar datos a la bd
#no es necesario usar ModelSerializer
class EntradaVisitasSerializer(serializers.Serializer):
    pass