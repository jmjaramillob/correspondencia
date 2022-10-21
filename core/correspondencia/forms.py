from socket import fromshare
from django import forms

class EntradaForm(forms.Form):

    fields = ['radicado', 'recibido_de', 'fecha_recibido', 'asunto', 'numero_folios', 'firmado_por', 'cargo_firmante', 'enviado_a', 'fecha_envio', 'almacenado_AZ', 'observaciones', 'entrada']
    labels = []