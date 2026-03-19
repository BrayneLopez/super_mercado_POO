from datetime import datetime

# fecha del producto (string → convertir a datetime)
fecha_vencimiento = datetime.strptime('28/01/2026', '%d/%m/%Y')

# fecha actual
hoy = datetime.now()

# comparación
if fecha_vencimiento < hoy:
    print("Producto vencido")
else:
    print("Producto vigente")