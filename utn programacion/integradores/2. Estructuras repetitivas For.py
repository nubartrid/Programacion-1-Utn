def ejercicio1():
    for i in range(1, 11):
        print(i)

def ejercicio2():
    for i in range(10, 0, -1):
        print(i)

def ejercicio3():
    n = int(input("Ingrese un número: "))
    for i in range(0, n + 1):
        print(i)

def ejercicio4():
    n = int(input("Ingrese un número: "))
    for i in range(11):
        print(f"{n} x {i} = {n * i}")

def ejercicio5():
    suma = 0
    contador = 0

    for i in range(10):
        num = int(input("Ingrese un número (0 para cortar): "))
        if num == 0:
            break
        suma += num
        contador += 1

    if contador > 0:
        print("Suma:", suma)
        print("Promedio:", suma / contador)
    else:
        print("No se ingresaron números.")

def ejercicio6():
    for i in range(1, 11):
        if i % 3 == 0:
            print(i)

def ejercicio7():
    for i in range(1, 51):
        if i % 2 == 0:
            print(i)

def ejercicio8():
    n = int(input("Ingrese un número: "))
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def ejercicio9():
    n = int(input("Ingrese un número: "))
    contador = 0

    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
            contador += 1

    print("Cantidad de divisores:", contador)

def ejercicio10():
    n = int(input("Ingrese un número: "))
    es_primo = True

    if n < 2:
        es_primo = False
    else:
        for i in range(2, n):
            if n % i == 0:
                es_primo = False
                break

    if es_primo:
        print("Es primo")
    else:
        print("No es primo")

def ejercicio11():
    n = int(input("Ingrese un número: "))
    contador_primos = 0

    for num in range(2, n + 1):
        es_primo = True

        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                break

        if es_primo:
            print(num)
            contador_primos += 1

    print("Cantidad de primos:", contador_primos)


# MENÚ
while True:
    print("\n--- MENÚ ---")
    print("1 al 11 para elegir ejercicio")
    print("0 para salir")

    opcion = input("Opción: ")

    if opcion == "1":
        ejercicio1()
    elif opcion == "2":
        ejercicio2()
    elif opcion == "3":
        ejercicio3()
    elif opcion == "4":
        ejercicio4()
    elif opcion == "5":
        ejercicio5()
    elif opcion == "6":
        ejercicio6()
    elif opcion == "7":
        ejercicio7()
    elif opcion == "8":
        ejercicio8()
    elif opcion == "9":
        ejercicio9()
    elif opcion == "10":
        ejercicio10()
    elif opcion == "11":
        ejercicio11()
    elif opcion == "0":
        break
    else:
        print("Opción inválida")