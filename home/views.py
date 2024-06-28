from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def panel(request):
    return render(request, "panel.html", {})

def buscador(request):
    return render(request, "buscador.html", {})

def ofertantes(request):
    return render(request, "ofertantes.html", {})
