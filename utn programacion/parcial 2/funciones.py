import copy


# Función para mostrar un personaje

def mostrar_personaje(personaje):
    print("-----------------------------")
    print("Nombre:         ", personaje["nombre"])
    print("Raza:           ", personaje["raza"])
    print("Nivel de poder: ", personaje["nivel_poder"])
    print("Planeta:        ", personaje["planeta"])
    print("Edad:           ", personaje["edad"])
    print("Alineacion:     ", personaje["alineacion"])
    print("Transformaciones:", len(personaje["transformaciones"]))
    for t in personaje["transformaciones"]:
        print("   -", t)
    print("Tecnicas:")
    for tec in personaje["tecnicas"]:
        print("   -", tec)
    print("-----------------------------")



# Listar personajes por raza

def listar_por_raza(lista):
    raza = input("Ingrese la raza a buscar: ")
    encontrados = 0
    for personaje in lista:
        if personaje["raza"].lower() == raza.lower():
            mostrar_personaje(personaje)
            encontrados += 1
    if encontrados == 0:
        print("No se encontraron personajes de esa raza.")



# Modificar un personaje

def modificar_personaje(lista):
    nombre = input("Ingrese el nombre del personaje a modificar: ")
    indice = -1
    for i in range(len(lista)):
        if lista[i]["nombre"].lower() == nombre.lower():
            indice = i
            break

    if indice == -1:
        print("No se encontro el personaje.")
        return

    print("Personaje encontrado:")
    mostrar_personaje(lista[indice])

    print("""¿Que caracteristica desea modificar?
    1 - Nivel de poder
    2 - Planeta
    3 - Edad
    4 - Alineacion""")

    opcion = input("Elija una opcion: ")

    if opcion == "1":
        nuevo = input("Nuevo nivel de poder: ")
        lista[indice]["nivel_poder"] = int(nuevo)
        print("Nivel de poder actualizado.")
    elif opcion == "2":
        nuevo = input("Nuevo planeta: ")
        lista[indice]["planeta"] = nuevo
        print("Planeta actualizado.")
    elif opcion == "3":
        nuevo = input("Nueva edad: ")
        lista[indice]["edad"] = int(nuevo)
        print("Edad actualizada.")
    elif opcion == "4":
        nuevo = input("Nueva alineacion (Heroe / Villano / Neutral): ")
        lista[indice]["alineacion"] = nuevo
        print("Alineacion actualizada.")
    else:
        print("Opcion no valida.")



# Eliminar un personaje por nombre

def eliminar_personaje(lista):
    nombre = input("Ingrese el nombre del personaje a eliminar: ")
    encontrado = False
    for i in range(len(lista)):
        if lista[i]["nombre"].lower() == nombre.lower():
            lista.pop(i)
            print("Personaje eliminado correctamente.")
            encontrado = True
            break
    if not encontrado:
        print("No se encontro el personaje.")



# Ordenar la lista por criterio (trabaja con una copia)

def ordenar_lista(lista):
    print("¿Por que criterio desea ordenar?")
    print("1 - Nombre")
    print("2 - Raza")
    print("3 - Edad")

    opcion = input("Elija una opcion: ")

    copia = copy.deepcopy(lista)

    if opcion == "1":
        # ordenamiento burbuja por nombre
        for i in range(len(copia) - 1):
            for j in range(len(copia) - 1 - i):
                if copia[j]["nombre"] > copia[j + 1]["nombre"]:
                    aux = copia[j]
                    copia[j] = copia[j + 1]
                    copia[j + 1] = aux
        print("Lista ordenada por nombre:")
    elif opcion == "2":
        # ordenamiento burbuja por raza
        for i in range(len(copia) - 1):
            for j in range(len(copia) - 1 - i):
                if copia[j]["raza"] > copia[j + 1]["raza"]:
                    aux = copia[j]
                    copia[j] = copia[j + 1]
                    copia[j + 1] = aux
        print("Lista ordenada por raza:")
    elif opcion == "3":
        # ordenamiento burbuja por edad
        for i in range(len(copia) - 1):
            for j in range(len(copia) - 1 - i):
                if copia[j]["edad"] > copia[j + 1]["edad"]:
                    aux = copia[j]
                    copia[j] = copia[j + 1]
                    copia[j + 1] = aux
        print("Lista ordenada por edad:")
    else:
        print("Opcion no valida.")
        return

    for personaje in copia:
        mostrar_personaje(personaje)



# Mostrar el personaje con más técnicas

def personaje_mas_tecnicas(lista):
    maximo = 0
    indice_max = 0
    for i in range(len(lista)):
        cantidad = len(lista[i]["tecnicas"])
        if cantidad > maximo:
            maximo = cantidad
            indice_max = i
    print("El personaje con mas tecnicas es:")
    mostrar_personaje(lista[indice_max])


# Mostrar el personaje con menos transformaciones

def personaje_menos_transformaciones(lista):
    minimo = len(lista[0]["transformaciones"])
    indice_min = 0
    for i in range(len(lista)):
        cantidad = len(lista[i]["transformaciones"])
        if cantidad < minimo:
            minimo = cantidad
            indice_min = i
    print("El personaje con menos transformaciones es:")
    mostrar_personaje(lista[indice_min])
