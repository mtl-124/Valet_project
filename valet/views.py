from django.shortcuts import render
from .models import VALET_VEHICLES

def vehicle_list(request):
    return render(request, 'valet/vehicle_list.html', {'vehicles': VALET_VEHICLES})