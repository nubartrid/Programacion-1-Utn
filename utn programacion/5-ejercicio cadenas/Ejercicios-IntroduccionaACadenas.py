
# EJERCICIO 1

def contar_letra(letra, cadena):

    contador = 0

    for caracter in cadena:

        if caracter == letra:
            contador += 1

    return contador


texto = input("Ingrese un texto: ")
letra = input("Ingrese una letra: ")

resultado = contar_letra(letra, texto)

print("La letra aparece", resultado, "veces")


# EJERCICIO 2

def recortar_cadena(cadena, inicio, fin):

    if inicio < 0 or fin >= len(cadena) or inicio > fin:
        return "Posiciones inválidas"

    return cadena[inicio:fin+1]


texto = input("\nIngrese una cadena: ")

inicio = int(input("Ingrese índice inicial: "))
fin = int(input("Ingrese índice final: "))

resultado = recortar_cadena(texto, inicio, fin)

print("Resultado:", resultado)


# EJERCICIO 3

def char_at(cadena, posicion):

    if posicion < 0 or posicion >= len(cadena):
        return "Posición inválida"

    return cadena[posicion]


texto = input("\nIngrese una cadena: ")

posicion = int(input("Ingrese posición: "))

resultado = char_at(texto, posicion)

print("Carácter:", resultado)