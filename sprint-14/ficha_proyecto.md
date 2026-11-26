# Ficha de proyecto (1 página) · Anexo A

**Equipo (nombre de la consultora):** Error404 · **Fecha:** 26/11/2026&nbsp;

## 1\. Equipo y roles iniciales

| Persona | Rol en el Sprint 14 | Rotación prevista (S15 / S16) |
| :---- | :---- | :---- |
| Eli | Scrum Master | Técnico / Datos |
| Jukeiza | Responsable técnico | Datos / IA responsable |
| Fran | Responsable de datos | IA responsable / Scrum Master |
| Eva | Responsable de IA responsable | Scrum Master / Técnico |

## 2\. Brief elegido y pregunta de negocio

- **Brief:** 3 Asistente FP — OrientaFPCanarias.  
- **Pregunta de negocio en una frase:** ¿Podemos crear un asistente que responda a dudas para que una persona interesada pueda elegir qué ciclos vale la pena considerar?

## 3\. Cliente y decisión que se apoyará

- **Quién usará el resultado:** alumnado, familias y orientadores.  
- **Decisión concreta que mejorará:** localizar ciclos, centros y modalidades; hoy exige búsquedas dispersas. No decide admisiones.

## 4\. Datos

| Fuente (enlace) | Licencia | Tamaño | Variables clave | Limitaciones previstas |
| :---- | :---- | :---- | :---- | :---- |
| [Centros educativos de Canarias](https://datos.canarias.es/catalogos/general/dataset/centros-educativos-de-canarias) | CC BY 4.0 | 34.906 filas; 2.751 documentos FP | Centro, isla, nivel, estudio, modalidad, curso | Oferta histórica, cobertura desigual, requisitos no incluidos |

*Debe ser real, accesible y con licencia. Detalle en `plan_datos_licencias.md`.*

## 5\. Métrica de éxito y baseline

- **Métrica de negocio:** Reducir un 50 % el tiempo de consulta (propuesta sin medir).  
- **Métrica técnica:** Aciertos completos y fundamentados sobre 40 preguntas; Hit@1 para recuperación.  
- **Umbral de éxito acordado:** 36/40 (90 %, pendiente de aprobación).  
- **Baseline previsto:** TF-IDF \+ coseno; Hit@1 de desarrollo registrado: 11/12.  
- **Partición de los datos:** Corpus fijo; 12 preguntas de desarrollo y 40 de test reservado.

## 6\. Modelos previstos (≥ 3, incluyendo redes neuronales / LLM según el brief)

- **Enfoque elegido y por qué:** recuperación documental y RAG para citar fuentes y abstenerse sin evidencia.  
1. TF-IDF. 2\. BM25. 3\. Embeddings. 4\. LLM-RAG.

## 7\. Demostrador previsto

- **Tecnología:** Streamlit. **Qué hará:** responder con citas, curso y abstención.  
- **Plan B si falla la demo:** vídeo de 90 s.

## 8\. Riesgos y mitigación

| Riesgo | Tipo (datos / modelo / uso / legal / técnico) | Mitigación |
| :---- | :---- | :---- |
| Oferta antigua | Un ciclo figuraba en un curso anterior y el chat podría presentarlo como disponible ahora.&nbsp; | Mostrar **el curso académico de la fuente** y advertir si la información es histórica o provisional.&nbsp; |
| Alucinaciones | El chat podría inventar un centro, un requisito o una salida profesional, incluso incluyendo una cita que no respalde lo que afirma.&nbsp; | Citar **la fuente que respalda la afirmación**. Si falta evidencia, responder «No tengo información suficiente para confirmarlo». Eso es la **abstención**.&nbsp; |
| Datos de menores en consultas | Una persona menor de edad podría escribir su nombre, DNI o teléfono al pedir orientación.&nbsp; | **No solicitar ni guardar** esos datos. Si vais a usar una API externa, evitad también enviárselos y pedid que la consulta se reformule sin ellos&nbsp; |

&nbsp;

## 9\. Backlog inicial (10-15 historias) y objetivo de cada sprint

- **Historias principales:** datos, EDA, baseline, RAG, evaluación, riesgos y demo (15 historias).  
- **Objetivo S14:** datos y baseline · **Objetivo S15:** comparar y elegir candidato · **Objetivo S16:** evaluar y cerrar demo · **Objetivo S17:** defensa.

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;