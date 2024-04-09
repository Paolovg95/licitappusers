from django import forms
from django.forms import inlineformset_factory
from datetime import date
from licitaciones.models import Licitacion, LicitacionItem

# LicitacionForm = forms.modelform_factory(Licitacion, fields="__all__")

class LicitacionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({ 'class': 'form-control m-2', 'placeholder': 'Title'})
        self.fields["obs"].widget.attrs.update({'class': 'form-control m-2', 'placeholder': 'Observaciones'})
        self.fields["status"].widget.attrs.update({'class': 'form-control m-2'})
        # self.fields["start_date"].date_attrs.update({'class': 'form-control m-2'})
        self.fields["close_date"].widget.input_type = 'date'
        self.fields["close_date"].widget.attrs.update({'class': 'form-control m-2', 'placeholder': 'Close Date'})
        self.fields["currency"].widget.attrs.update({'class': 'form-control m-2', 'placeholder': 'Moneda'})
        self.fields["category"].widget.attrs.update({'class': 'form-control m-2', 'placeholder': 'Categoría'})
        self.fields["payment_method"].widget.attrs.update({'class': 'form-control m-2', 'placeholder': 'Método de pago'})
        self.fields["delivery_time"].widget.attrs.update({'class': 'form-control m-2', 'placeholder': 'Tiempo de entrega'})
        self.fields["client"].widget.attrs.update({'class': 'bg-light form-control m-2', 'placeholder': 'Empresa'})
        self.fields["city"].widget.attrs.update({'class': 'form-control m-2' , 'placeholder': 'Ciudad'})
        self.fields["total_sum_lic"].widget.attrs.update({'class': 'form-control m-2', 'placeholder': 'Suma total'})
    class Meta:
        model = Licitacion
        fields = "__all__"
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
