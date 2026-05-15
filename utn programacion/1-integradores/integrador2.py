def pedir_edad():
    while True:
        try:
            edad = int(input("Edad (>=18): "))
            if edad >= 18:
                return edad
        except:
            pass
        print("Error. Edad inválida.")

def pedir_genero():
    while True:
        genero = input("Género (masculino/femenino/otro): ").lower()
        if genero in ["masculino", "femenino", "otro"]:
            return genero
        print("Error. Género inválido.")

def pedir_tecnologia():
    while True:
        tec = input("Tecnología (ia/rv/ra/iot): ").lower()
        if tec in ["ia", "rv/ra", "iot"]:
            return tec
        print("Error. Tecnología inválida.")


# acumuladores
cont_punto1 = 0

cont_no_ia_cond = 0
total_encuestas = 10

mayor_edad_masculino = None
nombre_mayor = ""
tec_mayor = ""


for i in range(total_encuestas):
    print(f"\n--- Encuesta {i+1} ---")

    nombre = input("Nombre: ")
    edad = pedir_edad()
    genero = pedir_genero()
    tec = pedir_tecnologia()

    # 1)
    if genero == "masculino" and tec in ["ia", "iot"] and 25 <= edad <= 50:
        cont_punto1 += 1

    # 2)
    if tec != "ia" and (genero != "femenino" or 33 <= edad <= 40):
        cont_no_ia_cond += 1

    # 3)
    if genero == "masculino":
        if mayor_edad_masculino is None or edad > mayor_edad_masculino:
            mayor_edad_masculino = edad
            nombre_mayor = nombre
            tec_mayor = tec


# porcentaje punto 2
porcentaje = (cont_no_ia_cond / total_encuestas) * 100


# resultados
print("\n--- RESULTADOS ---")

print("1) Cantidad:", cont_punto1)

print("2) Porcentaje:", porcentaje, "%")

if mayor_edad_masculino is not None:
    print("3) Empleado masculino de mayor edad:")
    print("Nombre:", nombre_mayor)
    print("Tecnología:", tec_mayor)
else:
    print("3) No hubo empleados masculinos.")