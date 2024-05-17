from django.contrib import admin
from django.urls import path
from licitaciones import views

urlpatterns = [
    path('', views.view_licitaciones, name="licitaciones"),
    path('new/', views.create_update_lic, name="licitaciones_new"),
    path('<str:status>/', views.view_licitaciones, name="licitaciones_status"),
    path('edit/<int:lic_id>/', views.create_update_lic, name="licitaciones_edit"),
]
