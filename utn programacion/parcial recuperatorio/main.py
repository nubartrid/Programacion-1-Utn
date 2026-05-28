
# 1) Importamos la lista de pokemones desde el archivo pokemones.py
from pokemones import lista_pokemon

# Referencias de índice para no confundirse
NOMBRE = 0
TIPO = 1
ALTURA = 2
PESO = 3
NIVEL = 4
FUERZA_ATAQUE = 5
REGION = 6

# Regiones válidas según la Pokedex oficial
REGIONES_VALIDAS = ["Johto", "Kanto", "Sinnoh", "Hoenn"]


# ============================================================
# FUNCIONES DE VISUALIZACION
# ============================================================

def mostrar_linea_separadora():
    """Muestra una línea para separar visualmente el contenido"""
    print("-" * 45)


def mostrar_pokemon(pokemon):
    """
    Muestra toda la información de un pokémon de forma amena.
    Recibe una lista con los datos del pokémon.
    """
    mostrar_linea_separadora()
    print(f"  Nombre        : {pokemon[NOMBRE]}")
    print(f"  Tipo          : {pokemon[TIPO]}")
    print(f"  Altura        : {pokemon[ALTURA]} m")
    print(f"  Peso          : {pokemon[PESO]} kg")
    print(f"  Nivel         : {pokemon[NIVEL]}")
    print(f"  Fuerza ataque : {pokemon[FUERZA_ATAQUE]}")
    print(f"  Región        : {pokemon[REGION]}")
    mostrar_linea_separadora()


def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("=" * 45)
    print("  SISTEMA POKÉDEX - PROF. OAK")
    print("=" * 45)
    print("  1. Ver todos los pokémones")
    print("  2. Agregar un pokémon")
    print("  3. Eliminar un pokémon por nombre")
    print("  4. Ordenar pokémones de Z a A")
    print("  5. Ver el pokémon de agua más pesado")
    print("  6. Ver el pokémon con más fuerza de ataque")
    print("  7. Listar pokémones por región")
    print("  8. Salir")
    print("=" * 45)


# ============================================================
# OPCIÓN 1 - LISTAR TODOS LOS POKÉMONES
# ============================================================

def listar_todos(lista):
    """Muestra en pantalla todos los pokémones de la lista"""
    if len(lista) == 0:
        print("\n No hay pokémones en la lista.")
        return

    print(f"\n Hay {len(lista)} pokémones registrados:\n")
    for pokemon in lista:
        mostrar_pokemon(pokemon)


# ============================================================
# OPCIÓN 2 - AGREGAR POKÉMON
# ============================================================

def pedir_nombre():
    """
    Le pide al usuario el nombre del pokémon.
    No puede ser un string vacío.
    """
    nombre = input("  Ingresá el nombre del pokémon: ").strip()
    while nombre == "":
        print(" El nombre no puede estar vacío. Intentá de nuevo.")
        nombre = input("  Ingresá el nombre del pokémon: ").strip()
    return nombre


def pedir_tipo():
    """
    Le pide al usuario el tipo del pokémon.
    No puede ser un string vacío.
    """
    tipo = input("  Ingresá el tipo del pokémon (Ej: Fuego, Agua): ").strip()
    while tipo == "":
        print(" El tipo no puede estar vacío. Intentá de nuevo.")
        tipo = input("  Ingresá el tipo del pokémon: ").strip()
    return tipo


def pedir_numero_positivo(mensaje):
    """
    Le pide al usuario un número y valida que sea mayor a 0.
    Si el usuario ingresa algo que no es número, avisa y vuelve a pedir.
    """
    while True:
        entrada = input(mensaje).strip()
        # Verificamos que sea un número válido
        es_numero = True
        for caracter in entrada:
            if caracter not in "0123456789.":
                es_numero = False
                break

        if not es_numero or entrada == "" or entrada == ".":
            print(" Ingresá un número válido mayor a 0.")
        else:
            numero = float(entrada)
            if numero <= 0:
                print(" El valor debe ser mayor a 0. Intentá de nuevo.")
            else:
                return numero


def pedir_region():
    """
    Le pide al usuario la región del pokémon.
    Solo acepta: Johto, Kanto, Sinnoh o Hoenn.
    """
    print(f"  Regiones válidas: {', '.join(REGIONES_VALIDAS)}")
    region = input("  Ingresá la región: ").strip().capitalize()
    while region not in REGIONES_VALIDAS:
        print(f" Región inválida. Debe ser una de: {', '.join(REGIONES_VALIDAS)}")
        region = input("  Ingresá la región: ").strip().capitalize()
    return region


def agregar_pokemon(lista):
    """
    Le pide al usuario todos los datos de un nuevo pokémon
    y lo agrega a la lista original.
    """
    print("\n AGREGAR NUEVO POKÉMON")
    mostrar_linea_separadora()

    nombre = pedir_nombre()
    tipo = pedir_tipo()
    altura = pedir_numero_positivo("  Ingresá la altura (en metros, Ej: 0.5): ")
    peso = pedir_numero_positivo("  Ingresá el peso (en kg, Ej: 9.0): ")
    nivel = int(pedir_numero_positivo("  Ingresá el nivel (Ej: 10): "))
    fuerza_ataque = int(pedir_numero_positivo("  Ingresá la fuerza de ataque (Ej: 55): "))
    region = pedir_region()

    # Creamos el nuevo pokémon como lista (igual que los demás)
    nuevo_pokemon = [nombre, tipo, altura, peso, nivel, fuerza_ataque, region]

    # Lo agregamos a la lista original
    lista.append(nuevo_pokemon)

    print(f"\n ¡{nombre} fue agregado exitosamente a la Pokédex!")


# ============================================================
# OPCIÓN 3 - ELIMINAR POKÉMON POR NOMBRE
# ============================================================

def buscar_pokemon_por_nombre_recursivo(lista, nombre_buscado, indice):
    """
    Busca un pokémon en la lista por nombre usando RECURSIVIDAD.
    Devuelve el índice donde está en la lista, o -1 si no lo encuentra.
    """
    # Caso base: llegamos al final de la lista sin encontrarlo
    if indice == len(lista):
        return -1

    # Comparamos en minúsculas para que no importe si está en mayúsculas
    if lista[indice][NOMBRE].lower() == nombre_buscado.lower():
        return indice

    # Llamada recursiva: buscamos en el siguiente elemento
    return buscar_pokemon_por_nombre_recursivo(lista, nombre_buscado, indice + 1)


def eliminar_pokemon(lista):
    """
    Le pide al usuario el nombre del pokémon a eliminar
    y lo quita de la lista si existe.
    """
    print("\n ELIMINAR POKÉMON")
    mostrar_linea_separadora()

    nombre = input("  Ingresá el nombre del pokémon a eliminar: ").strip()

    # Usamos la función recursiva para buscar el pokémon
    indice = buscar_pokemon_por_nombre_recursivo(lista, nombre, 0)

    if indice == -1:
        print(f"\n No se encontró ningún pokémon con el nombre '{nombre}'.")
    else:
        pokemon_eliminado = lista[indice][NOMBRE]
        lista.pop(indice)
        print(f"\n ¡{pokemon_eliminado} fue eliminado de la Pokédex!")


# ============================================================
# OPCIÓN 4 - ORDENAR DE Z A A (ORDEN DESCENDENTE ALFABÉTICO)
# ============================================================

def ordenar_por_nombre_z_a(lista):
    """
    Ordena la lista de pokémones alfabéticamente de Z a A.
    Usa el algoritmo de ordenamiento BURBUJA (Bubble Sort).
    """
    n = len(lista)

    # Recorremos la lista n-1 veces
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # Comparamos nombres en minúsculas para que sea justo
            nombre_actual = lista[j][NOMBRE].lower()
            nombre_siguiente = lista[j + 1][NOMBRE].lower()

            # Si el nombre actual es MENOR al siguiente, los intercambiamos
            # (queremos de Z a A, entonces el mayor va primero)
            if nombre_actual < nombre_siguiente:
                # Intercambio
                auxiliar = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = auxiliar

    print("\n ¡Lista ordenada de Z a A exitosamente!")
    listar_todos(lista)


# ============================================================
# OPCIÓN 5 - POKÉMON DE AGUA MÁS PESADO
# ============================================================

def encontrar_mas_pesado_de_agua_recursivo(lista, indice, mas_pesado_hasta_ahora):
    """
    Busca el pokémon de tipo Agua más pesado usando RECURSIVIDAD.
    Devuelve el pokémon más pesado, o None si no hay pokémones de agua.
    """
    # Caso base: llegamos al final de la lista
    if indice == len(lista):
        return mas_pesado_hasta_ahora

    pokemon_actual = lista[indice]

    # Verificamos si es de tipo Agua
    if pokemon_actual[TIPO].lower() == "agua":
        # Si todavía no tenemos un candidato, este es el primero
        if mas_pesado_hasta_ahora is None:
            mas_pesado_hasta_ahora = pokemon_actual
        # Si el actual pesa más, lo reemplazamos
        elif pokemon_actual[PESO] > mas_pesado_hasta_ahora[PESO]:
            mas_pesado_hasta_ahora = pokemon_actual

    # Llamada recursiva con el siguiente índice
    return encontrar_mas_pesado_de_agua_recursivo(lista, indice + 1, mas_pesado_hasta_ahora)


def ver_pokemon_agua_mas_pesado(lista):
    """Muestra el pokémon de tipo Agua más pesado de la lista"""
    print("\n POKÉMON DE AGUA MÁS PESADO")

    # Arrancamos la búsqueda desde el índice 0 y sin candidato todavía
    mas_pesado = encontrar_mas_pesado_de_agua_recursivo(lista, 0, None)

    if mas_pesado is None:
        print("\n No hay pokémones de tipo Agua en la lista.")
    else:
        print(f"\n El pokémon de agua más pesado es:")
        mostrar_pokemon(mas_pesado)


# ============================================================
# OPCIÓN 6 - POKÉMON CON MÁS FUERZA DE ATAQUE
# ============================================================

def ver_pokemon_mas_fuerte(lista):
    """Muestra el pokémon con mayor fuerza de ataque"""
    print("\n  POKÉMON CON MÁS FUERZA DE ATAQUE")

    if len(lista) == 0:
        print("\n No hay pokémones en la lista.")
        return

    # Arrancamos asumiendo que el primero es el más fuerte
    mas_fuerte = lista[0]

    for pokemon in lista:
        if pokemon[FUERZA_ATAQUE] > mas_fuerte[FUERZA_ATAQUE]:
            mas_fuerte = pokemon

    print(f"\n El pokémon con más fuerza de ataque es:")
    mostrar_pokemon(mas_fuerte)


# ============================================================
# OPCIÓN 7 - LISTAR POKÉMONES POR REGIÓN
# ============================================================

def listar_por_region(lista):
    """
    Le pide al usuario una región y muestra
    todos los pokémones que pertenecen a ella.
    """
    print("\n LISTAR POKÉMONES POR REGIÓN")
    mostrar_linea_separadora()

    # Obtenemos todas las regiones únicas que hay en la lista
    regiones_disponibles = []
    for pokemon in lista:
        if pokemon[REGION] not in regiones_disponibles:
            regiones_disponibles.append(pokemon[REGION])

    print(f"  Regiones disponibles: {', '.join(regiones_disponibles)}")
    region_buscada = input("  Ingresá la región que querés ver: ").strip().capitalize()

    # Buscamos los pokémones de esa región
    pokemones_encontrados = []
    for pokemon in lista:
        if pokemon[REGION].lower() == region_buscada.lower():
            pokemones_encontrados.append(pokemon)

    if len(pokemones_encontrados) == 0:
        print(f"\n No se encontraron pokémones de la región '{region_buscada}'.")
    else:
        print(f"\n Pokémones de la región {region_buscada} ({len(pokemones_encontrados)} encontrados):\n")
        for pokemon in pokemones_encontrados:
            mostrar_pokemon(pokemon)


# ============================================================
# FUNCIÓN PRINCIPAL - MENÚ
# ============================================================

def main():
    """
    Función principal que muestra el menú y
    llama a la función correspondiente según la opción del usuario.
    """
    print("\n  ¡Bienvenido al sistema de la Liga Pokémon!")
    print("  El Profesor Oak te da la bienvenida.")

    continuar = True

    while continuar:
        mostrar_menu()
        opcion = input("\n  Elegí una opción (1-8): ").strip()

        if opcion == "1":
            listar_todos(lista_pokemon)

        elif opcion == "2":
            agregar_pokemon(lista_pokemon)

        elif opcion == "3":
            eliminar_pokemon(lista_pokemon)

        elif opcion == "4":
            ordenar_por_nombre_z_a(lista_pokemon)

        elif opcion == "5":
            ver_pokemon_agua_mas_pesado(lista_pokemon)

        elif opcion == "6":
            ver_pokemon_mas_fuerte(lista_pokemon)

        elif opcion == "7":
            listar_por_region(lista_pokemon)

        elif opcion == "8":
            print("\n ¡Hasta la próxima, entrenador! ¡Atrápelos a todos!")
            continuar = False

        else:
            print("\n Opción inválida. Por favor elegí un número del 1 al 8.")


# ============================================================
# Punto de entrada del programa
# ============================================================
main()
