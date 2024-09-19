from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms import inlineformset_factory

from licitaciones.models import Licitacion, LicitacionItem
from licitaciones.forms import LicitacionForm, LicitacionItemForm
from licitaciones.models import Licitacion


# Create your views here.
def home(request):
    return render(request, "home/home.html", {})


def panel(request):
    if request.htmx:
        return render(
            request,
            "partials/home/panel_partial.html",
            {},
        )
    else:
        return render(request, "home/panel.html", {})


def buscador(request):
    if request.htmx:
        licitaciones = Licitacion.objects.all()
        return render(
            request,
            "partials/home/buscador_partial.html",
            {"licitaciones": licitaciones},
        )
    else:
        licitaciones = Licitacion.objects.all()
        return render(request, "home/buscador.html", {"licitaciones": licitaciones})


def ofertantes(request):
    data = {}
    if request.method == "GET":
        url = reverse("ofertantes")
        form = LicitacionForm()
        data["form"] = form
        data["url"] = url
    else:
        form = LicitacionForm(request.POST)
        if form.is_valid():
            lic = form.save(commit=False)
            data = render_items_form(request, lic)
            return render(request, "partials/items_form.html", data)

    return render(request, "home/ofertantes.html", data)


def save_new_licitacion(request):
    LicitacionItemFormset = inlineformset_factory(
        Licitacion, LicitacionItem, form=LicitacionItemForm, extra=1
    )
    form = LicitacionForm(request.POST)
    if form.is_valid():
        lic = form.save(commit=False)
        lic.save()
        formset = LicitacionItemFormset(request.POST, instance=lic)
        if formset.is_valid():
            formset.save()
            return redirect("licitaciones")


def render_items_form(request, lic_instance):
    LicitacionItemFormset = inlineformset_factory(
        Licitacion, LicitacionItem, form=LicitacionItemForm, extra=1
    )
    form = LicitacionForm(instance=lic_instance)
    formset = LicitacionItemFormset(instance=lic_instance)
    data = {"form": form, "formset": formset}
    return data
