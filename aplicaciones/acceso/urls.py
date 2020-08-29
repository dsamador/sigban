from django.urls import path
from .views import *

app_name = 'acceso'

urlpatterns = [
    path('', Prueba.as_view(), name="prueba"),
]