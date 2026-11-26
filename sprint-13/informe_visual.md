# Informe visual · Regresión logística para TurisData Canarias

**Para:** Dirección · **Equipo:** pendiente de indicar · **Fecha:** 26/11/2026 · **Versión:** 1

---

## TITULAR: Pedir depósito y avisar a las reservas con riesgo alto podría ahorrar 16.590 € por cada 1.500 reservas.

## Los cuatro gráficos

| ¿Qué falla y cuánto? | ¿Podemos fiarnos del modelo? |
|---|---|
| **Detectamos el 83 % de las cancelaciones** — Gráfico 1: matriz de confusión | **El modelo distingue las cancelaciones mejor que el azar** — Gráfico 2: curva ROC |
| No detectamos el 17 % de las cancelaciones y avisamos por error al 49 % de quienes no cancelan. Una cancelación no detectada cuesta más por caso (50 € frente a 30 €). | El AUC de 0,744 indica una capacidad de discriminación razonable, aunque imperfecta. |
| **¿Qué mueve el resultado?** | **¿Cuánto vale?** |
| **La antelación de la reserva es la variable más importante** — Gráfico 3: importancia de variables | **El coste estimado se reduce un 48,2 %** — Gráfico 4: ahorro en euros |
| Los días entre reserva y llegada aportan más información predictiva que el depósito o el canal; esto no demuestra causalidad. | Sin modelo: 34.400 €; con modelo: 17.810 €; ahorro: 16.590 €. Supuestos: FN = 50 €, FP = 30 €. |

![Panel generado por el notebook](informe_visual_panel.png)

## Tres viñetas
- **Qué hemos hecho:** Hemos utilizado 6.000 reservas sintéticas para construir un modelo que estima la probabilidad de cancelación. Se ha entrenado con 4.500 reservas y evaluado con otras 1.500.
- **Qué recomendamos:** Iniciar una prueba piloto de avisos y solicitud de depósito para reservas con una probabilidad estimada de cancelación igual o superior al 35 %. El ahorro simulado es de 16.590 € por cada 1.500 reservas, sujeto a validar los costes y la eficacia de las medidas.
- **Qué límites tiene:** Los datos son sintéticos y su periodo no consta en los resultados disponibles. El modelo genera falsas alarmas en el 49 % de las reservas que no cancelan; el 41 % de los avisos son erróneos. No debe utilizarse para rechazar reservas. Proponemos validarlo con datos reales antes de implantarlo y revisarlo trimestralmente.

## IA responsable (2 líneas)
El modelo podría perjudicar a clientes que no iban a cancelar. Se utilizará para priorizar avisos, con revisión humana antes de solicitar depósitos y control trimestral de errores por grupos de clientes.
Se ha pedido a la IA redactar el informe a partir del notebook; se han contrastado las cifras con las salidas guardadas y el panel original.

## Pie
Datos: reservas_turisdata.csv, sintéticos (n = 6.000; periodo no verificado) · Modelo: regresión logística · Umbral: 0,35 · Semilla: 42 · Notebook: `IA_informe_visual.ipynb` · Responsable: pendiente de indicar.

---

### Lista de comprobación antes de entregar
- [x] ¿Entiende la decisión una persona no técnica en 30 segundos? (Redacción orientada a dirección; pendiente de validación externa.)
- [x] ¿Cada título dice algo que se pueda discutir? (En el informe; conviene actualizar el título del gráfico 3 en el notebook.)
- [x] ¿Barras desde 0, ejes con nombre y unidades, colores con sentido?
- [x] ¿Métricas del test, no del entrenamiento?
- [x] ¿Las cifras del texto coinciden con las del gráfico?
- [x] ¿Figura al menos un límite y un riesgo?
- [ ] ¿Cabe en una página y se lee proyectada? Pendiente de comprobar en el formato final.

### Reglas de oro de comunicación de datos
1. Un gráfico, un mensaje. 2. El título es la conclusión. 3. Ejes honestos. 4. Color con sentido. 5. Nada de 3D ni tartas de más de 3 trozos. 6. Etiqueta directa de los valores. 7. Di lo que no sabes.

---

## Revisión con la rúbrica
*Propuesta de revisión preliminar basada en las salidas guardadas. Debe validarla una persona que no haya redactado el informe.*

**Revisado por:** pendiente · **Fecha:** pendiente

| Criterio | Nivel (1–4) | Prueba |
|---|---|---|
| Corrección técnica | 3 (provisional) | Los cuatro gráficos utilizan el conjunto de prueba y las barras parten de cero. El título del gráfico 3 puede concretarse. |
| Reproducibilidad | Pendiente | El código fija la semilla 42, pero no se ha reiniciado y ejecutado el cuaderno completo. |
| Análisis y comunicación al cliente | 3 (provisional) | La decisión incluye umbral, ahorro y costes coherentes con las salidas del notebook. |
| IA responsable | 3 (provisional) | Se identifica el riesgo de falsas alarmas, se propone supervisión humana y se declara el uso de IA. |

**Lo primero que mejoraríamos:** Validar el ahorro y ajustar el umbral con datos reales, antes de aplicar depósitos a clientes.
