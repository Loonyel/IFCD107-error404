# Informe de calidad del dato · reservas\_sucio.csv

**Equipo:** Error404 · **Fecha:** 10/11/2026 · **Versión de los datos:** reservas\_sucio.csv (nº de filas: 1545, columnas: 18\)

## 1\. Resumen para el gerente (máx. 5 líneas)

- El fichero **no se puede usar tal cual**: 1 de cada 3 filas (506 de 1545\) tiene algún error de formato o de valor, y 1 de cada 5 tiene huecos en datos importantes.  
- Lo más grave: **precios imposibles** (0, −50 y 9999 €), **fechas escritas de dos formas** y **45 reservas repetidas**.  
- Todo se corrige con una función que se ejecuta siempre igual y no toca el fichero original: quedan 1500 reservas.  
- Con los datos limpios, un primer modelo acierta bastante más que adivinar (AUC 0,76 frente a 0,50), así que merece la pena seguir.

## 2\. Tabla de defectos

Los tres más graves van en **negrita**.

| Nº | Defecto | Columna(s) | Filas afectadas | Cómo lo detectamos | Causa probable | Tratamiento aplicado | Por qué (y riesgo) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | **Precios imposibles** (0, −50 y 9999\) | `precio_noche` | 8 | Se revisaron los valores mínimo y máximo con `describe()` y se filtraron los precios menores o iguales a 0 y superiores a 1000\. | Errores al introducir los datos o valores utilizados como marcadores.&nbsp; | Se sustituyeron por valores nulos, sin eliminar las filas. Posteriormente, el pipeline los completa utilizando la mediana.&nbsp; | Un precio como 9999 puede alterar los cálculos estadísticos y el escalado. Existe la posibilidad de que algún precio elevado sea real, por lo que conviene confirmarlo con el cliente.&nbsp; |
| 2 | **Fechas en dos formatos** (`2025-11-09` y `19/11/2024`) | `fecha_reserva` | 154 | Se localizaron los registros que contenían barras mediante `.str.contains("/").sum()` y se comprobó que podían interpretarse correctamente.&nbsp; | Los datos probablemente proceden de dos sistemas distintos.&nbsp; | Se interpretó cada formato por separado y después se unificaron las fechas.&nbsp; | Si no se corrige, el cálculo de la antelación puede ser incorrecto. También existe el riesgo de confundir el día con el mes, por lo que se verificó que las fechas estuvieran dentro del intervalo esperado (2024-01-01 a 2025-12-30).&nbsp; |
| 3 | **Filas duplicadas exactas** | todas | 45 | Se utilizó `crudo.duplicated().sum()` para identificar las filas idénticas.&nbsp; | Posibles exportaciones repetidas o envíos duplicados de información.&nbsp; | Se eliminaron las filas repetidas mediante `drop_duplicates()`.&nbsp; | Evita que una misma reserva aparezca tanto en los datos de entrenamiento como en los de prueba. El riesgo es bajo porque los registros duplicados eran exactamente iguales.&nbsp; |
| 4 | Precio con coma decimal (`93,5`) | `precio_noche` | 153 | Se buscaron los valores que contenían comas utilizando `.astype(str).str.contains(",").sum()`.&nbsp; | Configuración regional española de Excel.&nbsp; | Se sustituyó la coma por un punto y se convirtió la columna a formato numérico. | Este cambio es necesario para que los precios puedan utilizarse correctamente en los cálculos. No supone ningún riesgo si se realiza antes de aplicar los filtros.&nbsp; |
| 5 | Noches imposibles (0 y −2) | `noches` | 6 | Se contaron los registros cuyo valor era menor o igual a cero.&nbsp; | Errores durante la introducción o carga de los datos.&nbsp; | Los valores incorrectos se transformaron en nulos para que el pipeline los complete posteriormente.&nbsp; | Así se evita asignar valores inventados durante la limpieza inicial.&nbsp; |
| 6 | Antelación negativa (−3) | `antelacion_dias` | 5 | Se localizaron los valores negativos y se compararon con las fechas de reserva y llegada.&nbsp; | Los datos no coinciden con la secuencia temporal que deberían seguir.&nbsp; | Se volvió a calcular la antelación restando la fecha de reserva a la fecha de llegada.&nbsp; | Se pudieron corregir los cinco registros utilizando las fechas originales, que proporcionan información fiable.&nbsp; |
| 7 | Variantes de canal (`WEB_INTERMEDIARIA`, `Web Intermediaria`, `directo`…) | `canal` | 135 | Se utilizó `value_counts()` y se encontraron 9 categorías diferentes cuando realmente deberían existir 4\.&nbsp; | Introducción de texto libre y diferencias en la forma de escribir los canales.&nbsp; | Se normalizaron los textos convirtiéndolos a minúsculas y eliminando espacios y guiones bajos.&nbsp; | De esta manera, el modelo reconoce correctamente los cuatro canales existentes, en lugar de interpretarlos como nueve categorías distintas.&nbsp; |
| 8 | Variantes de país (`es`, `España`, `uk`, `Reino Unido`) | `pais_origen` | 94 | Se revisaron las frecuencias con `value_counts()` y aparecieron 12 variantes en lugar de los 8 países esperados.&nbsp; | Diferencias de escritura e introducción manual de los datos.&nbsp; | Se creó un diccionario para unificar los nombres y códigos equivalentes de cada país.&nbsp; | Se evita que un mismo país aparezca representado de varias maneras. También se comprobó que ningún país válido quedara convertido accidentalmente en nulo.&nbsp; |
| 9 | Nulos en país, régimen y adultos | `pais_origen`, `regimen`, `adultos` | 115 · 61 · 46 | Se utilizó `isna().sum()` para contar los valores ausentes de cada columna.&nbsp; | Son campos opcionales que no siempre se rellenan. Esto también explica que `adultos` tenga valores decimales.&nbsp; | Los valores nulos se conservaron durante la limpieza. El pipeline se encarga de completarlos utilizando la moda para las variables categóricas y la mediana para las numéricas.&nbsp; | No se imputan antes de dividir los datos para evitar que se produzca una fuga de información entre entrenamiento y prueba.&nbsp; |
| 10 | Nulos en precio | `precio_noche` | 84 | Se contabilizaron los valores ausentes mediante `isna().sum()`.&nbsp; | Falta de información en el momento de registrar la reserva. | *El pipeline sustituye los valores ausentes utilizando la mediana de los precios.&nbsp;* | Después de la limpieza, los valores nulos aumentan de 84 a 87 debido a que los ocho precios imposibles se transformaron en nulos, aunque algunos registros ya estaban contabilizados como ausentes. |

Total de filas con algún defecto de formato o de valor (sin contar los nulos): 506 de 1545 (32,8 %); con los nulos: 705 (45,6 %).

## 3\. Antes y después

|  | Antes | Después |
| :---- | :---- | :---- |
| Filas | 1545 | 1500 |
| Duplicados | 45 | 0 |
| Valores distintos de `canal` | 9 | 4 |
| Valores distintos de `pais_origen` | 12 | 8 |
| Nulos en `noches` | 0 | 6 |
| Nulos en `precio_noche` | 84 | 87 |
| Nulos en `regimen` | 61 | 59 |
| Nulos en `pais_origen` | 115 | 112 |
| Nulos en `adultos` | 46 | 46 |

- **Resumen de `limpiar_reservas`:** 45 duplicados quitados, 14 valores imposibles pasados a nulo, 5 antelaciones recalculadas, 1545 → 1500 filas.  
- Los nulos cambian porque los duplicados que se quitan tenían huecos y porque los valores imposibles pasan a nulo. La única fila que desaparece es una repetida, y todas están contadas.

## 4\. Pipeline y modelo de referencia

- **Columnas numéricas (9):** `antelacion_dias`, `noches`, `adultos`, `ninos`, `precio_noche`, `peticiones_especiales`, `cliente_repetidor`, `cancelaciones_previas`, `mes_llegada`. **De texto (6):** `tipo_habitacion`, `regimen`, `canal`, `pais_origen`, `tarifa`, `deposito`. Fuera: `id_reserva` (es un identificador) y las fechas.  
- **Antes (reglas fijas, en `limpiar_reservas`):** duplicados, formatos, categorías, valores imposibles a nulo y antelación recalculada. No calcula nada a partir de los datos.  
- **Dentro del *pipeline* (solo con *train*):** mediana y escalado en los números; categoría más frecuente y *one-hot* en el texto. De 15 a 34 columnas.  
- **Partición:** 1200 filas de *train* y 300 de *test*, con la misma proporción de canceladas (0,47).  
- **Resultado (validación cruzada de 5 particiones, métrica AUC):** regresión logística **0,758 ± 0,025** frente a **0,500 ± 0,000** del modelo tonto. Eso significa que el modelo ordena las reservas por riesgo de cancelación mucho mejor que el azar. En *test*, mirado una sola vez: 0,752.

## 5\. Preguntas para el cliente

1. ¿Un precio de **0 €** significa «gratis» (cortesía) o «sin dato»? Mientras no respondan, lo tratamos como dato que falta.  
2. ¿Qué es el **9999**? ¿Un código de «sin precio» o una tarifa real? Lo tratamos como error.  
3. ¿Por qué hay precios con coma y fechas de dos formas? ¿Cuántos sistemas exportan y se puede unificar el formato en origen?  
4. ¿El país vacío es «no se sabe» o «no aplica» (reserva de empresa o agencia)? Mientras tanto, no usamos el país en el modelo.

## 6\. IA responsable

- **Problemas al completar los países que faltan:** hay 112 registros sin país de origen (un 7,5 % del total). Si se rellenan automáticamente con `ES`, al ser el país más frecuente, se estaría asignando incorrectamente a España reservas que realmente proceden de otros países.&nbsp;  
- **Posible discriminación por nacionalidad:** los datos muestran diferencias en las tasas de cancelación según el país. Por ejemplo, Italia presenta una tasa de 0,60 (77 reservas), mientras que Países Bajos tiene una de 0,37 (75 reservas). Esto podría provocar que el modelo favoreciese o perjudicase a determinados clientes en función de su procedencia, sin una justificación adecuada.&nbsp;  
- **Solución aplicada y comprobada:** se ha probado el modelo eliminando la variable `pais_origen`. El resultado es prácticamente idéntico: un AUC de 0,759 ± 0,026, frente al 0,758 ± 0,025 que se obtiene incluyéndola. Por tanto, el país no mejora el rendimiento del modelo y se **recomienda excluirlo.&nbsp;**  
- **Variables que conviene eliminar:** `id_reserva`, porque es un identificador sin valor predictivo real; `pais_origen`, porque puede introducir sesgos sin mejorar los resultados; y `cancelaciones_previas`, siempre que el cliente confirme que esta información no está disponible en el momento de realizar la predicción.&nbsp;  
- Los datos son sintéticos y no hay datos personales. Uso de la IA y qué se revisó: ver el README.

## 7\. Cómo reproducirlo

- Python 3.13, pandas 2.3.3, scikit-learn 1.9.1 (en Colab saldrán otras versiones; las cifras pueden variar en el último decimal).  
- Abrir `reto_S06.ipynb` en Colab y ejecutar de arriba abajo (*Reiniciar y ejecutar todo*). La primera celda descarga `reservas_sucio.csv` si no está.  
- Semilla fija: 42\. Ficheros: `reto_S06.ipynb`, `reservas_sucio.csv`.

## Extras (nivel 🔴)

- **\- División temporal:** al utilizar el 80 % de los datos más antiguos para entrenar el modelo y el 20 % más reciente para probarlo, se obtiene un AUC de 0,737, ligeramente inferior al obtenido mediante una división aleatoria (0,758). Sin embargo, este método ofrece una evaluación más realista, ya que simula mejor cómo funcionaría el modelo al analizar reservas futuras.  
- **\- Fuga de información:** cuando el escalado se realiza utilizando todos los datos, la media del precio que utiliza el modelo cambia de 102,68 (solo con los datos de entrenamiento) a 102,73. Aunque la diferencia es mínima, hacerlo implica que el conjunto de prueba deja de ser completamente independiente.  
- **\- Propuesta para el cliente:** se recomienda continuar con un modelo sencillo que no incluya la variable del país y solicitar que el sistema genere las fechas y los precios siempre en un mismo formato. Hay que tener en cuenta que un AUC cercano a 0,76 permite clasificar las reservas según su nivel de riesgo, pero no garantiza que se pueda tomar una decisión acertada sobre cada reserva individual.  
- &nbsp;

## Revisión con la rúbrica

**Revisado por:** todos · **Fecha:** 10/11/2026

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
| :---- | :---- | :---- |
| Corrección técnica | 4 | Se han identificado y corregido los principales problemas de los datos: precios imposibles, fechas con distintos formatos, duplicados, valores negativos y categorías escritas de diferentes maneras. Además, se han tratado los valores nulos y se ha creado un modelo con un AUC de 0,758.&nbsp; |
| Reproducibilidad | 4 | El proceso de limpieza está automatizado mediante una función y el modelo utiliza un pipeline que permite repetir los mismos pasos. También se ha fijado una semilla (42) y se han indicado las versiones de las librerías utilizadas.&nbsp; |
| Análisis y comunicación al cliente | 4 | Se han explicado los problemas encontrados, sus posibles causas y las soluciones aplicadas. También se han planteado preguntas para el cliente sobre los precios y los formatos de los datos, además de explicar las limitaciones del modelo.&nbsp; |
| IA responsable | 4 | Se ha evaluado el posible sesgo relacionado con el país de origen y se ha comprobado que eliminar esta variable no empeora el rendimiento. También se han identificado variables que podrían provocar problemas, como `id_reserva` y `cancelaciones_previas`.&nbsp; |

**Lo primero que mejoraríamos:** probar el cuaderno en un Colab nuevo y anotar las versiones que salgan allí.