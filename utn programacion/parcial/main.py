from heroes import lista_heroes

# ─────────────────────────────────────────────────────────────
#  ÍNDICES DE LA LISTA
# ─────────────────────────────────────────────────────────────

I_NOMBRE      = 0
I_IDENTIDAD   = 1
I_EMPRESA     = 2
I_ALTURA      = 3
I_PESO        = 4
I_GENERO      = 5
I_COLOR_OJOS  = 6
I_COLOR_PELO  = 7
I_FUERZA      = 8
I_INTELIGENCIA= 9

# ─────────────────────────────────────────────────────────────
#  CONSTANTES DE VALIDACIÓN
# ─────────────────────────────────────────────────────────────
EMPRESAS_VALIDAS     = ["DC Comics", "Marvel Comics"]
GENEROS_VALIDOS      = ["M", "F", "NB"]
INTELIGENCIAS_VALIDAS= ["low", "average", "good", "high", "genius"]

SEPARADOR       = "═" * 60
SEP_DELGADO     = "─" * 60


# ─────────────────────────────────────────────────────────────
#  HELPERS DE PRESENTACIÓN
# ─────────────────────────────────────────────────────────────
def titulo(texto):
    print(SEPARADOR)
    print(f"   {texto}")
    print(SEPARADOR)


def mostrar_heroe(heroe, numero=None):
    """Muestra todos los datos de un héroe de forma amena."""
    genero_texto = {"M": "Masculino", "F": "Femenino", "NB": "No binario"}
    prefijo = f"  [{numero}]" if numero is not None else " "
    print(SEP_DELGADO)
    print(f"{prefijo} {heroe[I_NOMBRE]}  |  {heroe[I_EMPRESA]}")
    print(SEP_DELGADO)
    print(f"   Identidad     : {heroe[I_IDENTIDAD]}")
    print(f"   Género        : {genero_texto.get(heroe[I_GENERO], heroe[I_GENERO])}")
    print(f"   Altura        : {heroe[I_ALTURA]} cm")
    print(f"   Peso          : {heroe[I_PESO]} kg")
    print(f"   Color de ojos : {heroe[I_COLOR_OJOS]}")
    print(f"   Color de pelo : {heroe[I_COLOR_PELO]}")
    print(f"   Fuerza        : {heroe[I_FUERZA]}")
    print(f"   Inteligencia  : {heroe[I_INTELIGENCIA].capitalize()}")


# ─────────────────────────────────────────────────────────────
#  HELPERS DE VALIDACIÓN / INPUT
# ─────────────────────────────────────────────────────────────
def pedir_string_no_vacio(mensaje):
    """Solicita un string hasta que no esté vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  Este campo no puede estar vacío. Intentá de nuevo.")


def pedir_empresa():
    """Muestra las empresas válidas y retorna la elegida."""
    while True:
        print("   Empresas disponibles:")
        for x, emp in enumerate(EMPRESAS_VALIDAS, 1):
            print(f"     {x}. {emp}")
        opcion = input("   Seleccioná una opción (1 / 2): ").strip()
        if opcion == "1":
            return EMPRESAS_VALIDAS[0]
        if opcion == "2":
            return EMPRESAS_VALIDAS[1]
        print("   Opción inválida. Ingresá 1 o 2.")


def pedir_float_positivo(mensaje):
    """Solicita un número flotante mayor a 0."""
    while True:
        try:
            valor = float(input(mensaje).strip())
            if valor > 0:
                return valor
            print("   El valor debe ser mayor a 0.")
        except ValueError:
            print("   Ingresá un número válido (ej: 185.5).")


def pedir_numero_positivo(mensaje):
    """Solicita un número entero mayor a 0."""
    while True:
        try:
            valor = int(input(mensaje).strip())
            if valor > 0:
                return valor
            print("   El valor debe ser mayor a 0.")
        except ValueError:
            print("   Ingresá un número entero válido.")


def pedir_genero():
    """Solicita el género hasta ingresar uno válido."""
    while True:
        genero = input("   Género (M / F / NB): ").strip().upper()
        if genero in GENEROS_VALIDOS:
            return genero
        print(f"  Géneros válidos: {', '.join(GENEROS_VALIDOS)}.")


def pedir_inteligencia():
    """Muestra los niveles válidos y retorna el elegido."""
    while True:
        print("   Niveles disponibles: " + " | ".join(INTELIGENCIAS_VALIDAS))
        intel = input("   Inteligencia: ").strip().lower()
        if intel in INTELIGENCIAS_VALIDAS:
            return intel
        print("   Nivel inválido. Revisá las opciones disponibles.")


# ─────────────────────────────────────────────────────────────
#  OPCIÓN 2 — LISTAR HÉROES
# ─────────────────────────────────────────────────────────────
def listar_heroes():
    titulo("LISTA COMPLETA DE HÉROES")
    if not lista_heroes:
        print("   La lista de héroes está vacía.")
        return
    for i, heroe in enumerate(lista_heroes, 1):
        mostrar_heroe(heroe, numero=i)
    print(SEP_DELGADO)
    print(f"   Total de héroes: {len(lista_heroes)}")
    print()


# ─────────────────────────────────────────────────────────────
#  OPCIÓN 3 — AGREGAR HÉROE
# ─────────────────────────────────────────────────────────────
def agregar_heroe():
    titulo("AGREGAR NUEVO HÉROE")
    print("   Completá los datos del nuevo héroe:\n")

    nombre       = pedir_string_no_vacio("   Nombre          : ")
    identidad    = pedir_string_no_vacio("   Identidad        : ")
    empresa      = pedir_empresa()
    altura       = pedir_float_positivo( "   Altura (cm)      : ")
    peso         = pedir_float_positivo( "   Peso (kg)        : ")
    genero       = pedir_genero()
    color_ojos   = pedir_string_no_vacio("   Color de ojos    : ")
    color_pelo   = pedir_string_no_vacio("   Color de pelo    : ")
    fuerza       = pedir_numero_positivo("   Fuerza           : ")
    inteligencia = pedir_inteligencia()

    nuevo_heroe = [
        nombre, identidad, empresa, altura, peso,
        genero, color_ojos, color_pelo, fuerza, inteligencia
    ]

    lista_heroes.append(nuevo_heroe)
    print(f"\n   ¡{nombre} fue agregado/a exitosamente a la lista!")


# ─────────────────────────────────────────────────────────────
#  OPCIÓN 4 — ELIMINAR HÉROE POR NOMBRE
# ─────────────────────────────────────────────────────────────
def eliminar_heroe():
    titulo("ELIMINAR HÉROE")
    if not lista_heroes:
        print("   La lista de héroes está vacía.")
        return

    nombre_buscar = input("   Ingresá el nombre del héroe a eliminar: ").strip()

    heroe_encontrado = None
    for heroe in lista_heroes:
        if heroe[I_NOMBRE].lower() == nombre_buscar.lower():
            heroe_encontrado = heroe
            break

    if heroe_encontrado is None:
        print(f"  No se encontró ningún héroe con el nombre '{nombre_buscar}'.")
        return

    print("\n   Héroe encontrado:")
    mostrar_heroe(heroe_encontrado)
    confirmacion = input("\n   ¿Confirmar eliminación? (s / n): ").strip().lower()

    if confirmacion == "s":
        lista_heroes.remove(heroe_encontrado)
        print(f"\n  {heroe_encontrado[I_NOMBRE]} fue eliminado/a de la lista.")
    else:
        print("   Operación cancelada.")


# ─────────────────────────────────────────────────────────────
#  OPCIÓN 5 — ORDENAR POR NOMBRE (A → Z)
# ─────────────────────────────────────────────────────────────
def ordenar_heroes():
    titulo("ORDENAR HÉROES POR NOMBRE (A → Z)")
    if not lista_heroes:
        print("   La lista de héroes está vacía.")
        return

    # Bubble sort alfabético por nombre (índice 0)
    n = len(lista_heroes)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista_heroes[j][I_NOMBRE].lower() > lista_heroes[j + 1][I_NOMBRE].lower():
                lista_heroes[j], lista_heroes[j + 1] = lista_heroes[j + 1], lista_heroes[j]

    print("  Lista ordenada correctamente de la A a la Z.")
    print("\n   Vista rápida del nuevo orden:")
    print(SEP_DELGADO)
    for i, heroe in enumerate(lista_heroes, 1):
        print(f"   {i}. {heroe[I_NOMBRE]}  ({heroe[I_EMPRESA]})")
    print(SEP_DELGADO)


# ─────────────────────────────────────────────────────────────
#  OPCIÓN 6 — HÉROE MÁS ALTO
# ─────────────────────────────────────────────────────────────
def heroe_mas_alto():
    titulo("HÉROE MÁS ALTO")
    if not lista_heroes:
        print("   La lista de héroes está vacía.")
        return

    mas_alto = lista_heroes[0]
    for heroe in lista_heroes[1:]:
        if heroe[I_ALTURA] > mas_alto[I_ALTURA]:
            mas_alto = heroe

    print(f"\n   El héroe más alto es {mas_alto[I_NOMBRE]} con {mas_alto[I_ALTURA]} cm.\n")
    mostrar_heroe(mas_alto)
    print()


# ─────────────────────────────────────────────────────────────
#  OPCIÓN 7 — HÉROE MÁS FUERTE
# ─────────────────────────────────────────────────────────────
def heroe_mas_fuerte():
    titulo("HÉROE MÁS FUERTE")
    if not lista_heroes:
        print("   La lista de héroes está vacía.")
        return

    mas_fuerte = lista_heroes[0]
    for heroe in lista_heroes[1:]:
        if heroe[I_FUERZA] > mas_fuerte[I_FUERZA]:
            mas_fuerte = heroe

    print(f"\n   El héroe más fuerte es {mas_fuerte[I_NOMBRE]} con fuerza {mas_fuerte[I_FUERZA]}.\n")
    mostrar_heroe(mas_fuerte)
    print()


# ─────────────────────────────────────────────────────────────
#  OPCIÓN 8 — HÉROE MÁS DELGADO / MENOS PESADO
# ─────────────────────────────────────────────────────────────
def heroe_menos_pesado():
    titulo("HÉROE MENOS PESADO")
    if not lista_heroes:
        print("   La lista de héroes está vacía.")
        return

    menos_pesado = lista_heroes[0]
    for heroe in lista_heroes[1:]:
        if heroe[I_PESO] < menos_pesado[I_PESO]:
            menos_pesado = heroe

    print(f"\n   El héroe menos pesado es {menos_pesado[I_NOMBRE]} con {menos_pesado[I_PESO]} kg.\n")
    mostrar_heroe(menos_pesado)
    print()


# ─────────────────────────────────────────────────────────────
#  MENÚ PRINCIPAL
# ─────────────────────────────────────────────────────────────
def mostrar_menu():
    print(SEPARADOR)
    print("        INDUSTRIAS STARK  —  DESAFÍO DE PROGRAMACIÓN")
    print(SEPARADOR)
    print("""   1. Importar lista de héroes
   2. Listar todos los héroes
   3. Agregar héroe
   4. Eliminar héroe por nombre
   5. Ordenar héroes por nombre (A → Z)
   6. Ver héroe más alto
   7. Ver héroe más fuerte
   8. Ver héroe menos pesado
   0. Salir""")
    print(SEPARADOR)


def main():
    importado = False

    while True:
        mostrar_menu()
        opcion = input("   Seleccioná una opción: ").strip()

        if opcion == "0":
            print("\n  ¡Hasta luego! Cerrando el sistema...\n")
            break

        elif opcion == "1":
            titulo("IMPORTAR LISTA DE HÉROES")
            if importado:
                print(f" La lista ya fue importada. Contiene {len(lista_heroes)} héroe/s.")
            else:
                importado = True
                print(f" Lista importada correctamente. Se cargaron {len(lista_heroes)} héroes.")

        elif opcion == "2":
            if not importado:
                print("\n  Primero debés importar la lista (opción 1).")
            else:
                listar_heroes()

        elif opcion == "3":
            if not importado:
                print("\n  Primero debés importar la lista (opción 1).")
            else:
                agregar_heroe()

        elif opcion == "4":
            if not importado:
                print("\n  Primero debés importar la lista (opción 1).")
            else:
                eliminar_heroe()

        elif opcion == "5":
            if not importado:
                print("\n  Primero debés importar la lista (opción 1).")
            else:
                ordenar_heroes()

        elif opcion == "6":
            if not importado:
                print("\n  Primero debés importar la lista (opción 1).")
            else:
                heroe_mas_alto()

        elif opcion == "7":
            if not importado:
                print("\n  Primero debés importar la lista (opción 1).")
            else:
                heroe_mas_fuerte()

        elif opcion == "8":
            if not importado:
                print("\n  Primero debés importar la lista (opción 1).")
            else:
                heroe_menos_pesado()

        else:
            print("\n     Opción inválida. Ingresá un número del 0 al 8.")

        input("\n   Presioná Enter para continuar...")

# ─────────────────────────────────────────────────────────────
#  PUNTO DE ENTRADA
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()