#1. Area rectángulo 
def area_rectangulo(base, altura):
    return base * altura


#  2. Area círculo
import math

def area_circulo(radio):
    return math.pi * (radio ** 2)


#  3. Par o impar (imprime) 
def par_o_impar_mensaje(num):
    if num % 2 == 0:
        print("Es par")
    else:
        print("Es impar")


#  4. Par o impar (retorna) 
def es_par(num):
    return num % 2 == 0


#  5. Maximo de tres 
def maximo(a, b, c):
    return max(a, b, c)


#  6. Potencia 
def potencia(base, exponente):
    return base ** exponente


#  7. Numero primo 
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


#  8. Mostrar primos hasta N 
def mostrar_primos_hasta(n):
    contador = 0
    for i in range(1, n + 1):
        if es_primo(i):
            print(i)
            contador += 1
    return contador


#  9. Tabla de multiplicar 
def tabla_multiplicar(num, inicio=1, fin=10):
    for i in range(inicio, fin + 1):
        print(f"{num} x {i} = {num * i}")


#  10. Pedir entero 
def pedir_entero():
    return int(input("Ingrese un número entero: "))


#  11. Pedir flotante 
def pedir_float():
    return float(input("Ingrese un número decimal: "))


#  12. Pedir cadena 
def pedir_cadena():
    return input("Ingrese un texto: ")


#  13. Versiones reutilizables con validación 
def pedir_entero_validado(minimo=None, maximo=None):
    while True:
        try:
            num = int(input("Ingrese un entero: "))
            if minimo is not None and num < minimo:
                print("Muy chico.")
                continue
            if maximo is not None and num > maximo:
                print("Muy grande.")
                continue
            return num
        except:
            print("Error, ingrese un número válido.")


def pedir_float_validado(minimo=None, maximo=None):
    while True:
        try:
            num = float(input("Ingrese un decimal: "))
            if minimo is not None and num < minimo:
                print("Muy chico.")
                continue
            if maximo is not None and num > maximo:
                print("Muy grande.")
                continue
            return num
        except:
            print("Error, ingrese un número válido.")


def pedir_cadena_validada(long_min=1):
    while True:
        texto = input("Ingrese texto: ")
        if len(texto) >= long_min:
            return texto
        print("Texto demasiado corto.")