# ================= FUNCIONES GENERALES =================

def pedir_numero():
    return int(input("Ingrese un número: "))

def mostrar_numero(num):
    print("Número:", num)

def es_par(num):
    return num % 2 == 0

def pedir_numero_en_rango(desde, hasta):
    while True:
        num = int(input(f"Ingrese un número entre {desde} y {hasta}: "))
        if desde <= num <= hasta:
            return num
        print("Error, fuera de rango.")

def pedir_operacion():
    while True:
        op = input("Ingrese operación (s = sumar, r = restar): ").lower()
        if op in ['s', 'r']:
            return op
        print("Error, operación inválida.")

def realizar_descuento(valor):
    return valor * 0.95

def calcular(a, b, op):
    if op == 's':
        return a + b
    return a - b

# ================= RESTAR (EJ 3-5) =================

def restar1(a, b):
    return a - b

def restar2():
    a = pedir_numero()
    b = pedir_numero()
    return a - b

def restar3(a, b):
    print("Resultado:", a - b)

def restar4():
    a = pedir_numero()
    b = pedir_numero()
    print("Resultado:", a - b)

# ================= EJERCICIOS =================

def ejercicio_3_1():
    num = pedir_numero()
    mostrar_numero(num)

def ejercicio_3_2():
    num = pedir_numero()
    print("Número ingresado:", num)

def ejercicio_3_3():
    num = pedir_numero()
    if es_par(num):
        print("Es par")
    else:
        print("Es impar")

def ejercicio_3_4():
    num = pedir_numero_en_rango(1, 100)
    mostrar_numero(num)

def ejercicio_3_5():
    print("Restar1:", restar1(10, 5))
    print("Restar2:", restar2())
    restar3(8, 3)
    restar4()

def ejercicio_3_6():
    num = pedir_numero_en_rango(10, 100)
    resultado = realizar_descuento(num)
    print("Valor con descuento:", resultado)

def ejercicio_3_7():
    num1 = pedir_numero_en_rango(10, 100)
    num2 = pedir_numero_en_rango(10, 100)
    op = pedir_operacion()
    resultado = calcular(num1, num2, op)
    print("Resultado:", resultado)

# ================= MENÚ =================

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Ejercicio 3-1")
        print("2. Ejercicio 3-2")
        print("3. Ejercicio 3-3")
        print("4. Ejercicio 3-4")
        print("5. Ejercicio 3-5")
        print("6. Ejercicio 3-6")
        print("7. Ejercicio 3-7")
        print("0. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            ejercicio_3_1()
        elif opcion == "2":
            ejercicio_3_2()
        elif opcion == "3":
            ejercicio_3_3()
        elif opcion == "4":
            ejercicio_3_4()
        elif opcion == "5":
            ejercicio_3_5()
        elif opcion == "6":
            ejercicio_3_6()
        elif opcion == "7":
            ejercicio_3_7()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

# ================= PROGRAMA PRINCIPAL =================

menu()  
