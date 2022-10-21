from django.conf.urls import url
from core.correspondencia.views import IndexView, EntradaView

urlpatterns = [
    url('inicio/', IndexView.as_view(), name="index"),
    url('entrada/', EntradaView.as_view(), name="entrada"),
]