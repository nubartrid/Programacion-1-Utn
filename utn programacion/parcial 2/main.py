from archivos import cargar_datos, guardar_datos
from funciones import (
    listar_por_raza,
    modificar_personaje,
    eliminar_personaje,
    ordenar_lista,
    personaje_mas_tecnicas,
    personaje_menos_transformaciones
)

# Cargo los datos del json al iniciar el programa
personajes = cargar_datos()

def mostrar_menu():
    print("""
==============================
   CAPSULE CORP - ANALISIS
==============================
1. Listar personajes por raza
2. Modificar un personaje
3. Eliminar un personaje
4. Ordenar lista de personajes
5. Personaje con mas tecnicas
6. Personaje con menos transformaciones
7. Salir
==============================""")

# Bucle principal del programa

salir = False
while not salir:
    mostrar_menu()
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        listar_por_raza(personajes)
    elif opcion == "2":
        modificar_personaje(personajes)
    elif opcion == "3":
        eliminar_personaje(personajes)
    elif opcion == "4":
        ordenar_lista(personajes)
    elif opcion == "5":
        personaje_mas_tecnicas(personajes)
    elif opcion == "6":
        personaje_menos_transformaciones(personajes)
    elif opcion == "7":
        guardar_datos(personajes)
        print("Hasta luego!")
        salir = True
    else:
        print("Opcion no valida, intente de nuevo.")
