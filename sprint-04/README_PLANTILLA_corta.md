# Herramientas internas · TurisData Canarias

> **README corto** para la entrega en nivel mínimo con explicación. Cópialo como `README.md`, sustituye lo que está entre `<...>` y borra este aviso. Si tu equipo llega más lejos, usa `README_PLANTILLA.md`.

**Equipo:** Error404 · **Fecha:** 04/11/2026

## Qué hace

El programa utiliza un archivo CSV que contiene 6.000 reservas turísticas con información como las fechas de reserva y llegada, el número de noches, los huéspedes, el tipo de habitación, el canal de reserva, el precio por noche y si la reserva ha sido cancelada.

Con estos datos, el programa calcula indicadores (KPIs), como la tasa de cancelación por canal y el ingreso medio por reserva, y guarda los resultados en un archivo JSON para poder analizarlos y consultarlos fácilmente.

## Cómo se ejecuta y se prueba

```
python kpis.py reservas_turisdata.csv salida.json --capacidad 40
python test_kpis.py
```

Resultado de las pruebas: \<12 de 12 superadas\>

## Quién hizo qué

| Parte | La escribí yo | La copié y la expliqué |
| :---- | :---- | :---- |
| `tasa_cancelacion_por_canal` e `ingreso_medio_por_reserva` | todas | todas |
| `_convertir_fila` y `leer_reservas` | todas | todas |
| `exportar_json` y `main` | todas | todas |

Explicación de una función

\<Elige una función y explica con tus palabras, línea a línea, qué hace y por qué. Cinco o seis líneas.\>

**Función: `leer_reservas`**

1. Primero, la función recibe la ruta del archivo CSV que contiene las reservas.  
2. Después, abre el fichero para poder leer su contenido.  
3. Comprueba que estén presentes las columnas obligatorias para trabajar con los datos.  
4. Lee las filas del archivo y utiliza `_convertir_fila` para transformar cada una en datos que pueda utilizar el programa.  
5. Si encuentra alguna fila incorrecta, la descarta para evitar que provoque errores.  
6. Finalmente, devuelve las reservas que se han podido leer correctamente.

Esta función es importante porque permite cargar y comprobar los datos antes de calcular los indicadores.

## Errores que controla

\<Qué pasa si el fichero no existe, falta una columna o una fila viene mal; qué mensaje da.\>

`ERROR: No se encuentra el fichero: no_existe.csv`&nbsp;

`ERROR: Faltan columnas obligatorias: ['precio_noche']` (código `1`)&nbsp;

`OK: 5998 reservas analizadas, 2 descartadas -> salida_prueba.json` (código `0`)&nbsp;

## Uso de IA

No hemos usado IA

## Qué mejoraríamos

Nada