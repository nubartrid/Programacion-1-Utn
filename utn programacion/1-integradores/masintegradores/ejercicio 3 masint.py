def pedir_plan():
    while True:
        plan = input("Tipo de plan (mensual/trimestral/anual): ").lower()
        if plan in ["mensual", "trimestral", "anual"]:
            return plan
        print("Error.")

def pedir_edad():
    while True:
        edad = int(input("Edad (12-80): "))
        if 12 <= edad <= 80:
            return edad
        print("Error.")

def pedir_precio():
    while True:
        precio = float(input("Precio: "))
        if precio > 0:
            return precio
        print("Error.")

def pedir_pago():
    while True:
        pago = input("Forma de pago (efectivo/tarjeta/transferencia): ").lower()
        if pago in ["efectivo", "tarjeta", "transferencia"]:
            return pago
        print("Error.")

def pedir_turno():
    while True:
        turno = input("Turno (mañana/tarde/noche): ").lower()
        if turno in ["mañana", "tarde", "noche"]:
            return turno
        print("Error.")

def pedir_nuevo():
    while True:
        nuevo = input("Alumno nuevo (si/no): ").lower()
        if nuevo in ["si", "no"]:
            return nuevo
        print("Error.")


# INICIALIZACIÓN
total_bruto = 0
total_final = 0
contador_ventas = 0
suma_precios = 0

# contadores por plan
cont_mensual = 0
cont_trimestral = 0
cont_anual = 0

# turnos
cont_manana = 0
cont_tarde = 0
cont_noche = 0

# formas de pago
cont_efectivo = 0
cont_tarjeta = 0
cont_transferencia = 0

# máximos
max_precio = 0
cliente_max = ""

# menores
menores = 0


while True:
    seguir = input("¿Cargar venta? (s/n): ").lower()
    if seguir == "n":
        break

    nombre = input("Nombre: ")
    plan = pedir_plan()
    edad = pedir_edad()
    precio = pedir_precio()
    pago = pedir_pago()
    turno = pedir_turno()
    nuevo = pedir_nuevo()

    contador_ventas += 1
    suma_precios += precio

    # recargo anual
    if plan == "anual":
        precio *= 1.15

    # descuento alumno nuevo
    if nuevo == "si":
        precio *= 0.90

    total_bruto += precio

    # contadores por plan
    if plan == "mensual":
        cont_mensual += 1
    elif plan == "trimestral":
        cont_trimestral += 1
    else:
        cont_anual += 1

    # turnos
    if turno == "mañana":
        cont_manana += 1
    elif turno == "tarde":
        cont_tarde += 1
    else:
        cont_noche += 1

    # formas de pago
    if pago == "efectivo":
        cont_efectivo += 1
    elif pago == "tarjeta":
        cont_tarjeta += 1
    else:
        cont_transferencia += 1

    # máximo precio
    if precio > max_precio:
        max_precio = precio
        cliente_max = nombre

    # menores de edad
    if edad < 18:
        menores += 1


# descuento general
if contador_ventas > 50:
    total_final = total_bruto * 0.95
else:
    total_final = total_bruto

# promedio
if contador_ventas > 0:
    promedio = suma_precios / contador_ventas
else:
    promedio = 0

# turno con más clientes
if cont_manana > cont_tarde and cont_manana > cont_noche:
    turno_max = "mañana"
elif cont_tarde > cont_noche:
    turno_max = "tarde"
else:
    turno_max = "noche"

# forma de pago más usada
if cont_efectivo > cont_tarjeta and cont_efectivo > cont_transferencia:
    pago_max = "efectivo"
elif cont_tarjeta > cont_transferencia:
    pago_max = "tarjeta"
else:
    pago_max = "transferencia"


# RESULTADOS
print("\n--- RESULTADOS ---")
print("Total bruto:", total_bruto)
print("Total final:", total_final)
print("Ventas por plan:", cont_mensual, cont_trimestral, cont_anual)
print("Turno con más clientes:", turno_max)
print("Cliente del plan más caro:", cliente_max)
print("Promedio de precios:", promedio)
print("Forma de pago más usada:", pago_max)
print("Menores de 18:", menores)