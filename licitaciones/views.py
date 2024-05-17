from django.shortcuts import render, redirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.forms import inlineformset_factory
from licitaciones.models import Licitacion, LicitacionItem
from licitaciones.forms import LicitacionForm, LicitacionItemForm
from django.contrib import messages
def view_licitaciones(request):
    status = request.GET.get('status')
    if status != None:
        licitaciones = Licitacion.objects.filter(status=status)
        if request.htmx:
            return render(request, "partials/licitaciones_list.html", {'licitaciones': licitaciones, 'status': status})
        else:
            return redirect('/licitaciones/')
    else:
        if request.htmx:
            licitaciones = Licitacion.objects.all()
            return render(request, "licitaciones.html", {'licitaciones': licitaciones})
        else:
            licitaciones = Licitacion.objects.all()
            return render(request, "licitaciones.html", {'licitaciones': licitaciones})


def create_update_lic(request, lic_id=0):
    LicitacionItemFormset = inlineformset_factory(Licitacion, LicitacionItem, form=LicitacionItemForm, extra=1)
    data = {}
    if lic_id != 0:
        lic_instance = get_object_or_404(Licitacion, id=lic_id)
        form = LicitacionForm(instance=lic_instance)
        formset = LicitacionItemFormset(instance=lic_instance)
        data["licitacion"] = lic_instance
    elif lic_id <= 0:
        form = LicitacionForm()
        formset = LicitacionItemFormset()

    data["form"] = form
    data["formset"] = formset

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
                    messages.success(request, "Data updated successfully.")
                    return render(request, "licitaciones_new_form.html", data )
                    # code = HttpResponse.status_code
                    # content = f"Created - Code: {code}"
                    # return HttpResponse(content,content_type="text/plain")
        else:
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
                    return render(request, "partials/licitaciones_new_form.html", data )
                    # code = HttpResponse.status_code
                    # content = f"Edited - Code: {code}"
                    # return HttpResponse(content,content_type="text/plain")
    else:
        return render(request, "partials/licitaciones_new_form.html", data)
