from django.contrib import messages

from core.correspondencia.models import Correspondencia
from django.views.generic import TemplateView, CreateView, FormView
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
            self.request, messages.SUCCESS, 'Correpondencia registrada'
        )
        return super(EntradaView, self).form_valid(form)
