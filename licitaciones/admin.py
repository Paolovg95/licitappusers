from django.contrib import admin
from .models import Licitacion, LicitacionItem, LicitacionItemPhoto
# Register your models here.

class LicitacionItemInline(admin.StackedInline):
    model = LicitacionItem
    extra = 0
    fields = ['name', 'description', 'price', 'unit', 'quantity', 'images']
    readonly_fields = ['note','date_added', 'date_updated']

@admin.register(Licitacion)
class LicitacionAdmin(admin.ModelAdmin):
    inlines = [LicitacionItemInline]
    list_display = ('title', 'id')

admin.site.register(LicitacionItemPhoto)
