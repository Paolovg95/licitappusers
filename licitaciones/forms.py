from django import forms
from datetime import date
from django.utils.translation import gettext_lazy as _
from licitaciones.models import Licitacion, LicitacionItem


class LicitacionForm(forms.ModelForm):
    class Meta:
        model = Licitacion
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        kwargs["label_suffix"] = ""
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs = {
            "class": "mt-2 block w-full duration-100 rounded-md transition border border-solid focus:outline-none focus:ring text-base bg-white border-gray-400 hover:border-gray-600 text-high-emphasis focus:border-blue-700 outline-none focus:ring-blue-50"
        }
        self.fields["client"].widget.attrs = {
            "class": "mt-2 block w-full duration-100 rounded-md transition border border-solid focus:outline-none focus:ring text-base bg-white border-gray-400 hover:border-gray-600 text-high-emphasis focus:border-blue-700 outline-none focus:ring-blue-50"
        }
        self.fields["status"].widget.attrs = {
            "class": "mt-2 block w-full duration-100 rounded-md transition border border-solid focus:outline-none focus:ring text-base bg-white border-gray-400 hover:border-gray-600 text-high-emphasis focus:border-blue-700 outline-none focus:ring-blue-50"
        }
        self.fields["city"].widget.attrs = {
            "class": "basis-1/4 mt-2 block w-full mb-8 duration-100 rounded-md transition border border-solid focus:outline-none focus:ring text-base bg-white border-gray-400 hover:border-gray-600 text-high-emphasis focus:border-blue-700 outline-none focus:ring-blue-50"
        }
        self.fields["obs"].widget.attrs = {
            "class": "basis-1/2 mt-2 block w-full duration-100 rounded-md transition border border-solid focus:outline-none focus:ring text-base bg-white border-gray-400 hover:border-gray-600 text-high-emphasis focus:border-blue-700 outline-none focus:ring-blue-50",
            "rows": 4,
        }
        self.fields["currency"].widget.attrs = {
            "class": "basis-1/4 mt-2 block w-full mb-8 duration-100 rounded-md transition border border-solid focus:outline-none focus:ring text-base bg-white border-gray-400 hover:border-gray-600 text-high-emphasis focus:border-blue-700 outline-none focus:ring-blue-50"
        }
        self.fields["total_sum_lic"].widget.attrs = {
            "class": "basis-1/2 mt-2 block w-full duration-100 rounded-md transition border border-solid focus:outline-none focus:ring text-base bg-white border-gray-400 hover:border-gray-600 text-high-emphasis focus:border-blue-700 outline-none focus:ring-blue-50"
        }
        self.fields["category"].widget.attrs = {
            "class": "basis-1/4 mt-2 block w-full duration-100 rounded-md transition border border-solid focus:outline-none focus:ring text-base bg-white border-gray-400 hover:border-gray-600 text-high-emphasis focus:border-blue-700 outline-none focus:ring-blue-50"
        }
        self.fields["payment_method"].widget.attrs = {
            "class": "basis-1/4 mt-2 block w-full duration-100 rounded-md transition border border-solid focus:outline-none focus:ring text-base bg-white border-gray-400 hover:border-gray-600 text-high-emphasis focus:border-blue-700 outline-none focus:ring-blue-50"
        }
        self.fields["delivery_time"].widget.attrs = {
            "class": "basis-1/2 mt-2 block w-full duration-100 rounded-md transition border border-solid focus:outline-none focus:ring text-base bg-white border-gray-400 hover:border-gray-600 text-high-emphasis focus:border-blue-700 outline-none focus:ring-blue-50"
        }
        self.fields["close_date"].widget.input_type = "date"
        self.fields["close_date"].widget.attrs = {
            "class": "basis-1/4 mt-2 block w-full duration-100 rounded-md transition border border-solid focus:outline-none focus:ring text-base bg-white border-gray-400 hover:border-gray-600 text-high-emphasis focus:border-blue-700 outline-none focus:ring-blue-50"
        }

    def clean_close_date(self):
        close_date = self.cleaned_data.get("close_date")
        now = date.today()
        if close_date <= now:
            raise forms.ValidationError("Close Date has to be in the future")
        return close_date


class LicitacionItemForm(forms.ModelForm):
    class Meta:
        model = LicitacionItem
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs = {
            "class": "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-800 focus:outline-none focus:ring-0 focus:border-blue-800 peer",
            "placeholder": "Name",
        }
        self.fields["description"].widget.attrs = {
            "class": "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-800 focus:outline-none focus:ring-0 focus:border-blue-800 peer",
            "placeholder": "Description",
            "rows": 1,
        }
        self.fields["quantity"].widget.attrs = {
            "class": "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-800 focus:outline-none focus:ring-0 focus:border-blue-800 peer",
            "placeholder": "Cantidad",
        }
        self.fields["unit"].widget.attrs = {
            "class": "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-800 focus:outline-none focus:ring-0 focus:border-blue-800 peer",
            "placeholder": "Unit",
        }
        self.fields["price"].widget.attrs = {
            "class": "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-800 focus:outline-none focus:ring-0 focus:border-blue-800 peer",
            "placeholder": "Price",
        }
        self.fields["note"].widget.attrs = {
            "class": "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-800 focus:outline-none focus:ring-0 focus:border-blue-800 peer",
            "placeholder": "Note",
        }
