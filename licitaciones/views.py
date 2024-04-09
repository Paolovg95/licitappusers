from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.forms import inlineformset_factory
from licitaciones.models import Licitacion, LicitacionItem
from licitaciones.forms import LicitacionForm, LicitacionItemForm
# Create your views here.

def create_lic_item(request):
    data = {}
    lic_instance = Licitacion.objects.get(id=21)
    LicitacionItemFormset = inlineformset_factory(Licitacion, LicitacionItem, form=LicitacionItemForm, extra=1)
    formset = LicitacionItemFormset()
    if request.method == 'POST':
        formset = LicitacionItemFormset(request.POST, instance=lic_instance)
        if formset.is_valid():
            formset.save()
            code = HttpResponse.status_code
            content = f"Created {code}"
            return HttpResponse(content,content_type="text/plain")
        else:
            print(formset.error_messages)
            content = f"Not Created"
            return HttpResponse(content,content_type="text/plain")
    data['formset'] = formset
    return render(request, "create_lic_item.html", data)

def add_lic_item(request):
    LicitacionItemFormset = inlineformset_factory(Licitacion, LicitacionItem, form=LicitacionItemForm, extra=1)
    # count = "0"
    formset = LicitacionItemFormset()
    return render(request, "partials/add_lic_item.html", {'formset': formset})


def create_update_lic(request, lic_id=0):
    data = {}
    if request.method == "GET":
        if lic_id == 0:
            form = LicitacionForm()
            # form_item = LicitacionItemForm()
        else:
            lic_instance = get_object_or_404(Licitacion, id=lic_id)
            form = LicitacionForm(instance=lic_instance)
            data["licitacion"] = lic_instance
    else:
        if lic_id == 0:
            form = LicitacionForm(request.POST)
            # form_item = LicitacionItemForm(request.POST)
            if form.is_valid():
                lic = form.save(commit=False)
                lic.save()
                code = HttpResponse.status_code
                content = f"Created - Code: {code}"
                return HttpResponse(content,content_type="text/plain")
                # print(f"LIC: {lic}")
                # print(form_item.errors)
                # if form_item.is_valid():
                #     item = form_item.save(commit=False)
                #     print(f"ITEM{item}")
                #     item.licitacion = lic
                #     item.save()
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
    # data["form_item"] = form_item
    return render(request, "create_lic.html", data)
