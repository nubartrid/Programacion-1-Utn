def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

# lista de palabras
palabras = ["radar", "python", "neuquen", "hola"]

# recorrer la lista con for
for palabra in palabras:
    if es_palindromo(palabra):
        print(palabra, "es un palíndromo")
    else:
        print(palabra, "no es un palíndromo")