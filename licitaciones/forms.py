from django import forms
from datetime import date
from django.utils.translation import gettext_lazy as _
from licitaciones.models import Licitacion, LicitacionItem

class LicitacionForm(forms.ModelForm):
    class Meta:
        model = Licitacion
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = ({'class': 'basis-1/2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-800 sm:text-sm sm:leading-6'})
        self.fields['client'].widget.attrs = ({'class': 'basis-1/4 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-800 sm:text-sm sm:leading-6'})
        self.fields['status'].widget.attrs = ({'class': 'basis-1/4 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-800 sm:text-sm sm:leading-6'})
        self.fields['obs'].widget.attrs = ({'class': 'basis-1/2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-800 sm:text-sm sm:leading-6', 'rows':6})
        self.fields['currency'].widget.attrs = ({'class': 'basis-1/4 block w-full mb-8 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-800 sm:text-sm sm:leading-6'})
        self.fields['total_sum_lic'].widget.attrs = ({'class': 'basis-1/2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-800 sm:text-sm sm:leading-6'})
        self.fields['category'].widget.attrs = ({'class': 'basis-1/4 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-800 sm:text-sm sm:leading-6'})
        self.fields['payment_method'].widget.attrs = ({'class': 'basis-1/4 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-800 sm:text-sm sm:leading-6'})
        self.fields['delivery_time'].widget.attrs = ({'class': 'basis-1/2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-800 sm:text-sm sm:leading-6'})
        self.fields["close_date"].widget.input_type = 'date'
        self.fields['close_date'].widget.attrs = ({'class': 'basis-1/4 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-800 sm:text-sm sm:leading-6'})
        self.fields['city'].widget.attrs = ({'class': 'basis-1/4 block w-full mb-8 rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-800 sm:text-sm sm:leading-6'})

    def clean_close_date(self):
        close_date = self.cleaned_data.get('close_date')
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
        self.fields['name'].widget.attrs = ({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-800 focus:outline-none focus:ring-0 focus:border-blue-800 peer', 'placeholder': "Name"})
        self.fields['description'].widget.attrs = ({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-800 focus:outline-none focus:ring-0 focus:border-blue-800 peer', 'placeholder': "Description", 'rows': 1})
        self.fields['quantity'].widget.attrs = ({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-800 focus:outline-none focus:ring-0 focus:border-blue-800 peer', 'placeholder': "Cantidad"})
        self.fields['unit'].widget.attrs = ({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-800 focus:outline-none focus:ring-0 focus:border-blue-800 peer', 'placeholder': "Unit"})
        self.fields['price'].widget.attrs = ({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-800 focus:outline-none focus:ring-0 focus:border-blue-800 peer', 'placeholder': "Price"})
        self.fields['note'].widget.attrs = ({'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-800 focus:outline-none focus:ring-0 focus:border-blue-800 peer', 'placeholder': "Note"})
