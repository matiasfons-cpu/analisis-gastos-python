ejercicio manual 100%

1\) googlesheet limpiado y convertido a csv

2\) 100% vscode (sin pandas)



## *Estructura del código:*

1. limpio los espacios en blanco de las claves (encabezado del CSV) para evitar problemas de acceso a los campos del diccionario
2. reemplazo las comas por puntos en el valor del gasto para convertirlo a un número decimal (float), ya que en algunos países se usa la coma como separador decimal.

3\. valores vacíos: las opciones son

&#x09;ignorarla

&#x09;tratarla como 0

&#x09;registrarla como error

4\. procesamiento de datos

5\. gráficos

&#x09;básicos de gastos x categoría

&#x09;pro: series temporales (gastos por mes)



CSV

&#x20;↓

leer\_csv()

&#x20;↓

registros



\--------------------------------



FILTROS



filtrar\_mes()

filtrar\_año()

filtrar\_categoria()

filtrar\_detalle()



\--------------------------------



AGREGADORES



agrupar\_por\_categoria()

agrupar\_por\_fecha()

agrupar\_por\_mes()

agrupar\_por\_detalle()



\--------------------------------



VISUALIZACIONES



pie\_chart()

line\_chart()

bar\_chart()





## **Primer ejercicio**

¿Cuánto gasté por categoría?

¿Cuánto gasté por semana?

¿Cuánto gasté por día?

¿Cuál fue el gasto más grande?

¿Cuántas compras hice?

¿Cuál fue el ticket promedio?

¿Cuántas veces fui al supermercado?

¿Cuánto representa cada categoría?



## **Segundo ejercicio**

Generar automáticamente un informe.

Por ejemplo:

RESUMEN MAYO

Gasto total: 2086€

Categoría principal:

VV (31%)

Categoría secundaria:

Morf (15%)

Mayor gasto:

Alquiler 700€

Cantidad de movimientos:

52



## **Tercer ejercicio**



podrías empezar a ver tendencias.



## **Cuarto ejercicio**



Generar gráficos.

Pero eso vendrá después.

