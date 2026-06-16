import csv
from datetime import datetime
from collections import defaultdict
# Reemplazar los diccionarios anidados clásicos por collections.defaultdict nos ahorra todas las líneas de código donde preguntabas if año not in resultados:. El defaultdict crea la clave automáticamente si no existe.
import matplotlib.pyplot as plt

# ---- (1) IMPORTACIÓN + LIMPIEZA DE DATOS ------------------------------------

registros = []

with open("gastos_raw_v.1.csv", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    lector.fieldnames = [f.strip() for f in lector.fieldnames]

    for fila in lector:
        if not fila["gasto"] or not fila["fecha"]:
            continue

        fecha = datetime.strptime(fila["fecha"], "%d/%m/%Y")
        
        # Creamos la clave de mes directamente aquí para ahorrar trabajo después
        clave_mes = f"{fecha.year}-{fecha.month:02d}"

        registros.append({
            "mes_clave": clave_mes,
            "categoria": fila["concepto"],
            "gasto": float(fila["gasto"].replace(",", "."))
        })

# ---- (2) AGRUPACIÓN (Usando defaultdict) ------------------------------------

# Defaultdict(float) inicializa automáticamente cualquier clave nueva en 0.0

gastos_por_mes_cat = defaultdict(lambda: defaultdict(float))
totales_por_mes = defaultdict(float)

for r in registros:
    mes = r["mes_clave"]
    cat = r["categoria"]
    gasto = r["gasto"]
    
    gastos_por_mes_cat[mes][cat] += gasto
    totales_por_mes[mes] += gasto

# ---- (3) PREPARATIVOS PARA GRÁFICOS -----------------------------------------

# Extraemos meses únicos ordenados y categorías únicas de forma eficiente

meses = sorted(set(r["mes_clave"] for r in registros))
categorias = set(r["categoria"] for r in registros) 

# Bucles comprimido en una sola línea: "Recorre cada diccionario (r) dentro de la lista registros y extrae únicamente el valor que está guardado bajo la clave 'mes_clave' y 'categoria'"
# set(...): estructura de datos matemática que, por su propia naturaleza, no admite valores duplicados. Al envolver esa lista gigante con set(), Python automáticamente destruye cualquier categoría repetida de forma instantánea.

# ---- (4) DIBUJAR ------------------------------------------------------------

for categoria in categorias:

# List comprehension: armamos la serie de valores en una sola línea para que matplotlib pueda graficarlos. La lista valores_cat contiene los gastos de la categoría actual para cada mes en meses.

    valores_cat = [gastos_por_mes_cat[mes][categoria] for mes in meses]
    
    plt.plot(meses, valores_cat, label=categoria)

plt.legend()
plt.xlabel("Tiempo: Meses")
plt.ylabel("Gastos: Euros")
plt.title("Evolución de Gastos")
plt.show()

# ---- (5) ANÁLISIS -----------------------------------------------------------

# Extraemos los totales en una lista plana para facilitar el cálculo
totales = [totales_por_mes[mes] for mes in meses]

# Promedio (usando funciones nativas de Python)
promedio = sum(totales) / len(totales)
print(f"Gasto promedio mensual: {promedio:.2f}")

# Acumulado (Running Total)
acumulado = []
suma = 0
for gasto in totales:
    suma += gasto
    acumulado.append(suma)

plt.plot(meses, acumulado, label="ACUMULADO")
plt.legend()
plt.title("Gasto Acumulado")
plt.show()

# Comparación mes a mes (MoM %)
print("\nVariación Mes a Mes (MoM %):")
for i in range(1, len(totales)):
    anterior = totales[i - 1]
    actual = totales[i]
    variacion = ((actual - anterior) / anterior) * 100
    
    print(f"{meses[i-1]} -> {meses[i]}: {variacion:.2f}%")