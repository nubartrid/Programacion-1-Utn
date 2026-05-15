from biblioteca import *

datos_cargados = False

while True:

    print("\n===== MENU =====")
    print("1- Importar listas")
    print("2- Usuarios de México")
    print("3- Usuarios de Brasil")
    print("4- Usuarios más jóvenes")
    print("5- Promedio de edades")
    print("6- Usuario de Brasil de mayor edad")
    print("7- México y Brasil con CP > 8000")
    print("8- Italianos mayores de 40")
    print("9- Salir")

    opcion = input("Ingrese opción: ")

    if opcion == "1":

        datos_cargados = True
        print("Listas importadas")

    elif opcion == "2":

        if datos_cargados:
            usuarios_mexico()
        else:
            print("Primero importe las listas")

    elif opcion == "3":

        if datos_cargados:
            usuarios_brasil()
        else:
            print("Primero importe las listas")

    elif opcion == "4":

        if datos_cargados:
            usuarios_mas_jovenes()
        else:
            print("Primero importe las listas")

    elif opcion == "5":

        if datos_cargados:
            promedio_edades()
        else:
            print("Primero importe las listas")

    elif opcion == "6":

        if datos_cargados:
            brasil_mayor_edad()
        else:
            print("Primero importe las listas")

    elif opcion == "7":

        if datos_cargados:
            mexico_brasil_cp()
        else:
            print("Primero importe las listas")

    elif opcion == "8":

        if datos_cargados:
            italianos_mayores_40()
        else:
            print("Primero importe las listas")

    elif opcion == "9":

        print("Programa finalizado")
        break

    else:

        print("Opción inválida")