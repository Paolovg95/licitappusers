from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.forms import inlineformset_factory
from licitaciones.models import Licitacion, LicitacionItem
from licitaciones.forms import LicitacionForm, LicitacionItemForm
from django.contrib import messages
def read_licitaciones(request):
    status = request.GET.get('status')
    if status != None:
        licitaciones = Licitacion.objects.filter(status=status)
        if request.htmx:
            return render(request, "partials/read_licitaciones_status.html", {'licitaciones': licitaciones, 'status': status})
        else:
            return redirect('/licitaciones/')
    else:
        if request.htmx:
            licitaciones = Licitacion.objects.all()
            return render(request, "read_licitaciones.html", {'licitaciones': licitaciones})
        else:
            licitaciones = Licitacion.objects.all()
            return render(request, "read_licitaciones.html", {'licitaciones': licitaciones})

def create_update_lic(request, lic_id=0):
    LicitacionItemFormset = inlineformset_factory(Licitacion, LicitacionItem, form=LicitacionItemForm, extra=1)
    data = {}
    if request.method == 'GET':
        if lic_id != 0:
            lic_instance = get_object_or_404(Licitacion, id=lic_id)
            url = reverse('update_licitaciones', kwargs={'lic_id': lic_instance.id })
            form = LicitacionForm(instance=lic_instance)
            formset = LicitacionItemFormset(instance=lic_instance)
            data["licitacion"] = lic_instance
        elif lic_id <= 0:
            url = reverse('create_licitaciones')
            form = LicitacionForm()
            formset = LicitacionItemFormset()
        data["url"] = url
        data["form"] = form
        data["formset"] = formset
        return render(request, "create_licitaciones_form.html", data)

    if request.method == "POST":
        if lic_id == 0:
            form = LicitacionForm(request.POST)
            if form.is_valid():
                lic = form.save(commit=False)
                lic.save()
                formset = LicitacionItemFormset(request.POST, instance=lic)
                if formset.is_valid():
                    formset.save()
                    data['form'] = form
                    data['formset'] = formset
                    messages.success(request, "Data created successfully.")
                    return render(request, "partials/toast.html", data)
        else:
            lic_instance = get_object_or_404(Licitacion, id=lic_id)
            data["licitacion"] = lic_instance
            form = LicitacionForm(request.POST, instance=lic_instance)
            formset = LicitacionItemFormset(request.POST, instance=lic_instance)
            if form.is_valid():
                lic = form.save(commit=False)
                lic.save()
                if formset.is_valid():
                    formset.save()
                    data['form'] = form
                    data['formset'] = formset
                    messages.success(request, "Data updated successfully.")
                    return render(request, "partials/toast.html", data)
