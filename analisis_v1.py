# versión picapiedra sin código embebido. Todo a mano: explícito y literal. Sin pandas, numpy, funciones, clases, objetos, módulos, librerías externas, etc. Solo Python puro y duro.

import csv
# cvs es un módulo de Python que permite trabajar con archivos CSV (Comma Separated Values), que son archivos de texto plano donde cada línea representa un registro y los campos están separados por comas (u otro delimitador).

from datetime import datetime

# ---- (1) IMPORTACIÓN + LIMPIEZA DE DATOS.------------------------------------

# uso UTF-8 para asegurarme de que se lean correctamente los caracteres especiales (el archivo viene de excel y puede tener acentos, eñes, etc.)

with open("gastos_raw_v.1.csv", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

# DictReader: ese objeto no es una lista, es un iterador! 
# limpio los espacios en blanco de las claves para evitar problemas de acceso a los campos del diccionario
    
    lector.fieldnames = [f.strip() for f in lector.fieldnames]

# ---- (2) CREACIÓN DE MODELO MAESTRO.-----------------------------------------

# representación completa y cruda de los datos ya interpretados
# en registros guardo cada fila del archivo CSV como un diccionario para posterior manipulación.

    registros = []

    for fila in lector:

        if not fila["gasto"]:
            continue

# todavia no tengo un manejo de errores, entonces si no hay fecha o gasto, simplemente salto esa fila. Luego voy a agregar validaciones para asegurarme de que los datos sean correctos.

        fecha_raw = fila["fecha"]

        if not fecha_raw:
            continue

        fecha = datetime.strptime(fecha_raw, "%d/%m/%Y")

        registro = {
            "fecha": fecha,
            "año": fecha.year,
            "mes": fecha.month,
            "dia": fecha.day,
            "concepto": fila["concepto"],
            "detalle": fila["detalles"],
            "gasto": float(
                fila["gasto"].replace(",", ".")
            )
        }

        registros.append(registro)

# ---- (3) AGRUPACIÓN DE DATOS.------------------------------------------------
# transformación de granularidad: de microdatos a resumen por dimensión (macroestructura)
# por ahora armo el diccionario primitivamente. Luego usaré la herramienta embebida defaultdict
resultados = {}

for r in registros:

    año = r["año"]
    mes = r["mes"]
    categoria = r["concepto"]
    gasto = r["gasto"]

    if año not in resultados:
        resultados[año] = {}

    if mes not in resultados[año]:
        resultados[año][mes] = {}

    if categoria not in resultados[año][mes]:
        resultados[año][mes][categoria] = 0

    resultados[año][mes][categoria] += gasto

# ---- (3.b) tabla plana (flat table).-----------------------------------------
# “pre-proceso los datos para que el gráfico solo consuma estructura lista”
# lista de diccionarios: cada diccionario representa una fila de la tabla, con claves como "año", "mes", "categoria" y "gasto". Esta estructura es más fácil de manipular para análisis posteriores, como cálculos de promedios, acumulados o comparaciones mes a mes.

tabla = []

for año in resultados:
    for mes in resultados[año]:
        for categoria in resultados[año][mes]:

            fila = {
                "año": año,
                "mes": mes,
                "categoria": categoria,
                "gasto": resultados[año][mes][categoria]
            }

            tabla.append(fila)

# ---- (4) PREPARATIVOS PARA GRÁFICOS.-----------------------------------------
# Paso 1: obtener categorías únicas

categorias = []

for fila in tabla:

    categoria = fila["categoria"]

    if categoria not in categorias:
        categorias.append(categoria)

print(categorias)

# Paso 2: obtener meses únicos

meses = []

for fila in tabla:

    clave_mes = f"{fila['año']}-{fila['mes']:02d}"

    if clave_mes not in meses:
        meses.append(clave_mes)

meses.sort()

print(meses)

# Paso 3: construir una serie para cada categoría
# esto es una batata computacional, pero está bueno para entender cómo se construyen las series de tiempo a partir de los datos agrupados. Después usaré pandas para hacer esto de manera más eficiente.

categoria = "movi"

valores = []

for mes in meses:

    gasto_mes = 0

    for fila in tabla:

        fila_mes = f"{fila['año']}-{fila['mes']:02d}"

        if (
            fila_mes == mes
            and fila["categoria"] == categoria
        ):
            gasto_mes = fila["gasto"]

    valores.append(gasto_mes)

print(valores)

categoria = "alqui"

valores = []

for mes in meses:

    gasto_mes = 0

    for fila in tabla:

        fila_mes = f"{fila['año']}-{fila['mes']:02d}"

        if (
            fila_mes == mes
            and fila["categoria"] == categoria
        ):
            gasto_mes = fila["gasto"]

    valores.append(gasto_mes)

print(valores)

categoria = "resto"

valores = []

for mes in meses:

    gasto_mes = 0

    for fila in tabla:

        fila_mes = f"{fila['año']}-{fila['mes']:02d}"

        if (
            fila_mes == mes
            and fila["categoria"] == categoria
        ):
            gasto_mes = fila["gasto"]

    valores.append(gasto_mes)

print(valores)

categoria = "morfi"

valores = []

for mes in meses:

    gasto_mes = 0

    for fila in tabla:

        fila_mes = f"{fila['año']}-{fila['mes']:02d}"

        if (
            fila_mes == mes
            and fila["categoria"] == categoria
        ):
            gasto_mes = fila["gasto"]

    valores.append(gasto_mes)

print(valores)

categoria = "varios"

valores = []

for mes in meses:

    gasto_mes = 0

    for fila in tabla:

        fila_mes = f"{fila['año']}-{fila['mes']:02d}"

        if (
            fila_mes == mes
            and fila["categoria"] == categoria
        ):
            gasto_mes = fila["gasto"]

    valores.append(gasto_mes)

print(valores)

categoria = "servi"

valores = []

for mes in meses:

    gasto_mes = 0

    for fila in tabla:

        fila_mes = f"{fila['año']}-{fila['mes']:02d}"

        if (
            fila_mes == mes
            and fila["categoria"] == categoria
        ):
            gasto_mes = fila["gasto"]

    valores.append(gasto_mes)

print(valores)

categoria = "salud"

valores = []

for mes in meses:

    gasto_mes = 0

    for fila in tabla:

        fila_mes = f"{fila['año']}-{fila['mes']:02d}"

        if (
            fila_mes == mes
            and fila["categoria"] == categoria
        ):
            gasto_mes = fila["gasto"]

    valores.append(gasto_mes)

print(valores)

totales = []

for mes in meses:

    total_mes = 0

    for fila in tabla:

        fila_mes = f"{fila['año']}-{fila['mes']:02d}"

        if fila_mes == mes:
            total_mes += fila["gasto"]

    totales.append(total_mes)

for mes, total in zip(meses, totales):
    print(mes, total)

# ---- (5) DIBUJAR.------------------------------------------------------------
# El bloque gigante de extracciones individuales, hoy por hoy, no alimenta al gráfico en absoluto. El paso 5 es un ecosistema totalmente autosuficiente.

import matplotlib.pyplot as plt

for categoria in categorias:

    valores = []

    for mes in meses:

        gasto_mes = 0

        for fila in tabla:

            fila_mes = f"{fila['año']}-{fila['mes']:02d}"

            if (
                fila_mes == mes
                and fila["categoria"] == categoria
            ):
                gasto_mes = fila["gasto"]

        valores.append(gasto_mes)

    plt.plot(
        meses,
        valores,
        label=categoria
    )

# el total no lo grafico porque resta claridad al gráfico, pero lo dejo comentado para que se vea cómo se haría si quisiera graficarlo.

# # plt.plot(
# meses,
# totales,
# label="TOTAL"
# )

plt.legend()

plt.xlabel("Mes")
plt.ylabel("Euros")

plt.show()

# ---- (6) ANÁLISIS.-----------------------------------------------------------

# Gasto promedio por mes
suma_total = 0

for gasto in totales:
    suma_total += gasto

promedio = suma_total / len(totales)

print(promedio)

# Acumulado (Running Total)
acumulado = []

suma = 0

for gasto in totales:

    suma += gasto

    acumulado.append(suma)

print(acumulado)

plt.plot(
    meses,
    acumulado,
    label="ACUMULADO"
)

# Comparación mes a mes (MoM %)
mom = []

for i in range(1, len(totales)):

    anterior = totales[i - 1]
    actual = totales[i]

    variacion = (
        (actual - anterior)
        / anterior
    ) * 100

    mom.append(variacion)

print(mom)

for i in range(1, len(meses)):
    print(meses[i], mom[i - 1])

