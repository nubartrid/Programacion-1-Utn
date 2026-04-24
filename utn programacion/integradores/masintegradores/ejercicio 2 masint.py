def pedir_tipo_vehiculo():
    while True:
        tipo = input("Tipo de vehículo (auto/camioneta/moto): ").lower()
        if tipo in ["auto", "camioneta", "moto"]:
            return tipo
        print("Error. Tipo inválido.")

def pedir_dias():
    while True:
        dias = int(input("Cantidad de días (1-30): "))
        if 1 <= dias <= 30:
            return dias
        print("Error. Fuera de rango.")

def pedir_precio():
    while True:
        precio = float(input("Precio por día: "))
        if precio > 0:
            return precio
        print("Error. Debe ser mayor a 0.")

def pedir_km():
    while True:
        km = float(input("Kilómetros (0-5000): "))
        if 0 <= km <= 5000:
            return km
        print("Error. Fuera de rango.")

def pedir_pago():
    while True:
        pago = input("Forma de pago (efectivo/tarjeta/transferencia): ").lower()
        if pago in ["efectivo", "tarjeta", "transferencia"]:
            return pago
        print("Error. Forma inválida.")

def pedir_frecuente():
    while True:
        f = input("Cliente frecuente (si/no): ").lower()
        if f in ["si", "no"]:
            return f
        print("Error. Ingrese si o no.")


# INICIALIZACIONES
total_bruto = 0
total_final = 0
total_km = 0
contador_alquileres = 0
contador_tarjeta = 0

# contadores por tipo
cont_auto = 0
cont_camioneta = 0
cont_moto = 0

# km por tipo
km_auto = 0
km_camioneta = 0
km_moto = 0

# cliente con más días
max_dias = 0
cliente_max_dias = ""

# alquiler más caro
max_importe = 0
cliente_max_importe = ""

# acumulador de km general (para recargo)
km_acumulados = 0


while True:
    seguir = input("¿Cargar alquiler? (s/n): ").lower()
    if seguir == "n":
        break

    nombre = input("Nombre del cliente: ")
    tipo = pedir_tipo_vehiculo()
    dias = pedir_dias()
    precio = pedir_precio()
    km = pedir_km()
    pago = pedir_pago()
    frecuente = pedir_frecuente()

    contador_alquileres += 1
    total_km += km
    km_acumulados += km

    # cálculo base
    importe = dias * precio

    # recargo camioneta
    if tipo == "camioneta":
        importe *= 1.20

    # descuento cliente frecuente
    if frecuente == "si":
        importe *= 0.85

    total_bruto += importe

    # contar por tipo
    if tipo == "auto":
        cont_auto += 1
        km_auto += km
    elif tipo == "camioneta":
        cont_camioneta += 1
        km_camioneta += km
    else:
        cont_moto += 1
        km_moto += km

    # forma de pago
    if pago == "tarjeta":
        contador_tarjeta += 1

    # cliente con más días
    if dias > max_dias:
        max_dias = dias
        cliente_max_dias = nombre

    # alquiler más caro
    if importe > max_importe:
        max_importe = importe
        cliente_max_importe = nombre


# recargo global por km
if km_acumulados > 20000:
    total_final = total_bruto * 1.10
else:
    total_final = total_bruto

# promedio km
if contador_alquileres > 0:
    promedio_km = total_km / contador_alquileres
else:
    promedio_km = 0

# tipo más alquilado
if cont_auto > cont_camioneta and cont_auto > cont_moto:
    tipo_mas_alquilado = "auto"
elif cont_camioneta > cont_moto:
    tipo_mas_alquilado = "camioneta"
else:
    tipo_mas_alquilado = "moto"

# tipo con más km
if km_auto > km_camioneta and km_auto > km_moto:
    tipo_mas_km = "auto"
elif km_camioneta > km_moto:
    tipo_mas_km = "camioneta"
else:
    tipo_mas_km = "moto"


# RESULTADOS
print("\n--- RESULTADOS ---")
print("Total bruto:", total_bruto)
print("Total final:", total_final)
print("Tipo más alquilado:", tipo_mas_alquilado)
print("Cliente con más días:", cliente_max_dias)
print("Promedio de km:", promedio_km)
print("Tipo con más km:", tipo_mas_km)
print("Pagos con tarjeta:", contador_tarjeta)
print("Alquiler más caro:", cliente_max_importe, "-", max_importe)