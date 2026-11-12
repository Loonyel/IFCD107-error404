# Informe de modelado · TurisData Canarias · «Precio y cancelación»

**Equipo:** ERROR 404 · **Fecha:** 11/11/2026

## 1\. Resumen para el gerente (máx. 6 líneas)

Hemos preparado un modelo para estimar el precio por noche y otro para avisar de posibles cancelaciones.  
El modelo de precio con interacciones se equivoca de media 6,76 € por noche.  
Suponemos un coste de 284 € por cancelación no prevista y de 103 € por falsa alarma.  
Recomendamos revisar las reservas cuya probabilidad de cancelación sea igual o superior al 25 %.  
Con estas hipótesis, el coste en la muestra de prueba baja de 156.484 € a 58.331 €: una reducción estimada de 98.153 € (63 %).  
Es una simulación con datos sintéticos; las decisiones sobre clientes deben tener revisión humana.

## 2\. Datos y variables

Usamos 6.000 reservas. El archivo tiene 18 columnas y añadimos dos: el mes de llegada y si corresponde a temporada alta (enero, febrero, marzo, julio, agosto y diciembre).

**Para el precio**, usamos el tipo de habitación y la temporada. Excluimos `cancelada`, porque no se conoce al reservar, e `id_reserva`, porque solo identifica la reserva. Resumimos la época del año en la temporada y dejamos fuera las demás variables para mantener el modelo sencillo.

**Para la cancelación**, usamos antelación, noches, adultos, niños, precio por noche, peticiones especiales, cliente repetidor, cancelaciones previas, temporada, tipo de habitación, régimen, canal, país de origen, tarifa y depósito. Son características disponibles al reservar. Excluimos el identificador y las fechas originales. `cancelada` es lo que queremos predecir y no se introduce como dato de entrada.

Separamos aleatoriamente 4.800 reservas para entrenar y 1.200 para evaluar, con semilla 42\. Cada problema tiene su propia partición. En cancelación mantenemos aproximadamente un 45,9 % de canceladas en ambos grupos. Los datos ausentes se rellenan y las variables se preparan dentro del entrenamiento, también durante la validación cruzada.

## 3\. Regresión: precio por noche

| Modelo | MAE (€) | RMSE (€) | R² |
| :---- | :---- | :---- | :---- |
| Baseline (media) | 25,564 | 33,328 | −0,002 |
| Lineal | 7,239 | 9,704 | 0,915 |
| Lineal con interacciones | 6,758 | 8,936 | 0,928 |

El MAE indica cuánto nos equivocamos de media en euros. El RMSE da más peso a los errores grandes y R² resume cuánto explica el modelo de las diferencias de precio.

Elegimos el modelo con interacciones porque presenta el menor error: **6,76 € por noche**, frente a 25,56 € de predecir siempre la media. La mejora frente al lineal es pequeña, unos 0,48 €. Las interacciones permiten que la temporada tenga un efecto diferente según la habitación.

En el modelo lineal, una estándar en temporada baja parte de **67,30 €**. Los suplementos estimados son familiar \+45,00 €, suite \+101,20 €, superior \+28,40 € y temporada alta \+22,40 €. Estos suplementos corresponden al modelo lineal y son asociaciones, no efectos causales.

Los residuos son las diferencias entre los precios reales y los estimados. El RMSE superior al MAE muestra que hay errores mayores que el promedio, pero no hemos analizado los residuos por grupos; por eso no afirmamos en qué tipo de reserva falla más.

## 4\. Clasificación: cancelación

| Modelo | AUC | AP | Recall (umbral) | Precisión (umbral) |
| :---- | :---- | :---- | :---- | :---- |
| Baseline | 0,500 | 0,459 | 0 % (sin avisos) | No definida: sin avisos |
| Logística | 0,746 | 0,729 | 92,0 % (0,25) | 53,3 % (0,25) |

La referencia siempre predice que la reserva se mantiene. La logística distingue mejor entre reservas con mayor y menor riesgo, como indican sus valores superiores de AUC y AP.

**Matriz de confusión en test con umbral 0,25:**

| Resultado real | Predice que se mantiene | Predice que cancela |
| :---- | ----: | ----: |
| Se mantiene | 204 (aciertos) | 445 (falsas alarmas) |
| Cancela | 44 (no detectadas) | 507 (detectadas) |

Detectamos aproximadamente el **92 % de las cancelaciones**, pero solo el **53 % de los avisos** corresponde a cancelaciones reales. El modelo avisa mucho porque hemos supuesto que dejar escapar una cancelación cuesta más que una falsa alarma.

Los *odds ratios* permiten estudiar qué factores se asocian con mayor o menor riesgo. No los hemos calculado en este ejercicio, por lo que no atribuimos el riesgo a características concretas basándonos en estos resultados.

## 5\. De las métricas a los euros

- **Hipótesis de coste** de una cancelación no prevista (FN): **284 € por reserva**. Suponemos que solo se revende la mitad de una estancia media: 0,5 × 5,52 noches × 102,87 € ≈ 284 €.  
- **Hipótesis de coste** de una falsa alarma (FP): **103 € por reserva**. Suponemos una compensación equivalente al precio medio de una noche si la falsa alarma acaba provocando una reubicación. Es una simplificación: no toda falsa alarma causará ese gasto.  
- Umbral elegido con validación cruzada: **0,25**, el de menor coste entre los umbrales probados, usando cinco particiones de entrenamiento y sin elegirlo con test.  
- Coste en test: sin modelo **156.484 €** · umbral 0,5 **78.439 €** · umbral elegido **58.331 €**.  
- **Análisis de sensibilidad:** comprobamos qué ocurre al cambiar las hipótesis.

| Hipótesis | Coste FN (€) | Coste FP (€) | Umbral elegido | Coste total (€) | Sin modelo (€) |
| :---- | ----: | ----: | ----: | ----: | ----: |
| Inicial | 284 | 103 | 0,25 | 223.121 | 625.652 |
| FN el doble | 568 | 103 | 0,15 | 249.011 | 1.251.304 |
| FP la mitad | 284 | 51,50 | 0,15 | 124.506 | 625.652 |
| FP el doble | 284 | 206 | 0,40 | 354.720 | 625.652 |

Si no detectar una cancelación cuesta más, conviene avisar más y el umbral baja. Si una falsa alarma cuesta más, conviene avisar menos y el umbral sube. Estos costes son de las 4.800 reservas de entrenamiento con validación cruzada; no se comparan directamente con los totales de las 1.200 de test.

## 6\. Recomendación de negocio

Recomendamos usar el umbral **0,25** para priorizar la revisión de reservas y preparar alternativas de ocupación. El aviso no debe cancelar reservas ni autorizar automáticamente una sobreventa. Para el precio, proponemos el modelo con interacciones como tarifa orientativa, revisada por el gerente.

En las reservas de prueba, la reducción simulada de coste es **98.153 € (62,7 %)** frente a no avisar. No es un ahorro real demostrado: depende de nuestros costes y no hemos simulado la disponibilidad ni las reubicaciones reales.

Los datos son sintéticos y de un solo hotel; la evaluación es aleatoria, no sobre un periodo futuro. Antes de aplicarlo necesitamos costes reales de noches no revendidas y compensaciones. Si cambia el comportamiento de los clientes, habrá que revisar el modelo y el umbral.

## 7\. IA responsable

Entre las reservas que se mantienen, las falsas alarmas son aproximadamente el **65 % en agencia, 49 % en directo, 74 % en empresa y 85 % en web intermediaria**. Hay diferencias por canal que debemos vigilar; por sí solas no demuestran discriminación y habría que comprobar también el número de reservas de cada grupo.

Los clientes que no cancelan pueden verse perjudicados si una falsa alarma provoca su reubicación. Usar país o canal para exigir depósitos o modificar precios también puede generar un trato desigual. Proponemos revisión humana, seguimiento de errores por canal y país y evitar penalizaciones automáticas. Hemos comprobado las diferencias por canal; las medidas de uso son recomendaciones.

Hemos pedido ayuda a la IA para entender el ejercicio, revisar el código y redactar el informe. Hemos contrastado las cifras con las salidas de Colab y ejecutado el cuaderno completo sin errores. Hemos reducido los textos añadidos para ceñirnos al ejercicio. Los costes están justificados y el umbral procede del cálculo, no de una cifra propuesta por la IA.

## 8\. Cómo reproducirlo

Usamos **Python 3.13.18**, **scikit-learn 1.6.1** y **SEMILLA \= 42**.

Abrir `reto_S07.ipynb` en Colab y ejecutar de arriba abajo. La primera celda carga `reservas_turisdata.csv` y lo descarga del repositorio del curso si no está disponible localmente. Se necesita conexión para esa descarga.

El orden es: carga de datos, costes, modelos de precio, clasificación y elección del umbral, evaluación en test, sensibilidad, revisión por canal y versiones. Hemos reiniciado y ejecutado todo sin errores, según la comprobación comunicada por el equipo.

## Revisión con la rúbrica

**Revisado por:** Equipo ERROR 404 (revisión grupal) · **Fecha:** 11/11/2026

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
| :---- | :---- | :---- |
| Corrección técnica | 3 | Hemos revisado las referencias, la mejora del precio, las métricas y la matriz; el umbral se elige con validación cruzada de entrenamiento antes de evaluar test. |
| Reproducibilidad | 3 | Hemos reiniciado y ejecutado el cuaderno sin errores y registrado semilla. |
| Análisis y comunicación al cliente | 3 | Hemos explicado el error del precio en euros, el umbral, los costes, la sensibilidad y los límites de la recomendación. |
| IA responsable | 3 | Hemos explicado la ayuda de la IA y lo comprobado, identificado riesgos para los clientes y medido diferencias de falsas alarmas por canal. |

**Lo primero que mejoraríamos:** confirmar con el hotel los costes reales para ajustar el umbral.

**Como mejora del análisis**, estudiar los errores del precio por grupos y calcular los odds ratios para explicar los factores de cancelación.