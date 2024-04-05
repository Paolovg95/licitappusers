from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import get_object_or_404
from .forms import LicitacionItemFormSet
from licitaciones.models import Licitacion, LicitacionItem
from licitaciones.forms import LicitacionForm, LicitacionItemForm
# Create your views here.

def create_lic_item(request):
    data = {}
    if request.method == 'POST':
        lic_instance = Licitacion.objects.get(id=1)
        formset = LicitacionItemFormSet(request.POST, instance=lic_instance)
        data['formset'] = formset
        if formset.is_valid():
            formset.save()
            code = HttpResponse.status_code
            content = f"Created {code}"
            return HttpResponse(content,content_type="text/plain")
        else:
            print(formset.error_messages)
            content = f"Not Created"
            return HttpResponse(content,content_type="text/plain")

    else:
        formset = LicitacionItemFormSet()
        data['formset'] = formset
    return render(request, "lic_item_create.html", data)

def add_lic_item(request):
    data = {}
    data['formset'] = LicitacionItemFormSet()
    return render(request, "partials/lic_item_add.html", data)


def create_update_lic(request, lic_id=0):
    data = {}
    if request.method == "GET":
        if lic_id == 0:
            form = LicitacionForm()
            data['formset'] = LicitacionItemFormSet()
        else:
            lic_instance = get_object_or_404(Licitacion, id=lic_id)
            form = LicitacionForm(instance=lic_instance)
            data["licitacion"] = lic_instance
    else:
        if lic_id == 0:
            form = LicitacionForm(request.POST)
            if form.is_valid():
                lic = form.save(commit=False)
                lic.save()
                code = HttpResponse.status_code
                content = f"Created - Code: {code}"
                return HttpResponse(content,content_type="text/plain")
        else:
            lic_instance = get_object_or_404(Licitacion, id=lic_id)
            form = LicitacionForm(request.POST, instance=lic_instance)
            data["licitacion"] = lic_instance
            if form.is_valid():
                lic = form.save(commit=False)
                lic.save()
                code = HttpResponse.status_code
                content = f"Edited - Code: {code}"
                return HttpResponse(content,content_type="text/plain")
    data["form"] = form
    return render(request, "create_lic.html", data)
