def pedir_edad():
    while True:
        try:
            edad = int(input("Edad: "))
            if edad > 0:
                return edad
        except:
            pass
        print("Error. Edad inválida.")

def pedir_puntos():
    while True:
        try:
            puntos = int(input("Puntos (0 a 60): "))
            if 0 <= puntos <= 60:
                return puntos
        except:
            pass
        print("Error. Puntos inválidos.")

def pedir_partidos():
    while True:
        try:
            partidos = int(input("Partidos ganados (0 a 35): "))
            if 0 <= partidos <= 35:
                return partidos
        except:
            pass
        print("Error. Número inválido.")

def pedir_saque():
    while True:
        saque = input("Tipo de saque (plano/liftado/cortado): ").lower()
        if saque in ["plano", "liftado", "cortado"]:
            return saque
        print("Error. Saque inválido.")

def pedir_categoria():
    while True:
        cat = input("Categoría (elite/experto/avanzado): ").lower()
        if cat in ["elite", "experto", "avanzado"]:
            return cat
        print("Error. Categoría inválida.")


# acumuladores
cont_punto1 = 0

menor_edad_50 = None
nombre_menor = ""
cat_menor = ""

cont_expertos = 0
total_jugadores = 0

suma_edades_avanzado = 0
cont_avanzado = 0

# saques en elite
cont_plano = 0
cont_liftado = 0
cont_cortado = 0


while True:
    seguir = input("\n¿Cargar jugador? (s/n): ").lower()
    if seguir == "n":
        break

    nombre = input("Nombre: ")
    edad = pedir_edad()
    puntos = pedir_puntos()
    partidos = pedir_partidos()
    saque = pedir_saque()
    categoria = pedir_categoria()

    total_jugadores += 1

    # 1)
    if categoria == "elite" and saque == "plano" and 19 <= edad <= 25:
        cont_punto1 += 1

    # 2)
    if puntos > 50:
        if menor_edad_50 is None or edad < menor_edad_50:
            menor_edad_50 = edad
            nombre_menor = nombre
            cat_menor = categoria

    # 3)
    if categoria == "experto":
        cont_expertos += 1

    # 4)
    if categoria == "avanzado":
        suma_edades_avanzado += edad
        cont_avanzado += 1

    # 5)
    if categoria == "elite":
        if saque == "plano":
            cont_plano += 1
        elif saque == "liftado":
            cont_liftado += 1
        else:
            cont_cortado += 1


# resultados
print("\n--- RESULTADOS ---")

# 1
print("1) Cantidad:", cont_punto1)

# 2
if menor_edad_50 is not None:
    print("2) Jugador más joven con más de 50 puntos:")
    print("Nombre:", nombre_menor, "| Categoría:", cat_menor)
else:
    print("2) No hay jugadores con más de 50 puntos.")

# 3
if total_jugadores > 0:
    porcentaje_expertos = (cont_expertos / total_jugadores) * 100
    print("3) Porcentaje de expertos:", porcentaje_expertos, "%")

# 4
if cont_avanzado > 0:
    promedio = suma_edades_avanzado / cont_avanzado
    print("4) Promedio edad avanzados:", promedio)
else:
    print("4) No hay jugadores avanzados.")

# 5
if cont_plano >= cont_liftado and cont_plano >= cont_cortado:
    mas_usado = "plano"
elif cont_liftado >= cont_cortado:
    mas_usado = "liftado"
else:
    mas_usado = "cortado"

print("5) Saque más usado en elite:", mas_usado)