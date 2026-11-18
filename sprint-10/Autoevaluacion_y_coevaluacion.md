# Autoevaluación y coevaluación · «¿Vale la pena la red?»

---

## 1\. Autoevaluación (cada persona, unos 5 minutos)

**Nombre:** Eli

**Repaso rápido** (las mismas preguntas de «Antes de entregar» del reto en una página; contesta Sí / No / A medias):

| Pregunta | Mi respuesta |
| :---- | :---- |
| ¿El cuaderno se ejecuta de arriba abajo, con semillas fijas? | Sí |
| ¿La partición es única y la prueba se usa una sola vez? | Sí |
| ¿Hay al menos un MLP y un modelo de árboles/boosting comparados con las mismas métricas? | Sí |
| ¿Hay curvas de aprendizaje y un diagnóstico explícito de sobreajuste? | Sí |
| ¿La comparación tiene incertidumbre (varias semillas o bootstrap)? | Sí |
| ¿El informe recomienda algo concreto, con coste y límites? | Sí |
| ¿Hay al menos dos riesgos de IA responsable específicos? | Sí |

**Puntúate de 1 a 4** en cada criterio de la rúbrica:

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
| :---- | :---- | :---- | :---- |
| Corrección técnica | 4 | He comparado los dos modelos con las mismas métricas y he analizado si la diferencia es significativa.&nbsp; | Nada |
| Reproducibilidad | 4 | He utilizado semillas fijas, la misma partición de datos y tres entrenamientos del MLP.&nbsp; | Nada |
| Análisis y comunicación al cliente | 4 | He recomendado mantener el boosting explicando sus resultados, costes y limitaciones.&nbsp; | Nada |
| IA responsable | 3 | He identificado riesgos relacionados con los sesgos y los errores de predicción, pero no los he comprobado con datos reales. | Analizaría los resultados por país y canal de reserva para detectar posibles diferencias injustas.&nbsp; |

- **Lo que más me costó fue** interpretar las curvas de aprendizaje y entender si había sobreajuste, **porque** tenía que comparar las pérdidas de entrenamiento y validación. También me costó comprender el intervalo de confianza y saber si la diferencia entre los modelos era realmente importante.&nbsp;  
- **He usado IA para** ayudarme a interpretar los resultados, **y lo que he comprobado a mano es** que las cifras utilizadas aparecen en los resultados del cuaderno, como el AUC, el F1, los tiempos de entrenamiento y el intervalo de confianza. También he revisado que la recomendación tenga sentido según los resultados obtenidos.&nbsp;

&nbsp;

**Nombre:** Fran

**Repaso rápido** (las mismas preguntas de «Antes de entregar» del reto en una página; contesta Sí / No / A medias):

| Pregunta | Mi respuesta |
| :---- | :---- |
| ¿El cuaderno se ejecuta de arriba abajo, con semillas fijas? | SI |
| ¿La partición es única y la prueba se usa una sola vez? | SI |
| ¿Hay al menos un MLP y un modelo de árboles/boosting comparados con las mismas métricas? | SI |
| ¿Hay curvas de aprendizaje y un diagnóstico explícito de sobreajuste? | SI |
| ¿La comparación tiene incertidumbre (varias semillas o bootstrap)? | SI |
| ¿El informe recomienda algo concreto, con coste y límites? | SI |
| ¿Hay al menos dos riesgos de IA responsable específicos? | SI |

**Puntúate de 1 a 4** en cada criterio de la rúbrica:

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
| :---- | :---- | :---- | :---- |
| Corrección técnica | 3 | Hemos completado y revisado los ejercicios, comparando el MLP y el boosting con las mismas métricas.&nbsp; | Repetiría más pruebas para comprobar la estabilidad de los resultados.&nbsp; |
| Reproducibilidad | 4 | El cuaderno utiliza semillas fijas, incluye resultados y se ha compartido con el README en GitHub&nbsp; | NADA |
| Análisis y comunicación al cliente | 3 | Hemos preparado un informe con resultados, costes y una recomendación razonada para TurisData.&nbsp; | Añadiría una valoración más detallada del coste de los errores para el negocio.&nbsp; |
| IA responsable | 3 | Hemos considerado las limitaciones de los datos sintéticos y los posibles sesgos entre grupos de reservas.&nbsp; | Comprobaría estos riesgos con datos reales y un análisis por segmentos.&nbsp; |

&nbsp;

- **Lo que más me costó fue** interpretar las métricas y la incertidumbre de la comparación, **porque** todavía estoy aprendiendo a relacionar los resultados técnicos con las decisiones del negocio.  
- **He usado IA para** comprender el código, interpretar los resultados y revisar los textos del informe y del README, **y lo que he comprobado a mano es** que las cifras y conclusiones coincidan con las salidas del Colab.

&nbsp;

**Nombre:** EVA

**Repaso rápido** (las mismas preguntas de «Antes de entregar» del reto en una página; contesta Sí / No / A medias):

| Pregunta | Mi respuesta |
| :---- | :---- |
| ¿El cuaderno se ejecuta de arriba abajo, con semillas fijas? | SI |
| ¿La partición es única y la prueba se usa una sola vez? | SI |
| ¿Hay al menos un MLP y un modelo de árboles/boosting comparados con las mismas métricas? | SI |
| ¿Hay curvas de aprendizaje y un diagnóstico explícito de sobreajuste? | SI |
| ¿La comparación tiene incertidumbre (varias semillas o bootstrap)? | SI |
| ¿El informe recomienda algo concreto, con coste y límites? | SI |
| ¿Hay al menos dos riesgos de IA responsable específicos? | SI |

**Puntúate de 1 a 4** en cada criterio de la rúbrica:

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
| :---- | :---- | :---- | :---- |
| Corrección técnica | 4 | Hemos realizado las pruebas y comparado los modelos utilizando los mismos criterios de evaluación.&nbsp; | Probaría diferentes configuraciones para mejorar y comprobar los resultados.&nbsp; |
| Reproducibilidad | 4 | &nbsp;El proyecto está organizado y documentado, con semillas fijas y el código disponible en GitHub. | Mantendría el mismo procedimiento para futuros proyectos.&nbsp; |
| Análisis y comunicación al cliente | 3 | Hemos explicado los resultados y propuesto una solución teniendo en cuenta las necesidades de TurisData&nbsp; | Explicaría con más ejemplos cómo afectan los resultados a las decisiones de la empresa.&nbsp; |
| IA responsable | 3 | Hemos identificado posibles sesgos y limitaciones que podrían afectar a las predicciones del modelo.&nbsp; | Realizaría más comprobaciones para detectar diferencias entre distintos grupos de usuarios.&nbsp; |

&nbsp;

\-**Lo que más complicado me ha resultado** ha sido entender e interpretar correctamente las métricas de los modelos y saber cuál ofrece mejores resultados. También me ha costado relacionar los datos obtenidos con situaciones reales de una empresa.

\-**He utilizado la IA** como apoyo para entender algunas partes del código, resolver dudas y mejorar la redacción del informe.**y lo que he comprobado a mano es** los resultados del Colab para asegurarme de que los datos y las conclusiones fueran correctos.

&nbsp;

&nbsp;

&nbsp;

**Nombre:** JUKEIZA

**Repaso rápido** (las mismas preguntas de «Antes de entregar» del reto en una página; contesta Sí / No / A medias):

| Pregunta | Mi respuesta |
| :---- | :---- |
| ¿El cuaderno se ejecuta de arriba abajo, con semillas fijas? | SI |
| ¿La partición es única y la prueba se usa una sola vez? | SI |
| ¿Hay al menos un MLP y un modelo de árboles/boosting comparados con las mismas métricas? | SI |
| ¿Hay curvas de aprendizaje y un diagnóstico explícito de sobreajuste? | SI |
| ¿La comparación tiene incertidumbre (varias semillas o bootstrap)? | SI |
| ¿El informe recomienda algo concreto, con coste y límites? | SI |
| ¿Hay al menos dos riesgos de IA responsable específicos? | SI |

**Puntúate de 1 a 4** en cada criterio de la rúbrica:

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
| :---- | :---- | :---- | :---- |
| Corrección técnica | 4 | Todos los números, métricas y el análisis estadístico coinciden con los resultados del código.&nbsp; | Nada |
| Reproducibilidad | 4 | Se indican los tiempos exactos, las épocas y se usan tres semillas distintas para asegurar el resultado.&nbsp; | Nada |
| Análisis y comunicación al cliente | 4 | La recomendación final es muy clara y se apoya en datos reales de precisión, velocidad y facilidad de uso | Nada |
| IA responsable | 3 | Se mencionan dos riesgos claros (discriminación y pérdida de precisión con el tiempo) y cómo evitarlos. | Pondría reglas exactas, como revisar el modelo cada mes o fijar un límite de error por país.&nbsp; |

**Lo que más me costó fue** entender partes del código y decidir cuál de los dos modelos era mejor para el trabajo, **porque** los resultados eran casi iguales y me costó estar seguro de si esa mínima diferencia valía la pena o era solo suerte.&nbsp;

**He usado IA para** ayudarme a redactar los textos y ordenarlos dentro de la plantilla, **y lo que he comprobado a mano es** que todos los números y tiempos que puse en el informe fueran los mismos que me salieron al hacer las pruebas en el ordenador.&nbsp;

---

## 2\. Coevaluación (durante la review, unos 10 minutos)

**Trabajo revisado de (persona o equipo):** ……  **Revisado por (yo):** ……

**¿Está lo que pide el reto?** Marca ✔ (sí), ✘ (no) o — (no procede).

| Entregable (nómbralo) | ¿Está y se entiende? | Comentario breve |
| :---- | :---- | :---- |
| Cuaderno de Google Colab | ✔ | Se explica la comparación entre el MLP y el boosting, utilizando las mismas métricas y semillas fijas. |
| Informe para TurisData | ✔ | Presenta los resultados, los costes y una recomendación razonada sobre el modelo que conviene utilizar. |
| README y repositorio de GitHub | ✔ | La documentación ayuda a entender el proyecto y a repetir las pruebas. |

&nbsp;

**Puntuación (1–4) de quien revisa:**

| Criterio | Puntuación | Comentario breve |
| :---- | :---- | :---- |
| Corrección técnica | 4 | Se comparan los modelos con las mismas métricas y se analiza la incertidumbre de los resultados. |
| Reproducibilidad | 4 | Se utilizan semillas fijas y el trabajo está documentado para poder repetirlo. |
| Análisis y comunicación al cliente | 4 | La recomendación está justificada y tiene en cuenta el rendimiento, los costes y las limitaciones. |
| IA responsable | 3 | Se identifican riesgos de sesgos y de pérdida de precisión, aunque faltaría comprobarlos con datos reales. |

- **Lo que está muy bien:** Me ha ayudado que la comparación entre los dos modelos sea clara y que la recomendación final no se base solo en las métricas, sino también en el coste y la utilidad para TurisData.&nbsp;  
- **Lo que yo cambiaría, y por qué:** Añadiría un análisis de los errores por país y canal de reserva, porque permitiría comprobar si el modelo funciona de forma parecida para distintos grupos y detectar posibles sesgos.&nbsp;

> Se valora el **trabajo**, no a la persona. Frases que ayudan: «Me ha ayudado que …», «Yo cambiaría … porque …».