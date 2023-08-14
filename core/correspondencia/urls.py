from django.urls import path
from core.correspondencia.views import *

urlpatterns = [
    path('inicio/', IndexView.as_view(), name="index"),
    path('entrada/', EntradaView.as_view(), name="entrada"),
    path('salida/', SalidaView.as_view(), name="salida"),
    path('archivo/', ArchivoView.as_view(), name="archivo"),
]