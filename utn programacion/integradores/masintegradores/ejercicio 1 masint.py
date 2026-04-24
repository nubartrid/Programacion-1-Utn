def pedir_edad():
    while True:
        try:
            edad = int(input("Edad (0-100): "))
            if 0 <= edad <= 100:
                return edad
        except:
            pass
        print("Error. Edad inválida.")

def pedir_tipo():
    while True:
        tipo = input("Tipo (urgencia/control/cirugia): ").lower()
        if tipo in ["urgencia", "control", "cirugia"]:
            return tipo
        print("Error. Tipo inválido.")

def pedir_dias():
    while True:
        try:
            dias = int(input("Días (1-60): "))
            if 1 <= dias <= 60:
                return dias
        except:
            pass
        print("Error. Días inválidos.")

def pedir_costo():
    while True:
        try:
            costo = float(input("Costo por día (>0): "))
            if costo > 0:
                return costo
        except:
            pass
        print("Error. Costo inválido.")

def pedir_sexo():
    while True:
        sexo = input("Sexo (F/M/NB): ").upper()
        if sexo in ["F", "M", "NB"]:
            return sexo
        print("Error. Sexo inválido.")

def pedir_obra():
    while True:
        obra = input("¿Tiene obra social? (si/no): ").lower()
        if obra in ["si", "no"]:
            return obra
        print("Error.")

def pedir_pago():
    while True:
        pago = input("Forma de pago (efectivo/tarjeta/transferencia): ").lower()
        if pago in ["efectivo", "tarjeta", "transferencia"]:
            return pago
        print("Error.")


# acumuladores
total_bruto = 0
total_final = 0
total_dias = 0

# b)
cont_urgencia = 0
cont_control = 0
cont_cirugia = 0

# c) días por tipo
dias_urgencia = 0
dias_control = 0
dias_cirugia = 0

# d)
mayor_costo = None
nombre_mayor = ""

# e)
suma_costos_dia = 0
cont_pacientes = 0

# f)
cont_efectivo = 0
cont_tarjeta = 0
cont_transferencia = 0

# g)
cont_mas_10 = 0


while True:
    seguir = input("\n¿Cargar paciente? (s/n): ").lower()
    if seguir == "n":
        break

    nombre = input("Nombre: ")
    edad = pedir_edad()
    tipo = pedir_tipo()
    dias = pedir_dias()
    costo_dia = pedir_costo()
    sexo = pedir_sexo()
    obra = pedir_obra()
    pago = pedir_pago()

    cont_pacientes += 1

    subtotal = dias * costo_dia
    total_bruto += subtotal
    total_dias += dias

    # descuento obra social
    if obra == "si":
        subtotal *= 0.8

    total_final += subtotal

    # b)
    if tipo == "urgencia":
        cont_urgencia += 1
        dias_urgencia += dias
    elif tipo == "control":
        cont_control += 1
        dias_control += dias
    else:
        cont_cirugia += 1
        dias_cirugia += dias

    # d)
    if mayor_costo is None or subtotal > mayor_costo:
        mayor_costo = subtotal
        nombre_mayor = nombre

    # e)
    suma_costos_dia += costo_dia

    # f)
    if pago == "efectivo":
        cont_efectivo += 1
    elif pago == "tarjeta":
        cont_tarjeta += 1
    else:
        cont_transferencia += 1

    # g)
    if dias > 10:
        cont_mas_10 += 1


# descuento general
if total_dias > 500:
    total_final *= 0.9


# resultados
print("\n--- RESULTADOS ---")

# a)
print("Total bruto:", total_bruto)
print("Total final:", total_final)

# b)
print("Urgencia:", cont_urgencia)
print("Control:", cont_control)
print("Cirugía:", cont_cirugia)

# c)
if dias_urgencia >= dias_control and dias_urgencia >= dias_cirugia:
    tipo_mas_dias = "urgencia"
elif dias_control >= dias_cirugia:
    tipo_mas_dias = "control"
else:
    tipo_mas_dias = "cirugia"

print("Tipo con más días acumulados:", tipo_mas_dias)

# d)
if mayor_costo is not None:
    print("Paciente con mayor costo:", nombre_mayor)

# e)
if cont_pacientes > 0:
    promedio = suma_costos_dia / cont_pacientes
    print("Promedio costo por día:", promedio)

# f)
if cont_efectivo >= cont_tarjeta and cont_efectivo >= cont_transferencia:
    forma = "efectivo"
elif cont_tarjeta >= cont_transferencia:
    forma = "tarjeta"
else:
    forma = "transferencia"

print("Forma de pago más usada:", forma)

# g)
print("Pacientes con más de 10 días:", cont_mas_10)