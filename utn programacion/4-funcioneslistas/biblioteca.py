from listas_personas import *
import random


# =========================
# EJERCICIO 1
# =========================

def cargar_nombres():

    lista = []

    for i in range(10):

        nombre = input(f"Ingrese el nombre {i+1}: ")

        while nombre.isalpha() == False:

            nombre = input("Error. Ingrese solo letras: ")

        lista.append(nombre)

    return lista


# =========================
# EJERCICIO 2
# =========================

def cargar_numeros():

    lista = [0] * 10

    posicion = random.randint(0, 9)

    numero = int(input("Ingrese un número: "))

    lista[posicion] = numero

    return lista


# =========================
# EJERCICIO 3
# =========================

def cargar_rango(minimo, maximo):

    lista = []

    for i in range(10):

        numero = int(input(f"Ingrese número entre {minimo} y {maximo}: "))

        while numero < minimo or numero > maximo:

            numero = int(input("Error. Reingrese: "))

        lista.append(numero)

    return lista


# =========================
# EJERCICIO 4
# =========================

def buscar_numero(lista, numero):

    return numero in lista


# =========================
# EJERCICIO 5
# =========================

def buscar_menores(lista_nombres, lista_edades):

    menor = min(lista_edades)

    for i in range(len(lista_edades)):

        if lista_edades[i] == menor:

            print(lista_nombres[i], lista_edades[i])


# =========================
# MENU OPCION 2
# =========================

def usuarios_mexico():

    for i in range(len(country)):

        if country[i] == "Mexico":

            print(nombres[i], edades[i], country[i])


# =========================
# MENU OPCION 3
# =========================

def usuarios_brasil():

    for i in range(len(country)):

        if country[i] == "Brazil":

            print(nombres[i], mails[i], telefonos[i])


# =========================
# MENU OPCION 4
# =========================

def usuarios_mas_jovenes():

    menor = min(edades)

    for i in range(len(edades)):

        if edades[i] == menor:

            print(nombres[i], edades[i])


# =========================
# MENU OPCION 5
# =========================

def promedio_edades():

    promedio = sum(edades) / len(edades)

    print("Promedio:", promedio)


# =========================
# MENU OPCION 6
# =========================

def brasil_mayor_edad():

    mayor = -1
    indice = -1

    for i in range(len(country)):

        if country[i] == "Brazil":

            if edades[i] > mayor:

                mayor = edades[i]
                indice = i

    print(nombres[indice], edades[indice])


# =========================
# MENU OPCION 7
# =========================

def mexico_brasil_cp():

    for i in range(len(country)):

        if (country[i] == "Mexico" or country[i] == "Brazil") and postalZip[i] > 8000:

            print(nombres[i], country[i], postalZip[i])


# =========================
# MENU OPCION 8
# =========================

def italianos_mayores_40():

    for i in range(len(country)):

        if country[i] == "Italy" and edades[i] > 40:

            print(nombres[i], mails[i], telefonos[i])