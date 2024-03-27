from django import forms
from licitaciones.models import Licitacion

# LicitacionForm = forms.modelform_factory(Licitacion, fields="__all__")

class LicitacionForm(forms.ModelForm):
    class Meta:
        model = Licitacion
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({'class': 'form-control col-md-6'})
        self.fields["obs"].widget.attrs.update({'class': 'form-control col-md-6'})
        # self.fields["start_date"].widget.attrs.update({'class': 'form-control col-md-6'})
        # self.fields["close_date"].widget.attrs.update({'class': 'form-control col-md-6'})
        self.fields["status"].widget.attrs.update({'class': 'form-control col-md-6'})
        self.fields["currency"].widget.attrs.update({'class': 'form-control col-md-6'})
        self.fields["category"].widget.attrs.update({'class': 'form-control col-md-6'})
        self.fields["payment_method"].widget.attrs.update({'class': 'form-control col-md-6'})
        self.fields["delivery_time"].widget.attrs.update({'class': 'form-control col-md-6'})
        self.fields["client"].widget.attrs.update({'class': 'form-control col-md-6'})
        self.fields["city"].widget.attrs.update({'class': 'form-control col-md-6'})
        self.fields["total_sum_lic"].widget.attrs.update({'class': 'form-control col-md-6'})
