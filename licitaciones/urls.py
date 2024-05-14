from django.contrib import admin
from django.urls import path
from licitaciones import views

urlpatterns = [
    path('', views.view_licitaciones, name="licitaciones"),
    path('new/', views.create_update_lic, name="create_lic"),
    path('all/', views.view_all_licitaciones, name="all_lic"),
    path('edit/<int:lic_id>/', views.create_update_lic, name="update_lic"),
]
