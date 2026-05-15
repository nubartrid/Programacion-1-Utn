
# EJERCICIO 1

def contar_vocales(cadena):

    matriz = [
        ["a", 0],
        ["e", 0],
        ["i", 0],
        ["o", 0],
        ["u", 0]
    ]

    cadena = cadena.lower()

    for caracter in cadena:

        if caracter == "a":
            matriz[0][1] += 1

        elif caracter == "e":
            matriz[1][1] += 1

        elif caracter == "i":
            matriz[2][1] += 1

        elif caracter == "o":
            matriz[3][1] += 1

        elif caracter == "u":
            matriz[4][1] += 1

    return matriz


texto = "murcielaguito"

resultado = contar_vocales(texto)

for fila in resultado:

    print(fila[0], fila[1])


# EJERCICIO 2

def buscar_caracter(cadena, caracter):

    for i in range(len(cadena)):

        if cadena[i] == caracter:

            return i

    return -1


texto = "Hola"

print(buscar_caracter(texto, "l"))


# EJERCICIO 3

def es_palindromo(cadena):

    cadena = cadena.lower()

    if cadena == cadena[::-1]:

        return True

    return False


print(es_palindromo("neuquen"))


# EJERCICIO 4

def suprimir_repetidos(cadena):

    nueva = ""

    for caracter in cadena:

        if caracter not in nueva:

            nueva += caracter

    return nueva


print(suprimir_repetidos("Hooola"))


# EJERCICIO 5

def eliminar_vocales(cadena):

    nueva = ""

    for caracter in cadena:

        if caracter.lower() not in "aeiou":

            nueva += caracter

    return nueva


print(eliminar_vocales("Hola"))


# EJERCICIO 6

def contar_subcadena(cadena, subcadena):

    contador = 0

    for i in range(len(cadena)):

        if cadena[i:i+len(subcadena)] == subcadena:

            contador += 1

    return contador


texto = "El pan del panadero"

print(contar_subcadena(texto, "pan"))