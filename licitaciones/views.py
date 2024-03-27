from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from licitaciones.models import Licitacion
from licitaciones.forms import LicitacionForm
# Create your views here.

def create_update_lic(request, lic_id=0):
    if request.method == "GET":
        if lic_id == 0:
            form = LicitacionForm()
        else:
            lic_instance = get_object_or_404(Licitacion, id=lic_id)
            form = LicitacionForm(instance=lic_instance)
    else:
        if lic_id == 0:
            form = LicitacionForm(request.POST)
            if form.is_valid():
                lic = form.save(commit=False)
                lic.save()
            return redirect("/")
        else:
            lic_instance = get_object_or_404(Licitacion, id=lic_id)
            form = LicitacionForm(request.POST, instance=lic_instance)
            if form.is_valid():
                lic = form.save(commit=False)
                lic.save()
            return redirect("/")
    data = {
        "form": form
    }
    return render(request, "create_lic.html", data)
