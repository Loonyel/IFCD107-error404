# Autoevaluación y coevaluación · «Datos sucios, cliente impaciente»

---

## 1\. Autoevaluación (cada persona, unos 5 minutos)

**Nombre:** ELI

**Repaso rápido** (las mismas preguntas de «Antes de entregar» del reto en una página; contesta Sí / No / A medias):

| Pregunta | Mi respuesta |
| :---- | :---- |
| ¿El informe recoge todos los defectos con causa probable y tratamiento? | Sí |
| ¿El cuaderno se ejecuta de principio a fin sin errores? | Sí |
| ¿Imputación, escalado y codificación se ajustan **solo con train**? | Sí |
| ¿Hay un baseline (`DummyClassifier`) y un modelo comparados con validación cruzada? | Sí |
| ¿El README tiene instrucciones y versiones de librerías? | Sí |
| ¿Hemos respondido a la pregunta de IA responsable (país de origen, discriminación)? | Sí |
| ¿Está subido a Git, con autoevaluación y coevaluación? | Sí |

&nbsp;

**Puntúate de 1 a 4** en cada criterio de la rúbrica:

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
| :---- | :---- | :---- | :---- |
| Corrección técnica | 4 | He detectado y corregido los principales errores de los datos y he conseguido un modelo con resultados mejores que el azar.&nbsp; | Nada |
| Reproducibilidad | 3 | He automatizado la limpieza y la preparación de los datos mediante un pipeline, utilizando una semilla fija e indicando las versiones de las librerías.&nbsp; | Ejecutar todo el cuaderno en un Colab nuevo y comprobar que funciona sin errores.&nbsp; |
| Análisis y comunicación al cliente | 4 | He explicado los problemas encontrados, sus posibles causas, las soluciones aplicadas y las recomendaciones para el cliente.&nbsp; | Nada |
| IA responsable | 4 | He analizado el posible sesgo por país de origen y he decidido excluir esa variable porque no mejora los resultados y podría provocar discriminación.&nbsp; | Nada |

&nbsp;

- **Lo que más me costó fue** identificar y corregir todos los errores de los datos, **porque** había diferentes formatos de fechas, precios escritos de distintas maneras, valores imposibles y registros duplicados. También fue importante evitar las fugas de información al preparar el modelo.  
- **He usado IA para** ayudarme a redactar y explicar los resultados, organizar la información y comprender mejor algunos conceptos del análisis de datos. **Lo que he comprobado a mano es** los errores encontrados, las soluciones aplicadas, los resultados del modelo, las métricas AUC y la comparación entre utilizar o eliminar la variable del país de origen.

## 1\. Autoevaluación (cada persona, unos 5 minutos)

**Nombre:** FRAN

**Repaso rápido** (las mismas preguntas de «Antes de entregar» del reto en una página; contesta Sí / No / A medias):

| Pregunta | Mi respuesta |
| :---- | :---- |
| ¿El informe recoge todos los defectos con causa probable y tratamiento? | SI |
| ¿El cuaderno se ejecuta de principio a fin sin errores? | SI |
| ¿Imputación, escalado y codificación se ajustan **solo con train**? | SI |
| ¿Hay un baseline (`DummyClassifier`) y un modelo comparados con validación cruzada? | SI |
| ¿El README tiene instrucciones y versiones de librerías? | SI |
| ¿Hemos respondido a la pregunta de IA responsable (país de origen, discriminación)? | SI |
| ¿Está subido a Git, con autoevaluación y coevaluación? | SI |

&nbsp;

**Puntúate de 1 a 4** en cada criterio de la rúbrica:

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
| :---- | :---- | :---- | :---- |
| Corrección técnica | 3 | He participado en la preparación del cuaderno y en la interpretación de los resultados, con ayuda para comprender el código. | Realizar con el equipo una prueba del efecto de ajustar el preprocesado con todos los datos.&nbsp; |
| Reproducibilidad | 3 | Hemos comprobado que el cuaderno se ejecuta completo siguiendo el README y obtiene las mismas cifras, con versiones y semilla registradas.&nbsp; | Probar también la reproducción en un cuaderno nuevo de Colab y documentar el origen del CSV. |
| Análisis y comunicación al cliente | 4 | He trabajado en comprender los defectos y sus resultados y en preparar el informe con ayuda de IA; recoge diez defectos, prioridades, tratamientos, riesgos y límites del modelo.&nbsp; | Mantener este nivel y ganar autonomía para explicar al cliente los resultados con mis propias palabras.&nbsp; |
| IA responsable | 3 | Entiendo que imputar el país más frecuente puede atribuir una nacionalidad incorrecta; hemos explicado este riesgo con cifras y documentado el uso de IA y las comprobaciones.&nbsp; | Comparar el modelo con y sin país de origen, y documentar una medida evaluada y un fallo concreto de la IA si lo detectamos.&nbsp; |

&nbsp;

- **Lo que más me costó fue** entender cómo se relacionan las celdas y diferenciar la limpieza del preprocesado,&nbsp;  
- **porque t**odavía voy despacio con Python y necesito explicaciones paso a paso.  
- **He usado IA** para comprender las instrucciones de Python, organizar el cuaderno y redactar el informe; lo que he comprobado a mano es que las salidas de Colab coinciden con los recuentos del informe, las categorías escritas de distintas maneras, las cinco antelaciones incoherentes y los resultados antes y después de limpiar.  
- &nbsp;

## 1\. Autoevaluación (cada persona, unos 5 minutos)

**Nombre:** EVA

**Repaso rápido** (las mismas preguntas de «Antes de entregar» del reto en una página; contesta Sí / No / A medias):

| Pregunta | Mi respuesta |
| :---- | :---- |
| ¿El informe recoge todos los defectos con causa probable y tratamiento? | SI |
| ¿El cuaderno se ejecuta de principio a fin sin errores? | SI |
| ¿Imputación, escalado y codificación se ajustan **solo con train**? | SI |
| ¿Hay un baseline (`DummyClassifier`) y un modelo comparados con validación cruzada? | SI |
| ¿El README tiene instrucciones y versiones de librerías? | SI |
| ¿Hemos respondido a la pregunta de IA responsable (país de origen, discriminación)? | SI |
| ¿Está subido a Git, con autoevaluación y coevaluación? | SI |

&nbsp;

**Puntúate de 1 a 4** en cada criterio de la rúbrica:

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
| :---- | :---- | :---- | :---- |
| Corrección técnica | 3 | El trabajo funciona correctamente y cumple con los requisitos pedidos.&nbsp; | Nada |
| Reproducibilidad | 4 | El cuaderno se puede ejecutar de principio a fin sin errores.&nbsp; | Nada |
| Análisis y comunicación al cliente | 3 | He explicado los resultados de forma clara, aunque podría dar más detalles.&nbsp; | Mejoraría las explicaciones y añadiría algún ejemplo más.&nbsp; |
| IA responsable | 3 | &nbsp;He tenido en cuenta los posibles problemas de discriminación y el origen de los datos. | Mejoraría las explicaciones y añadiría algún ejemplo más.&nbsp; |

&nbsp;

- **Lo que más me costó fue** integrar que no se puede borrar nada sin antes comprobar de donde procede y si es reemplazable y no afecta al resto, y hacer copias despues de cada limpieza **porque** si borramos podemos arruinar la documentacion y si no guardamos por pasos seguiremos teniendo los datos sucios. En definitiva es tener más atención en ese aspecto.  
- **He usado IA para** resolver algunas dudas, entender mejor ciertos conceptos y ayudarme con partes del trabajo, **y lo que he comprobado a mano** es que el código funcionara correctamente, que los resultados fueran coherentes y que el cuaderno se ejecutara sin errores.  
- &nbsp;  
- &nbsp;

## 1\. Autoevaluación (cada persona, unos 5 minutos)

**Nombre:** JUKEIZA

**Repaso rápido** (las mismas preguntas de «Antes de entregar» del reto en una página; contesta Sí / No / A medias):

| Pregunta | Mi respuesta |
| :---- | :---- |
| ¿El informe recoge todos los defectos con causa probable y tratamiento? | SI |
| ¿El cuaderno se ejecuta de principio a fin sin errores? | SI |
| ¿Imputación, escalado y codificación se ajustan **solo con train**? | SI |
| ¿Hay un baseline (`DummyClassifier`) y un modelo comparados con validación cruzada? | SI |
| ¿El README tiene instrucciones y versiones de librerías? | SI |
| ¿Hemos respondido a la pregunta de IA responsable (país de origen, discriminación)? | SI |
| ¿Está subido a Git, con autoevaluación y coevaluación? | SI |

&nbsp;

**Puntúate de 1 a 4** en cada criterio de la rúbrica:

| Criterio | Mi puntuación (1–4) | Por qué (una frase) | Qué haría para subir un punto |
| :---- | :---- | :---- | :---- |
| Corrección técnica | 4 | El código funciona perfecto, está ordenado en una sola función y no hace trampas con los datos.&nbsp; | Nada. |
| Reproducibilidad | 3 | Dejamos escritas las versiones y la semilla para que a cualquiera le salgan los mismos números&nbsp; | Probar el archivo en una cuenta de Google Colab nueva para asegurar que no falla nada.&nbsp; |
| Análisis y comunicación al cliente | 4 | El resumen se entiende muy fácil, sin tecnicismos, y añadimos 4 preguntas clave para el cliente.&nbsp; | Nada. |
| IA responsable | 3 | Demostramos con datos cómo evitar sesgos y discriminación al quitar la variable de país. | Escribir un ejemplo real de un error o "alucinación" que tuvo la IA mientras hacíamos el trabajo.&nbsp; |

&nbsp;

- **Lo que más me costó fue** Lo que más me costó fue conseguir arreglar los dos formatos de fechas diferentes sin dañar nada, **porque** si te equivocas ahí, el modelo calcula mal los días de antelación y hace trampas sin que te des cuenta.&nbsp;  
- **He usado IA para** escribir los textos del informe y organizar las tablas, **y lo que he comprobado a mano es** que el código funcione, que los números del modelo sean los correctos y que no se borrase ninguna fila por error.&nbsp;

&nbsp;

---

> ## **2\. Coevaluación (durante la review, unos 10 minutos)**

**Trabajo revisado de (persona o equipo):** Error404  
**Revisado por (yo):** Todos

**¿Está lo que pide el reto? Marca ✔ (sí), ✘ (no) o — (no procede).**

| Entregable (nómbralo) | ¿Está y se entiende? | Comentario breve |
| :---- | :---- | :---- |
| **Informe de análisis y limpieza de datos** | **✔** | Recoge los doce defectos encontrados, sus posibles causas, tratamientos y prioridades. |
| **Cuaderno de Google Colab** | **✔** | Contiene la limpieza, el preprocesado y la comparación de modelos. Se indica que funciona de principio a fin. |
| **README y documentación en Git** | **✔** | Incluye instrucciones, versiones de librerías y semilla para reproducir los resultados. |

**Puntuación (1–4) de quien revisa:**

| Criterio | Puntuación | Comentario breve |
| :---- | :---- | :---- |
| **Corrección técnica** | 4 | El código está bien organizado, se han corregido los errores de los datos y se ha comparado el modelo con un baseline. |
| **Reproducibilidad** | 3 | Se han indicado las versiones y la semilla, aunque sería conveniente probar el cuaderno en un Colab nuevo. |
| **Análisis y comunicación al cliente** | 4 | El informe explica los defectos, las soluciones y los resultados de forma clara y comprensible. |
| **IA responsable** | 3 | Se ha analizado el posible sesgo por país de origen y se ha justificado la decisión de excluir esa variable. |

* **Lo que está muy bien:** Nos ha ayudado que el informe esté bien organizado y explique los problemas encontrados y cómo los hemos solucionado. También valoramos positivamente haber comparado el modelo con un baseline y haber tenido en cuenta el posible sesgo por país de origen.  
* **Lo que yo cambiaría, y por qué:** Probaríamos el cuaderno en una cuenta nueva de Google Colab para asegurarnos de que cualquier persona pueda ejecutarlo sin problemas. También añadiríamos un ejemplo concreto de algún error o alucinación de la IA y cómo lo comprobamos, para mejorar la parte de IA responsable.

&nbsp;