
import csv
import os

#  EJERCICIO 1

def ordenar_por_nombre_asc(nombres: list, edades: list) -> tuple[list, list]:
    """
    Ordena las listas Nombres y Edades por nombre de manera ascendente.
    Retorna las dos listas ordenadas manteniendo la correspondencia.
    """
    pares = list(zip(nombres, edades))
    pares_ordenados = sorted(pares, key=lambda x: x[0].lower())
    nombres_ord, edades_ord = zip(*pares_ordenados) if pares_ordenados else ([], [])
    return list(nombres_ord), list(edades_ord)


#  EJERCICIO 2

def ordenar_por_nombre_asc_puntos_desc(nombres: list, puntos: list) -> tuple[list, list]:
    """
    Ordena las listas Nombres y Puntos:
      - Primero por nombre ascendente.
      - Si el nombre es igual, por puntos descendente.
    """
    pares = list(zip(nombres, puntos))
    pares_ordenados = sorted(pares, key=lambda x: (x[0].lower(), -x[1]))
    nombres_ord, puntos_ord = zip(*pares_ordenados) if pares_ordenados else ([], [])
    return list(nombres_ord), list(puntos_ord)


#  EJERCICIO 3

def ordenar_apellido_nombre_nota(
    estudiantes: list, apellidos: list, notas: list
) -> tuple[list, list, list]:
    """
    Ordena las listas por:
      1. Apellido ascendente.
      2. Si el apellido es igual → nombre ascendente.
      3. Si el nombre también es igual → nota descendente.
    """
    ternas = list(zip(apellidos, estudiantes, notas))
    ternas_ordenadas = sorted(
        ternas,
        key=lambda x: (x[0].lower(), x[1].lower(), -x[2])
    )
    apellidos_ord, nombres_ord, notas_ord = zip(*ternas_ordenadas) if ternas_ordenadas else ([], [], [])
    return list(nombres_ord), list(apellidos_ord), list(notas_ord)


#  EJERCICIO 4 – Importación y filtros de usuarios

# Columnas esperadas en el CSV (case-insensitive al leer)
COLUMNAS = ["nombre", "mail", "telefono", "edad", "pais", "codigo_postal"]


def importar_listas(ruta_csv: str) -> list[dict]:
    """
    Lee un archivo CSV y devuelve una lista de dicts con los datos de usuarios.
    Campos esperados: nombre, mail, telefono, edad, pais, codigo_postal.
    """
    if not os.path.exists(ruta_csv):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_csv}")

    usuarios = []
    with open(ruta_csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            # Normalizar claves a minúsculas y sin espacios
            fila_norm = {k.strip().lower(): v.strip() for k, v in fila.items()}
            usuario = {
                "nombre":        fila_norm.get("nombre", ""),
                "mail":          fila_norm.get("mail", ""),
                "telefono":      fila_norm.get("telefono", ""),
                "edad":          int(fila_norm.get("edad", 0)),
                "pais":          fila_norm.get("pais", ""),
                "codigo_postal": int(fila_norm.get("codigo_postal", 0)),
            }
            usuarios.append(usuario)
    return usuarios

def _cabecera(titulo: str) -> None:
    sep = "─" * 70
    print(f"\n{sep}")
    print(f"  {titulo}")
    print(sep)


def _imprimir_usuario(u: dict, campos: list[str] | None = None) -> None:
    """Imprime los campos indicados de un usuario (o todos si campos=None)."""
    if campos is None:
        campos = COLUMNAS
    partes = [f"{c.capitalize()}: {u[c]}" for c in campos if c in u]
    print("  |  ".join(partes))


# ── Opciones de menú

def listar_mexico(usuarios: list[dict]) -> None:
    """Opción 2: Todos los datos de usuarios de México."""
    _cabecera("Usuarios de México")
    resultado = [u for u in usuarios if u["pais"].lower() == "mexico"
                 or u["pais"].lower() == "méxico"]
    if not resultado:
        print("  Sin resultados.")
    for u in resultado:
        _imprimir_usuario(u)


def listar_brasil_nombre_mail_tel(usuarios: list[dict]) -> None:
    """Opción 3: Nombre, mail y teléfono de usuarios de Brasil."""
    _cabecera("Nombre, mail y teléfono de usuarios de Brasil")
    resultado = [u for u in usuarios if u["pais"].lower() == "brasil"
                 or u["pais"].lower() == "brazil"]
    if not resultado:
        print("  Sin resultados.")
    for u in resultado:
        _imprimir_usuario(u, ["nombre", "mail", "telefono"])


def listar_mas_jovenes(usuarios: list[dict]) -> None:
    """Opción 4: Todos los datos del/los usuario/s más joven/es."""
    _cabecera("Usuario/s más joven/es")
    if not usuarios:
        print("  Sin datos.")
        return
    min_edad = min(u["edad"] for u in usuarios)
    resultado = [u for u in usuarios if u["edad"] == min_edad]
    for u in resultado:
        _imprimir_usuario(u)


def promedio_edad(usuarios: list[dict]) -> None:
    """Opción 5: Promedio de edad de todos los usuarios."""
    _cabecera("Promedio de edad de usuarios")
    if not usuarios:
        print("  Sin datos.")
        return
    prom = sum(u["edad"] for u in usuarios) / len(usuarios)
    print(f"  Promedio de edad: {prom:.2f} años  (sobre {len(usuarios)} usuarios)")


def mayor_edad_brasil(usuarios: list[dict]) -> None:
    """Opción 6: Datos del usuario de mayor edad de Brasil."""
    _cabecera("Usuario de mayor edad en Brasil")
    brasil = [u for u in usuarios if u["pais"].lower() in ("brasil", "brazil")]
    if not brasil:
        print("  Sin usuarios de Brasil.")
        return
    max_edad = max(u["edad"] for u in brasil)
    resultado = [u for u in brasil if u["edad"] == max_edad]
    for u in resultado:
        _imprimir_usuario(u)


def listar_mexico_brasil_cp_mayor_8000(usuarios: list[dict]) -> None:
    """Opción 7: Usuarios de México y Brasil con código postal > 8000."""
    _cabecera("Usuarios de México y Brasil con código postal > 8000")
    resultado = [
        u for u in usuarios
        if u["pais"].lower() in ("mexico", "méxico", "brasil", "brazil")
        and u["codigo_postal"] > 8000
    ]
    if not resultado:
        print("  Sin resultados.")
    for u in resultado:
        _imprimir_usuario(u)


def listar_italianos_mayores_40(usuarios: list[dict]) -> None:
    """Opción 8: Nombre, mail y teléfono de italianos mayores de 40 años."""
    _cabecera("Italianos mayores de 40 años (nombre, mail, teléfono)")
    resultado = [
        u for u in usuarios
        if u["pais"].lower() in ("italia", "italy") and u["edad"] > 40
    ]
    if not resultado:
        print("  Sin resultados.")
    for u in resultado:
        _imprimir_usuario(u, ["nombre", "mail", "telefono"])


def listar_mexico_ord_nombre(usuarios: list[dict]) -> None:
    """Opción 9: Datos de usuarios de México ordenados por nombre ascendente."""
    _cabecera("Usuarios de México ordenados por nombre (ASC)")
    resultado = [u for u in usuarios if u["pais"].lower() in ("mexico", "méxico")]
    resultado_ord = sorted(resultado, key=lambda u: u["nombre"].lower())
    if not resultado_ord:
        print("  Sin resultados.")
    for u in resultado_ord:
        _imprimir_usuario(u)


def listar_mas_jovenes_ord_edad_nombre(usuarios: list[dict]) -> None:
    """
    Opción 10: Usuario/s más joven/es ordenados por edad ASC;
    si la edad se repite, por nombre ASC.
    """
    _cabecera("Usuario/s más joven/es (ordenados por edad ASC, nombre ASC)")
    if not usuarios:
        print("  Sin datos.")
        return
    min_edad = min(u["edad"] for u in usuarios)
    resultado = [u for u in usuarios if u["edad"] == min_edad]
    resultado_ord = sorted(resultado, key=lambda u: (u["edad"], u["nombre"].lower()))
    for u in resultado_ord:
        _imprimir_usuario(u)


def listar_mexico_brasil_cp8000_ord_nombre_edad_desc(usuarios: list[dict]) -> None:
    """
    Opción 11: Usuarios de México y Brasil con código postal > 8000,
    ordenados por nombre DESC y edad DESC.
    """
    _cabecera("Usuarios de México/Brasil con CP > 8000 (nombre DESC, edad DESC)")
    resultado = [
        u for u in usuarios
        if u["pais"].lower() in ("mexico", "méxico", "brasil", "brazil")
        and u["codigo_postal"] > 8000
    ]
    resultado_ord = sorted(
        resultado,
        key=lambda u: (u["nombre"].lower(), u["edad"]),
        reverse=True
    )
    if not resultado_ord:
        print("  Sin resultados.")
    for u in resultado_ord:
        _imprimir_usuario(u)