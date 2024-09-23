from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.forms import inlineformset_factory
from licitaciones.models import Licitacion, LicitacionItem
from licitaciones.forms import LicitacionForm, LicitacionItemForm


def read_licitaciones(request):
    status = request.GET.get("status")
    if status != None:
        licitaciones = Licitacion.objects.filter(status=status)
        if request.htmx:
            return render(
                request,
                "partials/table_licitaciones.html",
                {"licitaciones": licitaciones, "status": status},
            )
        else:
            return redirect("licitaciones")
    else:
        if request.htmx:
            licitaciones = Licitacion.objects.all()
            return render(
                request,
                "partials/home/read_licitaciones_partial.html",
                {"licitaciones": licitaciones},
            )
        else:
            licitaciones = Licitacion.objects.all()
            return render(
                request, "home/licitaciones.html", {"licitaciones": licitaciones}
            )


def create_update_lic(request, lic_id=0):
    LicitacionItemFormset = inlineformset_factory(
        Licitacion, LicitacionItem, form=LicitacionItemForm, extra=1
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
                    "message": "Licitacion Creada",
                }
                return render(request, "partials/create_licitacion_form.html", data)
        elif lic_id <= 0:
            data["form"] = LicitacionForm()
            data["url"] = reverse("create_licitacion")
        return render(request, "create_licitacion.html", data)

    if request.method == "POST":
        # CREATE
        if lic_id == 0:
            form = LicitacionForm(request.POST)
            formset = LicitacionItemFormset(request.POST)
            # ITEMS FORM
            if request.POST["form_id"] == "items":
                LicitacionItemFormset = inlineformset_factory(
                    Licitacion, LicitacionItem, form=LicitacionItemForm, extra=1
                )
                if form.is_valid():
                    lic = form.save(commit=False)
                    lic.save()
                    formset = LicitacionItemFormset(request.POST, instance=lic)
                    if formset.is_valid():
                        formset.save(commit=False)
                    data["form"] = form
                    data["formset"] = formset
                    return render(request, "partials/create_licitacion_form.html", data)
            # GENERAL INFO FORM
            elif request.POST["form_id"] == "info":
                if form.is_valid():
                    lic = form.save(commit=False)
                    LicitacionItemFormset = inlineformset_factory(
                        Licitacion, LicitacionItem, form=LicitacionItemForm, extra=1
                    )
                    form = LicitacionForm(instance=lic)
                    if formset.is_valid():
                        formset = LicitacionItemFormset(request.POST, instance=lic)
                    else:
                        formset = LicitacionItemFormset(instance=lic)
                    data = {"form": form, "formset": formset}
                    return render(request, "partials/items_form.html", data)
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
                    return render(request, "partials/create_licitacion_form.html", data)


def render_items_form(request, lic_instance):
    LicitacionItemFormset = inlineformset_factory(
        Licitacion, LicitacionItem, form=LicitacionItemForm, extra=1
    )
    form = LicitacionForm(instance=lic_instance)
    formset = LicitacionItemFormset(instance=lic_instance)
    data = {"form": form, "formset": formset}
    return data
