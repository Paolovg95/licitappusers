from django.contrib import admin
from django.urls import path
from licitaciones import views

urlpatterns = [
    path('new/', views.create_update_lic, name="create_lic"),
    path('edit/<int:lic_id>/', views.create_update_lic, name="update_lic"),
    path('licitacion-item/new/', views.add_lic_item, name="add_lic_item")
]
