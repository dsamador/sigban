from rest_framework.generics import (CreateAPIView, )
from .serializers import (
    EntradaSalidaEmpSerializer, EntradaVisitasSerializer,

    )

class EntradaVistitanteCreateAPIView(CreateAPIView):
    
    serializer_class = EntradaVisitasSerializer