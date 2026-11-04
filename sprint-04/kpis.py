#!/usr/bin/env python3
"""Herramientas internas de TurisData: KPIs de reservas a partir de un CSV.   (PLANTILLA)

Uso cuando esté terminado:
    python kpis.py reservas_turisdata.csv salida.json --capacidad 40

El reto se hace en DOS FASES. Cada función tiene una marca que dice cuándo toca:

    FASE 1 · martes · misión 3   →  tasa_cancelacion_por_canal, ingreso_medio_por_reserva, ocupacion_proxy
                                    (trabajas con reservas ya en memoria, sin ficheros)
                                    Prueba:  python test_kpis.py 1
    FASE 2 · miércoles · misiones 4 y 5  →  _convertir_fila, leer_reservas, exportar_json, main
                                    (ficheros, errores y JSON)
                                    Prueba:  python test_kpis.py 2

Tu trabajo: sustituir cada `raise NotImplementedError` por código que haga lo que dice el docstring.
Los comentarios «Paso» te dicen en qué orden pensarlo; el código lo escribes tú.
Ve función a función y ejecuta las pruebas después de cada una: verás qué pruebas ya pasan.
Solo se permite la biblioteca estándar (csv, json, argparse, datetime...). La versión con pandas es opcional.
"""
import argparse
import csv
import json
import sys
from datetime import date

COLUMNAS_OBLIGATORIAS = ["fecha_llegada", "noches", "precio_noche", "canal", "cancelada"]


# ════════════════════════════════════════════════════════════════════════════════════════════════
#  FASE 1 · MARTES · MISIÓN 3 · Funciones que calculan   (las reservas ya están en memoria)
#  Una reserva es un diccionario: {"fecha_llegada": date, "noches": int, "precio_noche": float,
#                                   "canal": str, "cancelada": 0 o 1}.   Las reservas son una lista de ellos.
# ════════════════════════════════════════════════════════════════════════════════════════════════

def tasa_cancelacion_por_canal(reservas):
    """Devuelve {canal: porcentaje de reservas canceladas, con 1 decimal}."""
    total = {}
    canceladas = {}
    for r in reservas:
        canal = r["canal"]
        total[canal] = total.get(canal, 0) + 1
        if r["cancelada"] == 1:
            canceladas[canal] = canceladas.get(canal, 0) + 1
    tasas = {}
    for canal in total:
        tasas[canal] = round(100 * canceladas.get(canal, 0) / total[canal], 1)
    return tasas

    # Paso 1: crea dos diccionarios vacíos: total = {} (reservas por canal) y canceladas = {} (canceladas por canal).
    # Paso 2: recorre las reservas con un for; por cada una, suma 1 al total de su canal
    #         y, si cancelada vale 1, suma 1 a las canceladas de su canal.  (Pista: total.get(canal, 0) + 1)
    # Paso 3: construye y devuelve el diccionario con el porcentaje de cada canal: round(100 * ... / ..., 1)
    raise NotImplementedError("TODO (misión 3): tasa_cancelacion_por_canal")


def ingreso_medio_por_reserva(reservas):
    """Ingreso medio de las reservas NO canceladas, con 2 decimales."""
    ingresos = []
    for r in reservas:
        if r["cancelada"] == 0:
            ingresos.append(r["noches"] * r["precio_noche"])
    if not ingresos:
        return 0.0
    return round(sum(ingresos) / len(ingresos), 2)

    # Paso 1: crea una lista vacía y añade noches * precio_noche de cada reserva que NO esté cancelada.
    # Paso 2: si la lista está vacía, devuelve 0.0.
    # Paso 3: si no, devuelve la media con 2 decimales:  round(sum(lista) / len(lista), 2)
    raise NotImplementedError("TODO (misión 3): ingreso_medio_por_reserva")


def ocupacion_proxy(reservas, capacidad_habitaciones):
    """Ocupación aproximada en %, con 1 decimal."""
    if capacidad_habitaciones <= 0:
        raise ValueError("La capacidad debe ser mayor que 0")
    if not reservas:
        return 0.0
    fechas = []
    for r in reservas:
        fechas.append(r["fecha_llegada"])
    dias = (max(fechas) - min(fechas)).days + 1
    noches = 0
    for r in reservas:
        if r["cancelada"] == 0:
            noches = noches + r["noches"]
    return round(100 * noches / (dias * capacidad_habitaciones), 1)

  
def calcular_kpis(reservas, capacidad_habitaciones):
    """Reúne los KPIs en un diccionario con estas claves (ya montado para ti):"""
    return {
        "reservas_analizadas": len(reservas),
        "ocupacion_proxy_pct": ocupacion_proxy(reservas, capacidad_habitaciones),
        "ingreso_medio_por_reserva": ingreso_medio_por_reserva(reservas),
        "tasa_cancelacion_por_canal_pct": tasa_cancelacion_por_canal(reservas),
    }


# ════════════════════════════════════════════════════════════════════════════════════════════════
#  FASE 2 · MIÉRCOLES · MISIÓN 4 · Leer el CSV
# ════════════════════════════════════════════════════════════════════════════════════════════════

def _convertir_fila(fila):
    """Convierte una fila de textos a tipos Python. Lanza ValueError si no es válida."""
    noches = int(fila["noches"])
    precio = float(fila["precio_noche"])
    cancelada = int(fila["cancelada"])
    fecha = date.fromisoformat(fila["fecha_llegada"])
    canal = fila["canal"].strip()

    if canal == "":
        raise ValueError("canal vacío")
    if noches < 1:
        raise ValueError("noches debe ser >= 1")
    if precio <= 0:
        raise ValueError("precio_noche debe ser > 0")
    if cancelada not in (0, 1):
        raise ValueError("cancelada debe ser 0 o 1")

    return {"fecha_llegada": fecha, "noches": noches, "precio_noche": precio,
            "canal": canal, "cancelada": cancelada}


def leer_reservas(ruta):
    """Lee el CSV y devuelve (reservas, avisos)."""
    try:
        with open(ruta, newline="", encoding="utf8") as f:
            lector = csv.DictReader(f)

            faltan = []                                            # 5.4
            for columna in COLUMNAS_OBLIGATORIAS:
                if columna not in lector.fieldnames:
                    faltan.append(columna)
            if faltan:
                raise ValueError(f"Faltan columnas obligatorias: {faltan}")

            reservas = []                                          # 5.5
            avisos = []

            for n, fila in enumerate(lector, start=2):             # 5.6
                try:
                    reservas.append(_convertir_fila(fila))
                except ValueError as error:
                    avisos.append(f"Fila {n} descartada: {error}")

            return reservas, avisos                                # 5.7
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encuentra el fichero: {ruta}")   # 5.8


# ════════════════════════════════════════════════════════════════════════════════════════════════
#  FASE 2 · MIÉRCOLES · MISIÓN 5 · Guardar y entregar
# ════════════════════════════════════════════════════════════════════════════════════════════════

def exportar_json(datos, ruta):
    """Guarda `datos` en un fichero JSON legible."""
    with open(ruta, "w", encoding="utf8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)


def main(argumentos=None):
    """Punto de entrada: devuelve 0 si todo va bien y 1 si hay un error."""
    parser = argparse.ArgumentParser(description="KPIs de reservas de TurisData")
    parser.add_argument("entrada", help="CSV de reservas")
    parser.add_argument("salida", help="JSON de salida")
    parser.add_argument("--capacidad", type=int, default=40, help="habitaciones disponibles (proxy de ocupación)")
    args = parser.parse_args(argumentos)
    try:
        reservas, avisos = leer_reservas(args.entrada)                                       # 3.4
        kpis = calcular_kpis(reservas, args.capacidad)                                       # 3.5
        kpis["calidad"] = {"filas_validas": len(reservas), "filas_descartadas": len(avisos),
                           "avisos": avisos[:20]}                                            # 3.6
        exportar_json(kpis, args.salida)                                                     # 3.7
    except (FileNotFoundError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)                                            # 3.8
        return 1
    print(f"OK: {len(reservas)} reservas analizadas, {len(avisos)} descartadas -> {args.salida}")   # 3.9
    return 0


if __name__ == "__main__":
    sys.exit(main())
