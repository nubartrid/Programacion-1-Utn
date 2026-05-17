
import sys
import os

# Aseguramos que la biblioteca se encuentre en el mismo directorio
sys.path.insert(0, os.path.dirname(__file__))

import biblioteca as bib

#  DATOS PARA EJERCICIOS 1, 2 y 3

NOMBRES_EJ1 = [
    "Ana", "Luis", "Juan", "Sol", "Roberto",
    "Sonia", "Ulises", "Sofia", "Maria", "Pedro",
    "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"
]
EDADES_EJ1 = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]

MATERIAS_EJ2 = [
    "Matematica", "Investigacion Operativa", "Ingles", "Literatura",
    "Ciencias Sociales", "Computacion", "Ingles", "Algebra",
    "Contabilidad", "Artistica", "Algoritmos", "Base de Datos",
    "Ergonomia", "Naturaleza"
]
PUNTOS_EJ2 = [100, 98, 56, 25, 87, 38, 64, 42, 28, 91, 66, 35, 49, 57, 98]

ESTUDIANTES_EJ3 = [
    "Ana", "Luis", "Juan", "Sol", "Roberto",
    "Sonia", "María", "Sofia", "Maria", "Pedro",
    "Antonio", "Eugenia", "Soledad", "Mario", "María"
]
APELLIDOS_EJ3 = [
    "Sosa", "Gutierrez", "Alsina", "Martinez", "Sosa",
    "Ramirez", "Perez", "Lopez", "Arregui", "Mitre",
    "Andrade", "Loza", "Antares", "Roca", "Perez"
]
NOTAS_EJ3 = [8, 4, 9, 10, 8, 6, 4, 8, 7, 5, 6, 7, 10, 4, 8]


#  HELPERS DE IMPRESIÓN

def separador(char: str = "═", ancho: int = 60) -> None:
    print(char * ancho)


def titulo(texto: str) -> None:
    separador()
    print(f"  {texto}")
    separador()


def imprimir_dos_columnas(lista1: list, lista2: list,
                           header1: str, header2: str) -> None:
    """Imprime dos listas alineadas en columnas."""
    print(f"  {'#':<4} {header1:<20} {header2}")
    print("  " + "-" * 45)
    for i, (v1, v2) in enumerate(zip(lista1, lista2), 1):
        print(f"  {i:<4} {str(v1):<20} {v2}")


def imprimir_tres_columnas(lista1: list, lista2: list, lista3: list,
                            h1: str, h2: str, h3: str) -> None:
    """Imprime tres listas alineadas en columnas."""
    print(f"  {'#':<4} {h1:<18} {h2:<18} {h3}")
    print("  " + "-" * 55)
    for i, (v1, v2, v3) in enumerate(zip(lista1, lista2, lista3), 1):
        print(f"  {i:<4} {str(v1):<18} {str(v2):<18} {v3}")


#  EJERCICIO 1

def ejercicio1() -> None:
    titulo("EJERCICIO 1 – Ordenamiento por Nombre (ASC)")

    print("\n  [Original]")
    imprimir_dos_columnas(NOMBRES_EJ1, EDADES_EJ1, "Nombre", "Edad")

    nombres_ord, edades_ord = bib.ordenar_por_nombre_asc(NOMBRES_EJ1, EDADES_EJ1)

    print("\n  [Ordenado por Nombre ASC]")
    imprimir_dos_columnas(nombres_ord, edades_ord, "Nombre", "Edad")

#  EJERCICIO 2

def ejercicio2() -> None:
    titulo("EJERCICIO 2 – Ordenamiento por Nombre (ASC) / Puntos (DESC)")

    print("\n  [Original]")
    imprimir_dos_columnas(MATERIAS_EJ2, PUNTOS_EJ2, "Materia", "Puntos")

    nombres_ord, puntos_ord = bib.ordenar_por_nombre_asc_puntos_desc(
        MATERIAS_EJ2, PUNTOS_EJ2
    )

    print("\n  [Ordenado: Nombre ASC, Puntos DESC si nombre igual]")
    imprimir_dos_columnas(nombres_ord, puntos_ord, "Materia", "Puntos")


#  EJERCICIO 3

def ejercicio3() -> None:
    titulo("EJERCICIO 3 – Ord. Apellido ASC / Nombre ASC / Nota DESC")

    print("\n  [Original]")
    imprimir_tres_columnas(
        ESTUDIANTES_EJ3, APELLIDOS_EJ3, NOTAS_EJ3,
        "Nombre", "Apellido", "Nota"
    )

    nombres_ord, apellidos_ord, notas_ord = bib.ordenar_apellido_nombre_nota(
        ESTUDIANTES_EJ3, APELLIDOS_EJ3, NOTAS_EJ3
    )

    print("\n  [Ordenado: Apellido ASC, Nombre ASC, Nota DESC]")
    imprimir_tres_columnas(
        nombres_ord, apellidos_ord, notas_ord,
        "Nombre", "Apellido", "Nota"
    )


#  EJERCICIO 4 – MENÚ

def mostrar_menu() -> None:
    separador("─")
    print("""           MENÚ DE OPCIONES – USUARIOS ONLINE
  ────────────────────────────────────────────────────
  1.  Importar listas
  2.  Listar datos de usuarios de México
  3.  Nombre, mail y teléfono de usuarios de Brasil
  4.  Datos del/los usuario/s más joven/es
  5.  Promedio de edad de los usuarios
  6.  Usuario de mayor edad de Brasil
  7.  Usuarios de México y Brasil con código postal > 8000
  8.  Nombre, mail y teléfono de italianos mayores de 40
  9.  Usuarios de México ordenados por nombre
  10. Usuario/s más joven/es ordenados (edad ASC, nombre ASC)
  11. México/Brasil CP > 8000 ordenado por nombre y edad DESC
  0.  Volver al menú principal""")
    separador("─")


def menu_ejercicio4() -> None:
    usuarios: list[dict] = []
    importado = False

    opciones_protegidas = {str(i) for i in range(2, 12)}

    while True:
        mostrar_menu()
        if not importado:
            print("  ⚠  Debe importar las listas primero (Opción 1).")
        opcion = input("\n  Ingrese una opción: ").strip()

        if opcion == "0":
            break

        if opcion in opciones_protegidas and not importado:
            print("\n   No se puede acceder a esta opción sin importar las listas.")
            input("  Presione Enter para continuar...")
            continue

        if opcion == "1":
            ruta = input("  Ingrese la ruta del archivo CSV [usuarios.csv]: ").strip()
            if not ruta:
                ruta = "usuarios.csv"
            try:
                usuarios = bib.importar_listas(ruta)
                importado = True
                print(f"\n  Se importaron {len(usuarios)} usuario/s correctamente.")
            except FileNotFoundError as e:
                print(f"\n  Error: {e}")
            except Exception as e:
                print(f"\n  Error inesperado al importar: {e}")

        elif opcion == "2":
            bib.listar_mexico(usuarios)

        elif opcion == "3":
            bib.listar_brasil_nombre_mail_tel(usuarios)

        elif opcion == "4":
            bib.listar_mas_jovenes(usuarios)

        elif opcion == "5":
            bib.promedio_edad(usuarios)

        elif opcion == "6":
            bib.mayor_edad_brasil(usuarios)

        elif opcion == "7":
            bib.listar_mexico_brasil_cp_mayor_8000(usuarios)

        elif opcion == "8":
            bib.listar_italianos_mayores_40(usuarios)

        elif opcion == "9":
            bib.listar_mexico_ord_nombre(usuarios)

        elif opcion == "10":
            bib.listar_mas_jovenes_ord_edad_nombre(usuarios)

        elif opcion == "11":
            bib.listar_mexico_brasil_cp8000_ord_nombre_edad_desc(usuarios)

        else:
            print("\n  ⚠  Opción no válida.")

        input("\n  Presione Enter para continuar...")


#  MENÚ PRINCIPAL

def menu_principal() -> None:
    while True:
        separador("═")
        print("       PROGRAMA DE ORDENAMIENTOS Y GESTIÓN DE USUARIOS")
        separador("═")
        print("  1. Ejercicio 1 – Ordenar por Nombre (ASC)")
        print("  2. Ejercicio 2 – Ordenar por Nombre ASC / Puntos DESC")
        print("  3. Ejercicio 3 – Ordenar Apellido / Nombre / Nota")
        print("  4. Ejercicio 4 – Menú de usuarios online")
        print("  0. Salir")
        separador("═")

        opcion = input("  Seleccione una opción: ").strip()

        if opcion == "0":
            print("\n  ¡Hasta luego!\n")
            break
        elif opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            menu_ejercicio4()
        else:
            print("\n   Opción no válida.")

        input("\n  Presione Enter para continuar...")


#  PUNTO DE ENTRADA

if __name__ == "__main__":
    menu_principal()