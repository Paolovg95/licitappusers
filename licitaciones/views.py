import urllib
from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.forms import inlineformset_factory
from licitaciones.models import Licitacion, LicitacionItem
from licitaciones.forms import LicitacionForm, LicitacionItemForm

def save_licitacion(request):
    LicitacionItemFormset = inlineformset_factory(
        Licitacion, LicitacionItem, form=LicitacionItemForm, extra=2
    )
    if request.method == "POST":
        # CREATE AND SAVE LICITACION
        form = LicitacionForm(request.POST)
        formset = LicitacionItemFormset(request.POST)
        if request.POST["form_id"] == "items":
            if form.is_valid():
                lic = form.save(commit=False)
                lic.save()
                formset = LicitacionItemFormset(request.POST, instance=lic)
                if formset.is_valid():
                    formset = formset.save(commit=False)
                    formset.save()
        return redirect("licitaciones")
def read_licitaciones(request):
    print(request.headers.get("Hx-Trigger-Name"))
    status = request.GET.get("status")
    search_text = request.GET.get("search_text", "")  #1
    if request.headers.get("Hx-Trigger-Name") == 'search_text':
        if len(search_text) != 0:
            search_text = urllib.parse.unquote(search_text) #2
            search_text = search_text.strip()
            licitaciones = []
            if search_text:
                parts = search_text.split()  #3
                q = Q(title__icontains=parts[0])
                for part in parts[1:]: #5
                    q |= Q(title__icontains=part) #6
                licitaciones = Licitacion.objects.filter(q)  #7
            data = {
                "search_text": search_text,
                "licitaciones": licitaciones,
            }
            return render(request, "partials/licitaciones/components/table_licitaciones.html", data)
        else:
            licitaciones = Licitacion.objects.all()
            return render(
                request,
                "partials/licitaciones/components/table_licitaciones.html",
                {"licitaciones": licitaciones},
            )
    if status != None:
        licitaciones = Licitacion.objects.filter(status=status)
        if request.htmx:
            return render(
                request,
                "partials/licitaciones/components/table_licitaciones.html",
                {"licitaciones": licitaciones},
            )
        else:
            return redirect("licitaciones")
    else:
            if request.htmx:
                licitaciones = Licitacion.objects.all()
                return render(
                    request,
                    "partials/licitaciones/read_licitaciones.html",
                    {"licitaciones": licitaciones},
                )
            else:
                licitaciones = Licitacion.objects.all()
                return render(
                    request, "home/licitaciones.html", {"licitaciones": licitaciones}
                )
def create_update_lic(request, lic_id=0):
    LicitacionItemFormset = inlineformset_factory(
        Licitacion, LicitacionItem, form=LicitacionItemForm, extra=2
    )
    data = {}
    if request.method == "GET":
        if lic_id != 0:
            lic_instance = get_object_or_404(Licitacion, id=lic_id)
            url = reverse("update_licitacion", kwargs={"lic_id": lic_instance.id})
            form = LicitacionForm(instance=lic_instance)
            formset = LicitacionItemFormset(instance=lic_instance)
            data["licitacion"] = lic_instance
            # Licitacion created via HTMX - Redirected after create POST request
            if request.htmx:
                data = {
                    "licitacion": lic_instance,
                    "form": form,
                    "formset": formset,
                    "url": url,
                }
        elif lic_id <= 0:
            data["form"] = LicitacionForm()
            data["url"] = reverse("create_licitacion")
            if request.htmx:
                return render(request, "partials/licitaciones/create_licitacion.html", data)
            else:
                return render(request, "partials/licitaciones/create_licitacion_base.html", data)

        return render(request, "partials/licitaciones/forms/create_licitacion_form.html", data)

    if request.method == "POST":
        # CREATE
        if lic_id == 0:
            form = LicitacionForm(request.POST)
            formset = LicitacionItemFormset(request.POST)
            # ITEMS FORM
            if request.POST["form_id"] == "items":
                if form.is_valid():
                    lic = form.save(commit=False)
                    formset = LicitacionItemFormset(request.POST, instance=lic)
                    data["form"] = form
                    data["formset"] = formset
                    return render(request, "partials/licitaciones/forms/create_licitacion_step_1.html", data)
            # GENERAL INFO FORM
            elif request.POST["form_id"] == "info":
                if form.is_valid():
                    lic = form.save(commit=False)
                    form = LicitacionForm(instance=lic)
                    print(formset)
                    if formset.total_form_count() <= 0:
                        formset = LicitacionItemFormset(instance=lic)
                    else:
                        formset = LicitacionItemFormset(request.POST,instance=lic)
                    data["form"] = form
                    data["formset"] = formset
                    return render(request, "partials/licitaciones/forms/create_licitacion_step_2.html", data)
        # UPDATE
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
                    data["form"] = form
                    data["formset"] = formset
                    data["message"] = "Datos actualizados"
                    return render(request, "partials/licitaciones/forms/create_licitacion_form.html", data)
