from django.db import models
from licitaciones.models import Licitacion


# Create your models here.
class Oferta(models.Model):
    licitacion = models.ForeignKey(Licitacion, on_delete=models.CASCADE)
    total_sum_offer = models.IntegerField()
    total_items_submitted = models.IntegerField()
    total_items_not_submitted = models.IntegerField()
    # Company -> foreignKey
    # User -> foreignKey
    payment_method = models.CharField(max_length=255)
    delivery_time = models.CharField(blank=True, null=True, max_length=20)


class OfferItem(models.Model):
    offer = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    note = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)
    offer_price = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
