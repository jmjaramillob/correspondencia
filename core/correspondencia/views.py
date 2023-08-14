from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from core.correspondencia.models import Correspondencia
from django.views.generic import TemplateView, CreateView, FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from core.correspondencia.forms import EntradaForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

#@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = "index.html"


class EntradaView(FormView):
    model = Correspondencia
    form_class = EntradaForm
    template_name = "entrada.html"
    #success_url = "/correspondencia/"

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.SUCCESS, 'Entrada registrada'
        )
        return super(EntradaView, self).form_valid(form)

class SalidaView(FormView):
    model = Correspondencia
    template_name = "salida.html"
    form_class = EntradaForm
    #success_url = "/correspondencia/"

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.SUCCESS, 'Salida registrada'
        )
        return super(SalidaView, self).form_valid(form)

    
class ArchivoView(FormView):
    model = Correspondencia
    template_name = "archivo.html"
    form_class = EntradaForm

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.SUCCESS, 'Salida registrada'
        )
        return super(ArchivoView, self).form_valid(form)

class DeleteView(DeleteView):
    model = Correspondencia
    success_url = reverse_lazy('index')