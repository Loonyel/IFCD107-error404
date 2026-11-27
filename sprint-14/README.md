# OrientaFPCanarias · Error404

**Brief:** 3 Asistente FP · **Curso:** IFCD107 · Especialista en IA · **Defensa:** día 2 del Sprint 17

## 1. El problema en 3 líneas

- **Pregunta de negocio:** ¿Podemos crear un asistente que responda a dudas para que una persona interesada pueda elegir qué ciclos vale la pena considerar?  
- **Decisión que apoya y para quién:** Alumnado, familias y orientadores: localizar ciclos, centros y modalidades y consultar requisitos y salidas profesionales; no decide admisiones.  
- **Métrica de éxito:** negocio: reducir de 3,18 a 1,59 minutos (50 %; ocho búsquedas manuales, media de 190,625 s) · técnica: 36/40 respuestas completas y fundamentadas (90 %) · baseline: TF-IDF + coseno, Hit@1 de desarrollo 11/12 (91,67 %)

## 2. Resultados en una tabla

| Modelo | Métrica principal (validación) | Métrica en test | Tiempo | Notas |
| :---- | :---- | :---- | :---- | :---- |
| Baseline (TF-IDF + coseno) | Hit@1: 11/12 (91,67 %) | Hit@1: 13/28 (46,43 %); Hit@5: 19/28 (67,86 %) | 3,82 s (cuaderno completo, Linux) | Corpus de 2.914 documentos; 12 preguntas sin respuesta/adversariales no evaluables como respuestas por el recuperador. Test ya consultado: reservar otro independiente si se usa para mejorar el modelo. |
| Modelo 1&nbsp; |  |  |  | \[Sprint 15\] |
| Modelo 2&nbsp; |  |  |  | \[Sprint 15\] |
| **Candidato final** |  |  |  |  |

*(Detalle en `sprint-16/docs/memoria_tecnica.pdf` y en `sprint-15/registro.csv`.)*

## 3. Estructura del repositorio

```
.                              # raíz del repositorio del equipo (ifcd107-equipo-…)
├── README.md                  # este archivo (la puerta de entrada)
├── requirements.txt           # versiones fijas
├── sprint-14/                 # definición y punto de partida
│   ├── ficha_proyecto.md
│   ├── plan_datos_licencias.md   # fuente, licencia, cómo descargar los datos
│   ├── 01_eda.ipynb
│   ├── 02_baseline.ipynb
│   ├── backlog_y_sprints.md
│   ├── riesgos_eticos.md
│   ├── descargar_datos.py     # solo si no subís los datos
│   └── scrum/
│       ├── tablero_sprint14.md
│       └── planning_sprint14.md
├── sprint-15/                 # experimentos
│   ├── registro.csv           # registro de experimentos
│   ├── 03_modelos.ipynb
│   ├── justificacion_candidato.md
│   ├── modelo_candidato.joblib, metadatos.json, explicacion_modelo.png
├── sprint-16/                 # entrega final
│   ├── README.md              # versión final de este README
│   ├── notebooks/04_evaluacion.ipynb
│   ├── demostrador/           # logica.py, app.py, tests/, requirements.txt
│   └── docs/                  # memoria_tecnica.pdf, model_card.md, riesgos_eticos.md, demo.mp4 (si pesa poco)
└── sprint-17/                 # defensa
    └── presentacion_defensa.pdf, plantilla_storytelling.md
```

*(Cada `sprint-NN/` lleva además una hoja `autoevaluacion_nombre.md` por persona. La coevaluación confidencial del anexo B **no se sube**: se entrega al docente.)*

## 4. Cómo reproducirlo (pasos exactos)

**Requisitos:** Python 3.13.5 (registrada en los cuadernos ejecutados) · Linux (entorno de ejecución de los cuadernos) · GPU: no para el baseline; \[candidato pendiente\]

```sh
git clone [url-del-repositorio]
cd [carpeta]
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python sprint-14/descargar_datos.py --solo-verificar   # verifica las copias originales locales (1,59 s medidos)
# Si faltan los CSV originales: python sprint-14/descargar_datos.py (descarga en directo pendiente de prueba; tiempo no medido)
# Coloca los cuatro CSV originales, corpus_fp_canarias_ampliado.csv, informacion_fp_oficial.csv,
# mapa_ensenanzas_fichas.csv, control_consolidacion.json y preguntas_desarrollo.csv en sprint-14/.
# Abre los cuadernos con directorio de trabajo sprint-14/ (en Colab, sube esos archivos al entorno).
# El script no reconstruye las fichas ampliadas; usa las copias consolidadas y las evidencias de revisión.
# después, ejecuta los cuadernos en orden: sprint-14/01_eda.ipynb, sprint-14/02_baseline.ipynb,
# sprint-15/03_modelos.ipynb y sprint-16/notebooks/04_evaluacion.ipynb
```

Tiempo total medido del Sprint 14 con datos locales y dependencias instaladas: 13,64 s (0,23 minutos): verificación 1,59 s, EDA 8,23 s y baseline 3,82 s. Una ejecución por etapa en Linux con Python 3.13.5, incluyendo arranque de los cuadernos. No incluye descarga, instalación, preparación inicial de fichas ni sprints posteriores. \[Tiempo total del proyecto pendiente\]. **Semilla fija:** `SEMILLA = 42` (definida en la primera celda de cada cuaderno).

## 5. Cómo lanzar el demostrador

```sh
cd sprint-16/demostrador
streamlit run app.py               # o: uvicorn api:app --reload
```

Se abre en [http://localhost:8501](http://localhost:8501). **Plan B:** vídeo en `sprint-16/docs/demo.mp4` \[o enlace\]. **Qué probar:** Ejemplos previstos (demostrador aún no implementado): «¿Dónde estudiar DAW en Tenerife?» (centros y curso con citas); «¿Qué requisitos tiene Farmacia y Parafarmacia?» (vías de acceso, sin garantizar plaza); «¿Qué salidas tiene Educación Infantil?» (ocupaciones con fuente).. **Entradas que no admite y qué mensaje muestra:** Ejemplo previsto: pedir una tasa de empleo no disponible o inventar una fuente; debe indicar que no dispone de evidencia suficiente, sin inventar datos. \[Mensaje definitivo pendiente\]..

## 6. Datos y licencias

| Conjunto | Fuente | Licencia | ¿Incluido en el repo? |
| :---- | :---- | :---- | :---- |
| Cuatro CSV originales: centros, enseñanzas autorizadas, impartidas y servicios complementarios | [Gobierno de Canarias](https://datos.canarias.es/catalogos/general/dataset/centros-educativos-de-canarias) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) y [condiciones del portal](https://datos.canarias.es/portal/aviso-legal-y-condiciones-de-uso) | Incluidos en ZIP local; |
| Fichas TodoFP | [TodoFP](https://www.todofp.es/que-estudiar/familias-profesionales.html) | [Aviso legal propio](https://www.todofp.es/comunes/aviso-legal.html); reconfirmar redistribución | Incluidas en corpus local;&nbsp; |
| Normativa FP Adaptada y cualificaciones | [BOC](https://www.gobiernodecanarias.org/boc/2025/046/918.html) y [BOE](https://www.boe.es/) | Resúmenes propios de textos normativos con cita; no se atribuye CC BY automáticamente | Incluidos en corpus local; |

**No hay datos personales** **en el repositorio:** No confirmado para todo el repositorio. Los CSV originales pueden contener contactos o titulares identificables; excluimos contactos innecesarios del corpus y no solicitaremos ni persistiremos datos personales de usuarios.

## 7. IA responsable (resumen)

- **Clasificación de riesgo (AI Act):** limitado (clasificación preliminar de chatbot informativo con transparencia; pendiente de confirmar con docente). Datos personales: posibles en fuentes originales y consultas; no previstos en corpus..  
- **Principales riesgos y medidas:** Oferta histórica: mostrar curso y advertir vigencia. Alucinaciones y engaños: citar fuentes y abstenerse sin evidencia. Cobertura desigual y fichas pendientes de revisión: comunicar límites y revisar por isla y tipo de pregunta. Privacidad: no solicitar ni guardar datos personales.. Detalle en `sprint-16/docs/riesgos_eticos.md` y `sprint-16/docs/model_card.md`.  
- **Limitaciones y usos no permitidos:** No garantiza admisión, empleo ni vigencia de la oferta; no sustituye orientación profesional. Oferta 2025/26 y fichas consultadas en noviembre de 2026; 154 fichas ordinarias pendientes de revisión humana. No inventar fuentes ni tratar datos sensibles..  
- **Uso de IA:** Hemos pedido ayuda a la IA para preparar código, cuadernos, contraste de fichas, documentación y preguntas. Fran confirmó CC BY 4.0 de los cuatro CSV originales; se documentaron las condiciones propias de TodoFP, BOE y BOC. Registramos ocho tiempos manuales y adaptamos el corpus y las preguntas. La revisión humana completa de las fichas y la autorización de redistribución siguen pendientes..

## 8. Equipo y contribuciones

| Persona | Roles (S14 / S15 / S16) | Contribución principal (enlaces a commits / PR) |
| :---- | :---- | :---- |
| Eli | Scrum Master / Técnico / Datos | Coordinación prevista; \[commits / PR pendientes de acreditar\] |
| Jukeiza | Técnico / Datos / IA responsable | Desarrollo técnico previsto; \[commits / PR pendientes de acreditar\] |
| Fran | Datos / IA responsable / Scrum Master | Verificación de licencia de los cuatro CSV; \[commits / PR pendientes de acreditar\] |
| Eva | IA responsable / Scrum Master / Técnico | Gestión de riesgos prevista; \[commits / PR pendientes de acreditar\] |

Convención de commits: `tipo: descripción` (`feat:`, `fix:`, `docs:`, `data:`, `exp:`). **Todas las personas** deben tener commits propios.

## 9. Evidencias de metodología

- Tablero: [Tablero Scrum del Sprint 14](sprint-14/scrum/tablero_sprint14.md) · Backlog ([backlog_y_sprints.md](sprint-14/backlog_y_sprints.md)): hemos organizado el trabajo mediante Scrum, con asignación y rotación de roles · Planning: [Sprint Planning del Sprint 14](sprint-14/scrum/planning_sprint14.md) (fecha y validación del equipo pendientes) · Review / retro de cada sprint: [evidencias pendientes de incorporar].

## 10. Créditos y licencia del código

Datos: Gobierno de Canarias, Centros educativos de Canarias, oferta 2025/26, [fuente](https://datos.canarias.es/catalogos/general/dataset/centros-educativos-de-canarias), [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); hemos filtrado, limpiado, unido y transformado los datos. Ministerio de Educación, FP y Deportes, TodoFP, consulta 26/11/2026, aviso legal propio; BOC y BOE, resúmenes normativos con cita. Proyecto independiente, sin respaldo institucional. Detalle en `sprint-14/plan_datos_licencias.md`.. Librerías principales: pandas 2.2.3, numpy 2.3.5, scikit-learn 1.8.0 y matplotlib 3.10.8 (según requirements.txt). Licencia del código: \[MIT / propia\].

## Revisión con la rúbrica

\<Sprint 14\. Rúbrica completa en `entrega_y_rubrica.md` de la carpeta `2_Entregar` del sprint, apartado 3\. Rellena quien revisa y **no escribió esa parte**: seguir solo este README para descargar los datos y ejecutar los cuadernos, leer la ficha como cliente, comprobar la fuente y la licencia, poner nivel con prueba.\>

**Revisado por:**             **Fecha:**&nbsp;&nbsp;

&nbsp;

| Criterio | Nivel (1–4) | Prueba: una frase de lo que has comprobado |
| :---- | :---- | :---- |
| Corrección técnica |  |  |
| Reproducibilidad |  |  |
| Análisis y comunicación al cliente |  |  |
| IA responsable |  |  |

**Lo primero que mejoraríamos:** \<una cosa concreta\>
