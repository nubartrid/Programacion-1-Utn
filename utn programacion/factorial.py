def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 42)

# uso
num = int(input("Ingrese un número: "))

if num < 0:
    print("No existe fibonacci para numeros negativos.")
else:
    print("Fibonacci:", fibonacci(num))


    
    
    #return num * factorial(num - 1)