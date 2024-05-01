from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from datetime import date
# Create your models here.

def get_categories():
    categories = settings.CATEGORIES
    categories.sort()
    return {i: i for i in categories}
def get_currencies():
    currency = settings.CURRENCY
    currency.sort()
    return {i: i for i in currency}
def get_status():
    status = settings.STATUS
    status.sort()
    return {i: i for i in status}
def get_cities():
    cities = settings.CITIES
    cities.sort()
    return {i: i for i in cities}

class Licitacion(models.Model):
    title = models.CharField(max_length=255)
    obs = models.TextField(blank=True, null=True)
    start_date = models.DateField(auto_now_add=True, null=True)
    close_date = models.DateField()
    status = models.CharField(max_length=10, choices=get_status, default="OPEN")
    currency = models.CharField(max_length=15, choices=get_currencies)
    category = models.CharField(max_length=100, choices=get_categories)
    payment_method = models.CharField(max_length=255)
    delivery_time = models.CharField(blank=True, null=True, max_length=20)
    client = models.CharField(blank=True, null=True,max_length=20)
    city = models.CharField(blank=True, null=True, max_length=20, choices=get_cities)
    total_sum_lic = models.IntegerField()

    class Meta:
        verbose_name = 'licitacion'
        verbose_name_plural = 'licitaciones'


class LicitacionItem(models.Model):
    licitacion = models.ForeignKey(Licitacion, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    note = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)
    price = models.IntegerField()
    date_added = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    date_updated = models.DateTimeField(blank=True, null=True, auto_now=True)
