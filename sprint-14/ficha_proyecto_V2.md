# Ficha de proyecto (1 página) · Anexo A

**Equipo:** Error404 · **Fecha:** 26/11/2026 · **Versión:** 2 (pendiente de GO)

## 1\. Equipo y roles iniciales

| Persona | Rol en el Sprint 14 | Rotación prevista (S15 / S16) |
| :---- | :---- | :---- |
| Eli | Scrum Master | Técnico / Datos |
| Jukeiza | Responsable técnico | Datos / IA responsable |
| Fran | Responsable de datos | IA responsable / Scrum Master |
| Eva | Responsable de IA responsable | Scrum Master / Técnico |

## 2\. Brief elegido y pregunta de negocio

- **Brief:** 3 Asistente FP — OrientaFP Canarias.  
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

- **Métrica de negocio:** Reducir el tiempo medio de consulta de 3,18 a 1,59 minutos (50 %). Hemos medido ocho búsquedas manuales (145, 177, 183, 104, 142, 356, 251 y 167 segundos): media de 190,625 segundos y objetivo de 95,3125 segundos. Pendiente de medir el tiempo con el asistente.  
- **Métrica técnica:** Aciertos completos y fundamentados sobre 40 preguntas; Hit@1 para recuperación.  
- **Umbral de éxito acordado:** 36/40 (90 %).  
- **Baseline previsto:** TF-IDF \+ coseno; Hit@1 de desarrollo registrado: 11/12.  
- **Partición de los datos:** Corpus fijo; 12 preguntas de desarrollo y 40 de test reservado.

**Registro de tiempos de búsqueda manual**

| Consulta | Tiempo (segundos) | Tiempo (min:s) |
| :---- | ----: | ----: |
| ¿Qué centros de Tenerife imparten Desarrollo de Aplicaciones Web? | 145 | 2:25 |
| ¿Dónde puedo estudiar Farmacia y Parafarmacia en Gran Canaria? | 177 | 2:57 |
| ¿Qué centros de Lanzarote ofrecen FP de Informática? | 183 | 3:03 |
| ¿Qué requisitos de acceso tiene el ciclo de Administración y Finanzas? | 104 | 1:44 |
| ¿Cuáles son las salidas profesionales de Educación Infantil? | 142 | 2:22 |
| ¿Dónde puedo estudiar Desarrollo de Aplicaciones Multiplataforma a distancia en Canarias? | 356 | 5:56 |
| ¿Qué ciclos de FP de Sanidad se imparten en La Palma? | 251 | 4:11 |
| ¿Qué requisitos de acceso tiene el ciclo de Dietética y dónde se imparte en Tenerife? | 167 | 2:47 |
| **Total** | **1.525** | **25:25** |
| **Media de partida** | **190,625** | **3:10,625** |
| **Objetivo (−50 %)** | **95,3125** | **1:35,3125** |

## **2\. Páginas donde realizar las búsquedas**

* [Oferta de Formación Profesional del Gobierno de Canarias](https://www.gobiernodecanarias.org/educacion/web/formacion_profesional/?utm_source=chatgpt.com)  
* [TodoFP – Ministerio de Educación](https://www.todofp.es/?utm_source=chatgpt.com)  
* [Datos Abiertos del Gobierno de Canarias](https://datos.canarias.es/?utm_source=chatgpt.com)

&nbsp;

## 6\. Modelos previstos (≥ 3, incluyendo redes neuronales / LLM según el brief)

- **Enfoque elegido y por qué:** recuperación documental y RAG para citar fuentes y abstenerse sin evidencia.  
1. TF-IDF. 2\. BM25. 3\. Embeddings. 4\. LLM-RAG.

## 7\. Demostrador previsto

- **Tecnología:** Streamlit. **Qué hará:** responder con citas, curso y abstención.  
- **Plan B si falla la demo:** vídeo de 90 s.

## 8\. Riesgos y mitigación

| Riesgo | Tipo (datos / modelo / uso / legal / técnico) | Mitigación |
| :---- | :---- | :---- |
| Oferta antigua | Datos | Mostrar curso y advertir vigencia |
| Alucinaciones | Modelo | Citas y abstención |
| Datos de menores en consultas | Legal/uso | No solicitar ni persistir |

Clasificación preliminar AI Act: chatbot informativo con obligaciones de transparencia; confirmar con docente. Datos personales: posibles en contactos originales y consultas; excluirlos del corpus.

## 9\. Backlog inicial (10-15 historias) y objetivo de cada sprint

- **Historias principales:** datos, EDA, baseline, RAG, evaluación, riesgos y demo (15 historias).  
- **Objetivo S14:** datos y baseline · **Objetivo S15:** comparar y elegir candidato · **Objetivo S16:** evaluar y cerrar demo · **Objetivo S17:** defensa.

| ID | Historia |
| :---- | :---- |
| H1 | Como cliente quiero una ficha con alcance y métricas para aprobar el proyecto |
| H2 | Como responsable de datos quiero verificar las fuentes y licencias para usar datos legalmente |
| H3 | Como equipo quiero analizar los cuatro CSV para conocer su calidad |
| H4 | Como equipo quiero medir TF-IDF para tener referencia |
| H5 | Como responsable ético quiero documentar riesgos para evitar perjuicios |
| H6 | Como equipo quiero congelar preguntas independientes para evaluar sin fugas |
| H7 | Como equipo quiero comparar BM25 y embeddings con TF-IDF para elegir recuperador |
| H8 | Como estudiante quiero recibir respuestas RAG con citas para comprobar la información |
| H9 | Como equipo quiero registrar experimentos para elegir candidato |
| H10 | Como cliente quiero evaluar el candidato congelado para conocer su fiabilidad |
| H11 | Como responsable ético quiero medir errores por isla y tipo de pregunta para detectar desigualdades |
| H12 | Como estudiante quiero probar el chatbot para consultar oferta de FP |
| H13 | Como cliente quiero leer memoria y model card para entender límites |
| H14 | Como equipo quiero preparar presentación para explicar resultados |
| H15 | Como equipo quiero repartir la defensa para demostrar aprendizaje |

&nbsp;

---

**Firmas del equipo (nombres):** Eli, Jukeiza, Fran y Eva · **Respuesta del docente:** ☐ GO ☐ GO con cambios ☐ NO-GO — Comentarios: \_\_\_\_\_\_