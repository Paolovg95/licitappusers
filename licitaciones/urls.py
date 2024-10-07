from django.contrib import admin
from django.urls import path
from licitaciones import views


urlpatterns = [
    path("", views.read_licitaciones, name="licitaciones"),
    path("new/", views.create_update_lic, name="create_licitacion"),
    path("save/", views.save_licitacion, name="save_licitacion"),
    path("edit/<int:lic_id>/", views.create_update_lic, name="update_licitacion"),
    path("<str:search_text>/", views.read_licitaciones, name="search_results"),
    path("<str:status>/", views.read_licitaciones, name="read_licitaciones")
]
