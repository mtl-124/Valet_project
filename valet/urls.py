from django.urls import path
from . import views

app_name = "valet"

urlpatterns = [
    path("", views.vehicle_list, name="vehicle_list"),
    path("nuevo/", views.vehicle_create, name="vehicle_create"),
]