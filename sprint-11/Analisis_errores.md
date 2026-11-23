# Análisis de errores · Visión artificial para el cliente (Sprint 11\)

## 1\. Qué se ha hecho y con qué datos

Para **TurisData Canarias** se ha probado un modelo que preclasifica imágenes de alojamientos en cinco categorías: apartamentos, camping, casa\_rural, hotel y piscina. El objetivo es ayudar a revisar las imágenes, no sustituir todavía la revisión humana.

Se ha utilizado el conjunto **sintético generado por el propio cuaderno del curso**: 300 imágenes (60 por clase). Son dibujos creados por código, no fotografías reales ni imágenes descargadas de terceros; por tanto, no se ha utilizado material fotográfico externo sujeto a licencias de terceros. La partición, con semilla `42`, es de **180 imágenes de entrenamiento, 60 de validación y 60 de prueba** (60 % / 20 % / 20 %).

Se ha entrenado un modelo con *transfer learning* y ajuste fino (*fine-tuning*), y se ha comparado con un modelo entrenado desde cero.

## 2\. Resultados

| Clase | Precisión | Recall |
| :---- | :---- | :---- |
| apartamentos | 0,86 | 0,86 |
| camping | 0,46 | 0,60 |
| casa\_rural | 0,67 | 0,62 |
| hotel | 0,82 | 0,82 |
| piscina | 1,00 | 0,83 |

Exactitud en prueba: transfer \+ fine-tuning **0,750** · desde cero **0,683**. F1 macro: **0,749** y **0,678**, respectivamente. El modelo con ajuste fino obtiene mejores resultados en esta prueba, aunque el conjunto de prueba es pequeño (60 imágenes).

## 3\. La matriz de confusión

Se han producido **15 errores de 60 imágenes**. Las confusiones más frecuentes son **casa\_rural → camping (5)** y **camping → casa\_rural (4)**. También hay **apartamentos → hotel (2)**, **hotel → apartamentos (2)** y **piscina → camping (2)**. La clase más difícil según el *recall* es **camping (0,60)**.

## 4\. Los errores

Se muestran ocho de los errores con mayor confianza del modelo, según la salida del cuaderno. Se ha comprobado en Colab que las 60 imágenes de prueba coinciden con sus respectivas rutas (60 de 60). Las causas propuestas son hipótesis visuales, no errores de etiquetado confirmados.

| Foto | Verdadera | Predicha | Confianza | Hipótesis de causa | Mejora propuesta |
| :---- | :---- | :---- | :---- | :---- | :---- |
| apartamentos/img\_043.png | apartamentos | hotel | 96 % | El edificio alto y sus ventanas se parecen a la representación de un hotel. | Añadir ejemplos de apartamentos altos y definir mejor las diferencias visuales. |
| camping/img\_045.png | camping | casa\_rural | 95 % | La imagen parece mostrar una casa con tejado, no una tienda de campaña. | Revisar la etiqueta y el generador de imágenes de esta clase. |
| camping/img\_020.png | camping | casa\_rural | 94 % | Aparece una construcción con tejado similar a una casa rural. | Comprobar la etiqueta y revisar otros casos semejantes. |
| casa\_rural/img\_046.png | casa\_rural | camping | 93 % | La figura se asemeja a una tienda de campaña. | Revisar el dibujo y la etiqueta de este ejemplo. |
| piscina/img\_012.png | piscina | camping | 92 % | Se observa una figura triangular parecida a una tienda, no una piscina. | Revisar si el dibujo representa claramente la clase. |
| hotel/img\_037.png | hotel | apartamentos | 92 % | El edificio bajo y ancho se parece a unos apartamentos. | Incluir más ejemplos de hoteles bajos y apartamentos similares. |
| camping/img\_043.png | camping | casa\_rural | 89 % | La imagen muestra una construcción con tejado rojo. | Revisar las etiquetas de la clase camping. |
| casa\_rural/img\_025.png | casa\_rural | camping | 87 % | La figura triangular recuerda a una tienda de campaña. | Revisar el dibujo y añadir ejemplos de casas rurales más variados. |

La comprobación de correspondencia entre las 60 imágenes de prueba y sus rutas ha resultado correcta (60/60). Algunos errores de alta confianza sugieren posibles semejanzas visuales entre categorías o problemas en los dibujos sintéticos; conviene revisar sus etiquetas antes de sacar conclusiones definitivas.

## 5\. Recomendación al cliente

Con un umbral de **0,7**, elegido mediante validación, el modelo decide solo el **80 %** de las fotos de prueba y acierta el **77 %** de las que acepta; el **20 %** restante lo revisa una persona.

**Recomendamos utilizarlo únicamente como apoyo con revisión humana**, no para clasificar automáticamente todas las imágenes. Primero se deben revisar las etiquetas dudosas, repetir la evaluación y probar el sistema con fotografías reales antes de plantear su uso operativo.

## 6\. Riesgos de IA responsable

1. Riesgo: **dibujos sintéticos ambiguos o etiquetas que no reflejan claramente su contenido visual**. Pueden distorsionar el entrenamiento y la evaluación, incluso cuando el modelo predice con mucha confianza. Medida: revisar manualmente los errores más seguros, corregir únicamente las etiquetas que se demuestren incorrectas y volver a evaluar.  
2. Riesgo: **los datos son dibujos sintéticos, no fotografías reales de alojamientos**. El rendimiento puede cambiar con iluminación, fondos, ángulos y contenidos reales. Medida: validar el modelo con fotografías reales obtenidas con permiso o licencia adecuada y mantener la revisión humana hasta comprobar su fiabilidad.