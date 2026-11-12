# Laboratorio 02 - Algoritmos: deteccion de duplicados
# Integrantes:
# - Erick Steven Estrada Morales
# - Nahomy Isabel Cisneros Guamaní
# Estrategias distintas a las diapositivas: count() y sorted() + vecinos.
# Ejecutar en Python 3: python laboratorio2_duplicados.py

import csv
import platform
import random
import sys
import time

DATOS_EJEMPLO = [8, 3, 12, 8, 5, 9, 3, 20]
TAMANOS = [100, 500, 1000, 2000, 5000]
REPETICIONES = 3


def algoritmo_conteo(datos, registrar=False):
    """Detecta valores repetidos con list.count() sin usar set ni doble for."""
    duplicados = []
    tabla = []
    for i, valor in enumerate(datos):
        veces = datos.count(valor)
        ya_guardado = valor in duplicados
        accion = ("No repetido" if veces == 1 else
                  "Ya registrado" if ya_guardado else "Agregar duplicado")
        if veces > 1 and not ya_guardado:
            duplicados.append(valor)
        if registrar:
            tabla.append([i + 1, i, valor, veces,
                          "Si" if veces > 1 else "No",
                          "Si" if ya_guardado else "No",
                          accion, str(duplicados),
                          len(datos), (i + 1) * len(datos)])
    return duplicados, tabla


def algoritmo_ordenado(datos, registrar=False):
    """Ordena una copia y compara elementos vecinos; no altera el original."""
    ordenados = sorted(datos)
    duplicados = []
    tabla = []
    for i in range(1, len(ordenados)):
        anterior, actual = ordenados[i - 1], ordenados[i]
        iguales = anterior == actual
        if iguales and (not duplicados or duplicados[-1] != actual):
            duplicados.append(actual)
            accion = "Agregar duplicado"
        elif iguales:
            accion = "Ya registrado"
        else:
            accion = "Distintos"
        if registrar:
            tabla.append([i, i, anterior, actual,
                          "Si" if iguales else "No",
                          accion, str(duplicados), 1, i])
    return duplicados, tabla


def medir(funcion, datos, repeticiones=3):
    """Mide SOLO el calculo, sin imprimir ni construir tablas de iteraciones."""
    tiempos_ms = []
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        funcion(datos, registrar=False)
        fin = time.perf_counter()
        tiempos_ms.append((fin - inicio) * 1000)
    return tiempos_ms


def datos_de_prueba(n, escenario):
    """Mismas entradas reproducibles para los dos algoritmos."""
    rng = random.Random(20261112 + n)
    datos = rng.sample(range(n * 12), n)
    if escenario == "Con duplicado" and n >= 2:
        datos[-1] = datos[0]
    return datos


def exportar_csv(nombre, columnas, filas):
    with open(nombre, "w", newline="", encoding="utf-8-sig") as f:
        escritor = csv.writer(f, delimiter=";")
        escritor.writerow(columnas)
        escritor.writerows(filas)


def mostrar_tabla(titulo, encabezados, filas):
    columnas = list(zip(encabezados, *filas))
    anchos = [max(len(str(dato)) for dato in columna) for columna in columnas]
    def imprimir(fila):
        return " | ".join(str(dato).ljust(ancho)
                          for dato, ancho in zip(fila, anchos))
    print("\n" + titulo)
    print(imprimir(encabezados))
    print("-" * len(imprimir(encabezados)))
    for fila in filas:
        print(imprimir(fila))


def ejecutar():
    h1 = ["Iteracion", "Posicion", "Numero", "Veces",
          "Repetido", "Ya guardado", "Accion", "Duplicados",
          "Inspecciones count aprox.", "Inspecciones acumuladas"]
    h2 = ["Iteracion", "Indice", "Anterior", "Actual",
          "Iguales", "Accion", "Duplicados",
          "Comparacion vecinos", "Comparaciones acumuladas"]
    dup_a, tabla_a = algoritmo_conteo(DATOS_EJEMPLO, registrar=True)
    dup_b, tabla_b = algoritmo_ordenado(DATOS_EJEMPLO, registrar=True)
    mostrar_tabla("ALGORITMO A: count()", h1[:8], [fila[:8] for fila in tabla_a])
    mostrar_tabla("ALGORITMO B: sorted() + vecinos", h2[:7],
                  [fila[:7] for fila in tabla_b])
    print("\nResultado A:", dup_a, "| Resultado B:", dup_b)
    exportar_csv("iteraciones_count.csv", h1, tabla_a)
    exportar_csv("iteraciones_sorted.csv", h2, tabla_b)
    h_benchmark = ["n", "Escenario", "Algoritmo", "Repeticion 1 (ms)",
                   "Repeticion 2 (ms)", "Repeticion 3 (ms)",
                   "Promedio (ms)", "Vueltas del ciclo",
                   "Trabajo estimado (modelo)", "Duplicados", "Correcto"]
    resultados = []
    for escenario in ["Sin duplicados", "Con duplicado"]:
        for n in TAMANOS:
            datos = datos_de_prueba(n, escenario)
            res_a, _ = algoritmo_conteo(datos)
            res_b, _ = algoritmo_ordenado(datos)
            correcto = sorted(res_a) == sorted(res_b)
            for nombre, funcion in [("A - count()", algoritmo_conteo),
                                    ("B - sorted()", algoritmo_ordenado)]:
                duraciones = medir(funcion, datos, REPETICIONES)
                resultados.append([
                    n, escenario, nombre,
                    *[round(x, 6) for x in duraciones],
                    round(sum(duraciones) / len(duraciones), 6),
                    n if nombre.startswith("A") else max(0, n - 1),
                    n * n if nombre.startswith("A") else "O(n log n)",
                    len(res_a) if nombre.startswith("A") else len(res_b),
                    "Si" if correcto else "No",
                ])
    exportar_csv("benchmark_laboratorio2.csv", h_benchmark, resultados)
    print("\nBANCO DE PRUEBAS (tres repeticiones por caso)")
    print("Python:", sys.version.split()[0], "|", platform.platform())
    print("CSV generados: iteraciones_count.csv, iteraciones_sorted.csv,"
          " benchmark_laboratorio2.csv")
    return tabla_a, tabla_b, resultados


if __name__ == "__main__":
    ejecutar()
