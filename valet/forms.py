from django import forms


class VehicleForm(forms.Form):
    brand_model = forms.CharField(
        label="Marca y modelo", max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    license_plate = forms.CharField(
        label="Placa", max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    key_code = forms.CharField(
        label="Código de llave", max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    responsible = forms.CharField(
        label="Responsable", max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    parking_spot = forms.CharField(
        label="Espacio asignado", max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )