from django.shortcuts import render
from licitaciones.models import Licitacion


# Create your views here.
def home(request):
    return render(request, "home.html", {})


def panel(request):
    return render(request, "panel.html", {})


def buscador(request):
    licitaciones = Licitacion.objects.all()
    return render(request, "buscador.html", {"licitaciones": licitaciones})


def ofertantes(request):
    return render(request, "ofertantes.html", {})
