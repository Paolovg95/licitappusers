from django.contrib import admin
from django.urls import path
from licitaciones import views

urlpatterns = [
    path('new/', views.create_update_lic, name="create_lic"),
    path('edit/<int:lic_id>/', views.create_update_lic, name="update_lic"),
    path('<int:lic_id>/item/', views.lic_item_create, name="lic_item_create")
]
