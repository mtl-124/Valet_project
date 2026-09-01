from django.shortcuts import render, redirect
from datetime import datetime
from .forms import VehicleForm
from .models import VALET_VEHICLES


def vehicle_list(request):
    return render(request, "valet/vehicle_list.html", {"vehicles": VALET_VEHICLES})


def vehicle_create(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            new_id = max([v["id"] for v in VALET_VEHICLES], default=0) + 1
            VALET_VEHICLES.append({
                "id": new_id,
                "username": "operador1",
                "brand_model": form.cleaned_data["brand_model"],
                "key_code": form.cleaned_data["key_code"],
                "ticket_number": f"T-{new_id:04d}",
                "responsible": form.cleaned_data["responsible"],
                "license_plate": form.cleaned_data["license_plate"],
                "status": "En Custodia",
                "parking_spot": form.cleaned_data["parking_spot"],
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            })
            return redirect("valet:vehicle_list")
    else:
        form = VehicleForm()
    return render(request, "valet/vehicle_form.html", {"form": form})