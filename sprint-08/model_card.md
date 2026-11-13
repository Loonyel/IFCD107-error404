# Model card · Predicción de cancelaciones de reservas · TurisData Canarias

**Equipo:** Error404 · **Fecha:** 13/11/2026 · **Versión del modelo:** 1.0 · **Contacto:** No especificado

> Documento para el cliente y para quien mantenga el modelo. Los datos no disponibles en las fuentes se indican como pendientes o no especificados.

## 1\. Resumen

El modelo predice la probabilidad de que una reserva hotelera sea cancelada. Su objetivo es ayudar a TurisData Canarias a anticiparse a las cancelaciones y mejorar la planificación de habitaciones y recursos. Está dirigido a los gerentes y responsables de reservas, que podrán utilizar las predicciones como apoyo a la toma de decisiones. El modelo no sustituye la revisión humana.

## 2\. Modelo campeón

- **Familia y algoritmo:** Árbol de decisión podado (`DecisionTreeClassifier`).  
- **Nombre del modelo:** `arbol_podado`.  
- **Hiperparámetros finales:**  
  - `min_samples_leaf = 80`  
  - `random_state = 42`  
- **Preprocesado:**  
  - Variables numéricas: imputación mediante la mediana.  
  - Variables categóricas: imputación mediante la categoría más frecuente y codificación One-Hot.  
  - No se aplica escalado al árbol de decisión.  
  - Todo el preprocesado está integrado en un pipeline.  
- **Librerías y versiones:**  
  - Scikit-learn: 1.6.1  
  - XGBoost: 3.4.1  
  - LightGBM: 4.6.0  
  - NumPy, Pandas y SciPy: versiones no especificadas.

## 3\. Por qué este campeón (y no otro)

Se eligió el árbol podado utilizando tres criterios: rendimiento, explicabilidad y coste.

| Criterio | Peso acordado | Resultado del campeón | Mejor rival y diferencia |
| :---- | ----: | :---- | :---- |
| Rendimiento (AUC validación cruzada) | 50 % | 0.7194 ± 0.0095 | Logística: 0.7546 (0.0352 más) |
| Explicabilidad (1–5) | 30 % | 5/5 | Logística: 4/5 |
| Coste (ajuste, predicción y tamaño) | 20 % | 0.035 s; 8.7 ms/1000; 11 KB | Logística: 0.384 s; 30.5 ms/1000; 4.2 KB |

La puntuación global del árbol podado fue **0.931**, frente a **0.912** de la regresión logística.

Aunque la regresión logística obtuvo el AUC más alto, el árbol podado ofrece una mayor explicabilidad y menor coste de ajuste y predicción.

### Análisis de sensibilidad

| Pesos (rendimiento / explicabilidad / coste) | Campeón |
| :---- | :---- |
| 0.5 / 0.3 / 0.2 (los nuestros) | `arbol_podado` |
| 0.8 / 0.1 / 0.1 (solo rendimiento) | `logistica` |
| 0.4 / 0.4 / 0.2 (equilibrado) | `arbol_podado` |
| 0.2 / 0.6 / 0.2 (explicabilidad primero) | `arbol_podado` |

El campeón cambia cuando se da mucha más importancia al rendimiento. Si el cliente prioriza exclusivamente el AUC, la regresión logística sería la alternativa recomendada.

## 4\. Datos de entrenamiento

- **Fuente:** Dataset de reservas `reservas_turisdata.csv`.  
- **Número total de reservas:** 6.000.  
- **Datos de entrenamiento:** 4.800 reservas (80 %).  
- **Datos de test:** 1.200 reservas (20 %).  
- **Partición:** estratificada, con semilla 7\.  
- **Validación cruzada:** 5 particiones estratificadas, con semilla 42\.  
- **Variable objetivo:** `cancelada`.

**Variables utilizadas:**

- Numéricas: antelación de la reserva, noches, adultos, niños, precio por noche, peticiones especiales, cliente repetidor, cancelaciones previas y temporada alta.  
- Categóricas: tipo de habitación, régimen, canal, país de origen, tarifa y depósito.

La temporada alta se define utilizando los meses de enero, febrero, marzo, julio, agosto y diciembre.

**Variables excluidas:** No se dispone de una relación documentada de las variables excluidas por motivos de fuga de información, sensibilidad o disponibilidad temporal.

**Limitaciones:** No se ha documentado el periodo temporal del dataset ni su representatividad respecto al conjunto real de reservas hoteleras. Es necesario comprobar su calidad y representatividad antes de utilizar el modelo en producción.

## 5\. Rendimiento

**Validación cruzada (train):**

* AUC: 0.7194.  
* Desviación estándar del AUC: 0.0095.  
* Average Precision (AP): 0.6668.

**Test (una sola evaluación):**

* AUC: 0.7166.

**Umbral de decisión: 0,25 (25 %).**

Se establece un umbral del 0,25 para clasificar las reservas:

* Si la probabilidad predicha de cancelación es igual o superior a 0,25, la reserva se clasifica como de riesgo de cancelación.  
* Si la probabilidad es inferior a 0,25, se clasifica como de bajo riesgo de cancelación.

Se elige este umbral para aumentar la capacidad de detectar posibles cancelaciones y facilitar que el personal del hotel pueda anticiparse y tomar medidas preventivas. Esto puede aumentar también las falsas alarmas, por lo que las predicciones deben revisarse por una persona.

**Recall y precisión:** Deben calcularse utilizando el umbral de 0,25 sobre los datos de test. No se dispone todavía de esos valores.

**Rendimiento por subgrupos:** No se dispone de resultados desglosados por canal, país o tipo de tarifa. Se recomienda realizar esta evaluación antes de implantar el modelo.

## 6\. Uso previsto y usos NO previstos

**Uso previsto:**

- Estimar el riesgo de cancelación de las reservas.  
- Ayudar a los gerentes a anticipar posibles cancelaciones.  
- Mejorar la planificación de habitaciones y recursos.  
- Facilitar la toma de decisiones mediante información predictiva.

**NO usar para:**

- Denegar automáticamente reservas.  
- Cobrar precios diferentes según el país de origen.  
- Discriminar a clientes por nacionalidad o canal.  
- Tomar decisiones automáticas sin supervisión humana.  
- Considerar una predicción como una cancelación segura.

## 7\. Explicabilidad

El modelo campeón es un árbol de decisión podado, con una puntuación de explicabilidad de 5 sobre 5\.

Sus decisiones pueden explicarse mediante reglas y condiciones sobre las variables de entrada. Esto permite que un gerente pueda comprender por qué una reserva ha sido clasificada con mayor o menor riesgo de cancelación.

Las variables disponibles incluyen la antelación, las cancelaciones previas, el precio por noche, el tipo de tarifa, el canal y las peticiones especiales.

Para explicar predicciones concretas se recomienda mostrar el camino recorrido por el árbol y las condiciones que han influido en la clasificación.

## 8\. Riesgos e IA responsable

**Posibles sesgos:**

- Diferencias relacionadas con el país de origen.  
- Diferencias entre canales de reserva.  
- Diferencias entre tipos de tarifa.  
- Posible falta de representatividad de determinados grupos de clientes.

**Impacto de los errores:**

- Falsos positivos: reservas que se consideran de riesgo y finalmente no se cancelan. Podrían provocar decisiones innecesarias sobre habitaciones o clientes.  
- Falsos negativos: reservas que se consideran seguras y finalmente se cancelan. Podrían provocar pérdidas de ingresos y problemas de planificación.

**Medidas recomendadas:**

- Mantener supervisión humana.  
- Revisar periódicamente los errores.  
- Analizar el rendimiento por subgrupos.  
- Evitar decisiones discriminatorias.  
- No utilizar las predicciones como única base para tomar decisiones.

No se dispone de una evaluación documentada de sesgos ni de medidas correctoras ya evaluadas.

## 9\. Mantenimiento

Se recomienda vigilar:

- La evolución del AUC.  
- La tasa real de cancelaciones frente a la prevista.  
- Los cambios en las características de las reservas.  
- La posible deriva de datos.  
- Las diferencias de rendimiento entre canales y países.

**Reentrenamiento:** Se recomienda revisar el modelo periódicamente y reentrenarlo cuando se detecte una pérdida significativa de rendimiento o cambios importantes en los datos.

**Coste de mantenimiento:** No especificado.

**Responsable:** Equipo técnico de TurisData Canarias (responsable concreto pendiente de asignar).

## 10\. Cómo reproducirlo

Para reproducir los resultados:

- Utilizar la semilla `SEMILLA = 42`.  
- Utilizar la semilla `SEMILLA_TEST = 7`.  
- Ejecutar las celdas del notebook en orden.  
- Mantener la misma partición de entrenamiento y test.  
- Utilizar validación cruzada estratificada de 5 particiones.  
- Ejecutar el preprocesado y entrenamiento mediante los pipelines definidos.  
- Utilizar el archivo `reservas_turisdata.csv`.  
- Consultar el leaderboard `leaderboard_S08.csv`.  
- Utilizar el notebook `S08_06_leaderboard_plantilla.ipynb`.

**Resultado final:** El modelo seleccionado es `arbol_podado`, con un AUC de validación cruzada de 0.7194 ± 0.0095 y un AUC de test de 0.7166.

La elección se justifica por el equilibrio entre rendimiento, explicabilidad y coste computacional, priorizando que los resultados puedan ser comprendidos y utilizados por los responsables de reservas.