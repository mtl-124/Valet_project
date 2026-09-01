# Valet Parking App

## Problemática
Servicio de valet parking para eventos y restaurantes. La entrega de autos suele
gestionarse con tickets de papel manuales, provocando pérdidas de llaves o demoras
al devolver el vehículo. Esta aplicación web permite al personal registrar la
recepción de cada auto (marca, placa y espacio asignado) y consultar la lista de
vehículos bajo custodia en tiempo real para agilizar la entrega.

## Requisitos funcionales
- El usuario debe poder iniciar sesión.
- El sistema debe permitir registrar los vehículos (marca del vehículo y código de llave).
- El sistema debe validar que los campos obligatorios del formulario no se envíen vacíos.
- Debe desplegar un mensaje de confirmación al usuario tras guardar correctamente un nuevo registro.
- El sistema debe mostrar el número de ticket único asignado a cada vehículo.
- El sistema debe indicar el responsable del vehículo.
- El sistema debe captar el número de placa del vehículo para una identificación única.
- El sistema debe reflejar una lista general con los datos del vehículo registrado recientemente.
- El sistema debe actualizar la lista de vehículos al momento de una devolución.
- El sistema debe requerir la verificación del código de ticket antes de autorizar la entrega.

## App: valet
App Django conectada al proyecto `valet_backend`, siguiendo el patrón MVT.
No usa base de datos: los datos se almacenan en una lista estática (`VALET_VEHICLES`)
dentro de `valet/models.py`. Los registros agregados mediante el formulario se
pierden al reiniciar el servidor — esto es esperado según el alcance del laboratorio.

- `models.py`: lista estática con los vehículos de ejemplo.
- `forms.py`: `VehicleForm`, formulario para registrar un nuevo vehículo.
- `views.py`: `vehicle_list` (listado) y `vehicle_create` (registro).
- `urls.py`: rutas `""` (listado) y `"nuevo/"` (registro).
- `templates/valet/`: `vehicle_list.html` y `vehicle_form.html`.

## Instalación
```bash
pip install -r requirements.txt
python manage.py runserver
```
Luego entra a `http://127.0.0.1:8000/valet/`.