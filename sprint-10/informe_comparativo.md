# Informe comparativo · ¿Vale la pena la red? (Sprint 10\)

## 1\. Pregunta y respuesta

Recomendamos **mantener el boosting de árboles**, porque obtiene un rendimiento muy parecido al MLP (AUC de 0,738 frente a 0,743) y se entrena aproximadamente **23 veces más rápido**.

## 2\. Resultados

| Modelo | AUC | AP | F1 | Exactitud |
| :---- | :---- | :---- | :---- | :---- |
| Boosting de árboles | 0,738 | 0,721 | 0,639 | 0,672 |
| MLP (media de 3 semillas) | 0,743 | 0,722 | 0,637 | 0,682 |

AUC de validación del MLP: **0,744 ± 0,002**. Diferencia de AUC (MLP − boosting): **\+0,005**, intervalo del 95 %: **\[-0,005; \+0,018\]**. La diferencia **no es mayor que el ruido**, porque el intervalo incluye el cero.

## 3\. Curva comentada

Las curvas de entrenamiento y validación se mantienen relativamente próximas. Las mejores épocas de las tres ejecuciones fueron la 30, 29 y 31\. La pérdida media de entrenamiento fue de 0,591 y la de validación de 0,618. **Diagnóstico:** no se observa un sobreajuste claro; la regularización L2, el dropout del 30 % y la parada temprana ayudan a controlarlo.

## 4\. Coste

**Tiempo de entrenamiento:** boosting 0,58 s; MLP 13,54 s (aproximadamente 23 veces más lento). **Complejidad:** boosting con 200 iteraciones; MLP con 4.417 parámetros. **Explicabilidad:** el boosting es más sencillo de interpretar y mantener que la red neuronal.

## 5\. Riesgos de IA responsable

1. **Riesgo:** predicciones desiguales entre grupos de clientes, por ejemplo según el país de origen o el canal de reserva. **Medida:** revisar los errores y las métricas por grupos y comprobar posibles sesgos antes de aplicar decisiones automáticas.  
2. **Riesgo:** que el comportamiento de las reservas cambie con el tiempo y el modelo pierda precisión. **Medida:** supervisar periódicamente su rendimiento con datos recientes y actualizarlo cuando sea necesario.

## 6\. Límites y siguiente paso

Los resultados proceden de datos sintéticos y no sabemos si se mantendrán con reservas reales. Además, se ha utilizado un umbral de decisión de 0,5 sin estudiar todavía el coste de los falsos positivos y falsos negativos. El siguiente paso sería **probar el boosting con datos reales**, ajustar el umbral según los costes para el hotel y comprobar su rendimiento y equidad a lo largo del tiempo.

## Uso de la IA

Pedimos a la IA que redactara una recomendación comparativa a partir de los resultados del ejercicio y que la adaptara a esta plantilla.

## Revisión con la rúbrica

Revisado por: **pendiente de completar** · Fecha: **18/11/2026**

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
| :---- | :---- | :---- |
| Corrección técnica | 4 | Contrastar las métricas, la diferencia de AUC y el intervalo de confianza con el cuaderno. |
| Reproducibilidad | 4 | Verificar las tres semillas, las mejores épocas y los tiempos de entrenamiento al ejecutar el cuaderno. |
| Análisis y comunicación al cliente | 4 | Revisar que la recomendación esté respaldada por rendimiento, coste y explicabilidad. |
| IA responsable | 3 | Revisar que los riesgos identificados tengan medidas de mitigación concretas. |

**Lo primero que mejoraríamos:** validar los resultados con reservas reales y ajustar el umbral de decisión según el coste de los errores.