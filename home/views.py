from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import inlineformset_factory

from licitaciones.models import Licitacion, LicitacionItem
from licitaciones.forms import LicitacionForm, LicitacionItemForm
from licitaciones.models import Licitacion

def panel(request):
    if request.htmx:
        return render(request,"partials/panel/panel_partial.html",{})
    else:
        return render(request, "home/panel.html", {})
def buscador(request):
    if request.htmx:
        licitaciones = Licitacion.objects.all()
        return render(request,"partials/buscador/buscador_partial.html", {"licitaciones": licitaciones},
        )
    else:
        licitaciones = Licitacion.objects.all()
        return render(request, "home/buscador.html", {"licitaciones": licitaciones})
def ofertantes(request):
    return render(request, "home/ofertantes.html", {})
