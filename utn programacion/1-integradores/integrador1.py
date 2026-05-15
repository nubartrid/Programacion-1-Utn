def pedir_tipo_producto():
    while True:
        tipo = input("Tipo de producto (alimento/limpieza/perfumería): ").lower()
        if tipo in ["alimento", "limpieza", "perfumería"]:
            return tipo
        print("Error. Tipo inválido.")

def pedir_cantidad():
    while True:
        try:
            cant = int(input("Cantidad (1 a 20): "))
            if 1 <= cant <= 20:
                return cant
        except:
            pass
        print("Error. Cantidad inválida.")

def pedir_precio():
    while True:
        try:
            precio = float(input("Precio unitario (>0): "))
            if precio > 0:
                return precio
        except:
            pass
        print("Error. Precio inválido.")

def pedir_pago():
    while True:
        pago = input("Forma de pago (efectivo/tarjeta/transferencia): ").lower()
        if pago in ["efectivo", "tarjeta", "transferencia"]:
            return pago
        print("Error. Forma de pago inválida.")


# acumuladores
total_bruto = 0
total_final = 0
total_unidades = 0

suma_precios = 0
contador_precios = 0

venta_mas_cara_tarjeta = None

# contadores de forma de pago
cont_efectivo = 0
cont_tarjeta = 0
cont_transferencia = 0


for i in range(25):
    print(f"\n--- Venta {i+1} ---")

    tipo = pedir_tipo_producto()
    cantidad = pedir_cantidad()
    precio = pedir_precio()
    pago = pedir_pago()

    subtotal = cantidad * precio
    total_bruto += subtotal
    total_unidades += cantidad

    # contar forma de pago
    if pago == "efectivo":
        cont_efectivo += 1
        subtotal *= 0.95
    elif pago == "tarjeta":
        cont_tarjeta += 1
    else:
        cont_transferencia += 1

    total_final += subtotal

    # venta más cara con tarjeta
    if pago == "tarjeta":
        if venta_mas_cara_tarjeta is None or subtotal > venta_mas_cara_tarjeta:
            venta_mas_cara_tarjeta = subtotal

    # promedio precio unitario
    suma_precios += precio
    contador_precios += 1


# descuento global
if total_unidades > 400:
    total_final *= 0.8
elif total_unidades > 200:
    total_final *= 0.9


# promedio
promedio = suma_precios / contador_precios


# forma de pago más usada
if cont_efectivo > cont_tarjeta and cont_efectivo > cont_transferencia:
    forma_mas_usada = "efectivo"
elif cont_tarjeta > cont_transferencia:
    forma_mas_usada = "tarjeta"
else:
    forma_mas_usada = "transferencia"


# resultados
print("\n--- RESULTADOS ---")
print("Total bruto:", total_bruto)
print("Total final con descuentos:", total_final)

if venta_mas_cara_tarjeta is not None:
    print("Venta más cara con tarjeta:", venta_mas_cara_tarjeta)
else:
    print("No hubo ventas con tarjeta.")

print("Promedio de precio unitario:", promedio)
print("Forma de pago más utilizada:", forma_mas_usada)