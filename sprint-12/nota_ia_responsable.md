# Nota de IA responsable · Sprint 12 · Escuchar al cliente

*Equipo: ERROR 404*

| Riesgo | Qué pasa | Medida | Cómo la medimos |
| :---- | :---- | :---- | :---- |
| El asistente responde a lo que no sabe | Sin umbral, a «¿Tienen gimnasio?» responde con la norma sobre fumar. | Aplicamos un umbral de 0,15 y devolvemos «No consta en la política del alojamiento.» si el mejor fragmento queda por debajo. | En 25 preguntas, pasamos de 22 aciertos y 2 alucinaciones detectadas sin umbral a 24 aciertos y 0 alucinaciones detectadas con umbral de 0,15. Con el umbral, el asistente se abstuvo ante las preguntas sobre gimnasio y sauna. |
| La respuesta cita una fuente que no resuelve la pregunta | Al preguntar por el horario del desayuno, cita la norma de media pensión, que no indica la hora. | Comprobamos si cada respuesta contiene la pista esperada, además de registrar si lleva fuente y si el detector señala una alucinación. | Hubo 24 aciertos de 25 y 0 respuestas sin fuente. Al revisar el único fallo, vimos que la cita era real y la respuesta era impertinente. El detector de alucinaciones no señaló ese caso. |
| Texto que intenta manipular al asistente | En las pruebas del simulador, prosperaron los 3 casos preparados sin defensa. | Probamos el filtro `es_seguro` para detectar texto sospechoso en preguntas y fragmentos. | Con el filtro prosperaron 0 de 3 casos y se bloquearon 0 de 25 preguntas legítimas y 0 de 25 fragmentos legítimos. En la prueba adicional, el filtro dejó pasar dos variantes. Su cobertura depende de los patrones que reconoce. |
| Datos personales en las reseñas | Las reseñas reales pueden contener nombres, teléfonos o referencias de reserva. Las del reto son sintéticas. | Si trabajamos con datos reales, retiraríamos los identificadores antes de guardar o analizar las reseñas y evitaríamos enviarlas a servicios externos de IA. | Medida propuesta para datos reales, pendiente de medir. |
| Sesgos y límites del clasificador | Puede confundir reseñas neutras con negativas y fallar con negaciones. | Documentamos estos límites en el informe y proponemos revisar manualmente los casos dudosos antes de usar la clasificación para actuar. | La matriz de confusión mostró 3 reseñas neutras clasificadas como negativas de 375 evaluadas. En una prueba adicional, «La limpieza no es impecable» se clasificó como positiva. |

**Uso de la IA:**&nbsp;

*Pedimos ayuda para entender y proponer cinco preguntas y redactar la nota. Comprobamos las respuestas con la política del alojamiento y las cifras con las salidas de Colab y el CSV. Ajustamos las pistas de evaluación para que correspondieran a las cinco preguntas del equipo.*