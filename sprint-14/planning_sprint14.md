# Sprint Planning – Sprint 14

**Proyecto:** OrientaFP Canarias · **Equipo:** Error404  
**Fecha:** [Fecha real de la reunión] · **Scrum Master:** Eli

## 1. Participantes

| Persona | Rol |
|---|---|
| Eli | Scrum Master |
| Jukeiza | Responsable técnico |
| Fran | Responsable de datos |
| Eva | Responsable de IA responsable |

## 2. Objetivo del sprint

Nuestro objetivo es definir el proyecto, disponer de un corpus fiable y documentado, analizar su calidad y establecer un baseline para comparar los modelos posteriores.

## 3. Sprint Backlog

| ID | Tarea | Responsable | Prioridad |
|---|---|---|---|
| H1 | Elaborar la ficha del proyecto | Eli | Alta |
| H2 | Verificar fuentes y licencias | Fran | Alta |
| H3 | Preparar el corpus y realizar el EDA | Fran | Alta |
| H4 | Implementar el baseline TF-IDF | Jukeiza | Alta |
| H5 | Documentar riesgos éticos | Eva | Alta |
| H6 | Preparar y congelar el test final | Equipo | Alta |

## 4. Plan de trabajo

- Definir la pregunta de negocio y las métricas.
- Descargar y verificar los cuatro CSV originales.
- Ampliar el corpus con requisitos de acceso y salidas profesionales de fuentes oficiales.
- Documentar licencias y condiciones de reutilización.
- Realizar el EDA e implementar TF-IDF con similitud coseno.
- Preparar 12 preguntas de desarrollo y 40 de test.
- Medir ocho búsquedas manuales.
- Documentar riesgos y preparar instrucciones de reproducción.

## 5. Criterios de aceptación

- Ficha con pregunta de negocio y métricas medibles.
- Fuentes y licencias documentadas; corpus con identificadores únicos.
- Cuadernos EDA y baseline ejecutables y métrica de referencia registrada.
- Test: 20 preguntas directas, 8 de varias fuentes, 8 sin respuesta y 4 intentos de engaño.
- Tiempo de partida medido y objetivo de reducción del 50 % calculado.
- Riesgos identificados e instrucciones de reproducción disponibles.

## 6. Riesgos y dependencias

| Riesgo | Medida prevista |
|---|---|
| Licencias no verificadas | Consultar condiciones oficiales. |
| Información desactualizada | Identificar curso y fecha de consulta. |
| Corpus incompleto | Ampliar y contrastar fuentes. |
| Alucinaciones | Prever citas y abstención. |
| Fuga de información del test | Separar desarrollo y evaluación. |
| Falta de reproducibilidad | Documentar dependencias, scripts y SHA-256. |

## 7. Entregables previstos

- `ficha_proyecto.md`, `plan_datos_licencias.md`, `backlog_y_sprints.md`, `riesgos_eticos.md`
- `descargar_datos.py`, `01_eda.ipynb`, `02_baseline.ipynb`
- `corpus_fp_canarias_ampliado.csv`, `informacion_fp_oficial.csv`, `preguntas_desarrollo.csv`, `set_preguntas.csv`
- `README.md`, `scrum/tablero_sprint14.md`

## 8. Seguimiento del sprint

Utilizaremos un tablero Scrum con tres estados: pendiente, en proceso y completado. Cada integrante actualizará sus tareas y comunicará los bloqueos al Scrum Master. Al finalizar revisaremos los entregables, resultados y mejoras para el Sprint 15.

**Validación del equipo:** [Pendiente de confirmar]. Documento reconstruido; no acredita por sí mismo la celebración de la reunión.
