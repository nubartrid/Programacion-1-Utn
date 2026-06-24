import json

ARCHIVO = "dragon_ball.json"

def cargar_datos():
    archivo = open(ARCHIVO, "r", encoding="utf-8")
    datos = json.load(archivo)
    archivo.close()
    return datos

def guardar_datos(lista):
    archivo = open(ARCHIVO, "w", encoding="utf-8")
    json.dump(lista, archivo, ensure_ascii=False, indent=4)
    archivo.close()
    print("Cambios guardados en el archivo.")
