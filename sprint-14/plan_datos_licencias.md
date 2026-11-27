# Plan de datos y licencias — OrientaFP

**Equipo:** Error404 · **Responsable:** Fran · **Sprint:** 14 · **Última actualización:** 26/11/2026

## 1\. Inventario de fuentes

Fuente: Gobierno de Canarias, Consejería de Educación. Catálogo: [https\://datos.canarias.es/catalogos/general/dataset/centros-educativos-de-canarias](https://datos.canarias.es/catalogos/general/dataset/centros-educativos-de-canarias). Aviso legal revisado el 26/11/2026: [https\://datos.canarias.es/portal/aviso-legal-y-condiciones-de-uso](https://datos.canarias.es/portal/aviso-legal-y-condiciones-de-uso) (apartado 3): CC BY 4.0 salvo excepción. Uso académico y redistribución permitidos con atribución, conservación de metadatos, identificación de cambios y respeto a privacidad. Fecha exacta de descarga original pendiente de confirmación por Fran; las copias aportadas con sufijo `_actual` coinciden byte a byte (apartado 9).

| Archivo | Filas | Columnas | Bytes |
| :---- | ----: | ----: | ----: |
| centros.csv | 1472 | 33 | 1233240 |
| ensenanzas-impartidas-por-centro.csv | 18324 | 11 | 3901309 |
| ensenanzas-autorizadas-por-centro.csv | 14138 | 22 | 6671034 |
| servicios-complementarios-por-centro.csv | 972 | 5 | 27334 |

### Inventario ampliado

| ID | Fuente y organismo | Fecha de consulta | Condiciones de uso | Formato / alcance | Datos personales |
| :---- | :---- | :---- | :---- | :---- | :---- |
| D1–D4 | Cuatro CSV del Gobierno de Canarias (enlaces en apartado 8\) | 26/11/2026, revisión de copias | CC BY 4.0; atribución y cambios identificados | CSV, tamaños arriba | Posibles contactos identificativos |
| D5 | [TodoFP, Ministerio de Educación, Formación Profesional y Deportes](https://www.todofp.es/que-estudiar/familias-profesionales.html) | 26/11/2026 | [Aviso legal](https://www.todofp.es/comunes/aviso-legal.html): reproducción textual condicionada a integridad y atribución, según revisión previa; reconfirmar antes de redistribuir | HTML; 228 fichas recopiladas, 412 correspondencias ordinarias aprobadas | No previstos en los apartados seleccionados |
| D6 | [BOC, Resolución de 21 de febrero de 2025](https://www.gobiernodecanarias.org/boc/2025/046/918.html) | 26/11/2026 | Disposición normativa, art. 13 TRLPI; resumen propio con cita | HTML; 7 registros de FP Adaptada | No extraemos datos individuales |
| D7 | BOE, disposiciones sobre cualificaciones profesionales (enlaces en apartado 10\) | 26/11/2026 | Disposiciones normativas, art. 13 TRLPI; resúmenes propios con cita | HTML/PDF; 6 cualificaciones | No extraemos datos individuales |
| D8 | Catálogos nacionales TodoFP 2026 y 26 folletos de familias | Aportados el 26/11/2026 | No incorporamos imágenes ni reproducimos los PDF; condiciones específicas pendientes si se redistribuyen | PDF, apoyo para identificar títulos | No previstos |

No usamos el catálogo nacional para afirmar que un ciclo se imparte en Canarias. La oferta local se acredita con D1–D4, especialmente enseñanzas impartidas.

## 2\. Diccionario y calidad de variables

### centros.csv

| Variable | Tipo observado | Nulos (%) |
| :---- | :---- | ----: |
| Codigo | int64 | 0.00 |
| Denominacion | object | 0.00 |
| DesEtapaCentro | object | 0.00 |
| DescripcionEtapaCentro | object | 0.00 |
| Direccion | object | 0.00 |
| Localidad | object | 0.00 |
| CodigoPostal | int64 | 0.00 |
| Municipio | object | 0.00 |
| Isla | object | 0.00 |
| Provincia | object | 0.00 |
| Telefono | object | 0.34 |
| Fax | object | 73.44 |
| CorreoElectronico | object | 0.68 |
| SegundoCorreoElectronico | object | 86.35 |
| PaginaWeb | object | 25.61 |
| Naturaleza | object | 0.00 |
| TipoCentro | object | 0.00 |
| Titular | object | 0.00 |
| CentroCER | float64 | 91.85 |
| PreferenteAuditivoMotorico | object | 92.53 |
| ColectivoEscuelasRurales | object | 91.85 |
| CentroProfesores | object | 18.75 |
| URLWebCEP | object | 18.75 |
| CentroDestino | object | 63.86 |
| EOEP | object | 26.43 |
| CentroCepaAlQuePertenece | object | 88.79 |
| FotoCentro | object | 72.28 |
| DescargarMapaCentroGoogleEarth | object | 0.00 |
| VerMapaCentroGoogleMaps | object | 1.29 |
| Longitud | float64 | 1.29 |
| Latitud | float64 | 1.29 |
| DescargarZonasInfluenciaCentroGoogleEarth | object | 0.00 |
| Concierto | object | 0.00 |

### ensenanzas-impartidas-por-centro.csv

| Variable | Tipo observado | Nulos (%) |
| :---- | :---- | ----: |
| CodigoCentro | int64 | 0.00 |
| DenominacionCentro | object | 0.00 |
| Nivel | object | 0.00 |
| Familia | object | 0.00 |
| Estudio | object | 0.00 |
| Modalidad | object | 0.00 |
| Ratio | int64 | 0.00 |
| CodigoEstudio | int64 | 0.00 |
| Longitud | float64 | 1.64 |
| Latitud | float64 | 1.64 |
| CursoEscolar | object | 0.00 |

### ensenanzas-autorizadas-por-centro.csv

| Variable | Tipo observado | Nulos (%) |
| :---- | :---- | ----: |
| CursoEscolar | int64 | 0.00 |
| CodigoCentro | int64 | 0.00 |
| DenominacionCentro | object | 0.00 |
| GrupoEnsenanza | object | 0.00 |
| Nivel | object | 0.00 |
| Familia | object | 0.00 |
| Ciclo | object | 4.93 |
| Estudio | object | 0.00 |
| Modalidad | object | 0.00 |
| Ratio | int64 | 0.00 |
| CodigoEstudio | int64 | 0.00 |
| DescargarMapaCentroGoogleEarth | object | 0.30 |
| VerMapaCentroGoogleMaps | object | 0.30 |
| Longitud | float64 | 0.30 |
| Latitud | float64 | 0.30 |
| Curso | float64 | 9.53 |
| OrdenGrupo0 | float64 | 4.98 |
| OrdenNivel | float64 | 4.98 |
| OrdenFamilia | float64 | 5.54 |
| AlumnosPRE | float64 | 6.00 |
| Vacantes | float64 | 6.00 |
| MatAltaPincel | float64 | 6.00 |

### servicios-complementarios-por-centro.csv

| Variable | Tipo observado | Nulos (%) |
| :---- | :---- | ----: |
| CodigoCentro | int64 | 0.00 |
| ComedorEscolar | object | 12.35 |
| TransporteEscolar | object | 12.35 |
| Desayuno | object | 12.35 |
| AperturaAntesHorarioLectivo | object | 12.35 |

### revision\_aprobada.csv (última versión, 419 filas y 41 columnas)

| Variable | Tipo / significado | Valores válidos | Nulos |
| :---- | :---- | :---- | ----: |
| Estudio, Nivel, Familia | Texto; clave de correspondencia local | Denominaciones de la oferta | 0 % en la clave conjunta |
| ciclo, clave | Texto; título y nombre normalizado | Titulación correspondiente | Revisar en EDA |
| requisitos\_acceso | Texto; acceso académico o normativo | Apartado oficial o resumen identificado | 0 % |
| salidas\_profesionales | Texto; ocupaciones o perfiles relacionados | Apartado oficial o resumen identificado | 0 % |
| continuidad\_estudios | Texto; opciones posteriores | Apartado oficial cuando exista | 1,67 % (7) |
| fuente, fecha\_consulta | URL y fecha ISO | Fuente oficial, 2026-11-26 | 0 % |
| licencia, licencia\_verificada | Texto; condiciones y referencia | TodoFP o disposición normativa | 0 % en referencia |
| aprobada, alcance\_aprobacion | Texto; estado y alcance | SI; estructural o normativa | 0 % |
| campos \*\_web, \*\_contraste, sha256\_html | Texto; evidencias de contraste | Valores registrados cuando aplican | No exigibles en FP Adaptada |
| codigo\_cualificacion, anexo\_boc, fuente\_salidas | Texto; trazabilidad normativa | Códigos y fuentes de FP Adaptada | No aplicables a FP ordinaria |

## 3\. Calidad

- Duplicados exactos: cero en los cuatro archivos.  
- Enseñanzas impartidas: 18.323 registros de 2025/26 y uno de 2024/25.  
- Enseñanzas autorizadas: 2.792 registros del grupo FORMACIÓN PROFESIONAL.  
- Cobertura desigual por isla. Revisar claves, valores imposibles y duplicados semánticos en el EDA.

## 4\. Linaje de los datos

CSV originales → selección de FP → unión por Codigo/CodigoCentro → selección de columnas → corpus de búsqueda. Script de oferta: 01\_eda.ipynb; ampliación y consolidación descritas en el apartado 11\. Huellas SHA-256 de los archivos locales indicadas abajo.

## 5\. Partición y congelación propuesta

Corpus documental fijo; separar preguntas de desarrollo y test por grupos de intención, evitando paráfrasis entre conjuntos. Disponemos de 12 preguntas de desarrollo y 40 de test final actualizado. Hemos fijado la versión candidata mediante SHA-256 (apartado 12); la aprobación del equipo y del docente sigue pendiente.

## 6\. Privacidad

Los CSV incluyen datos de contacto y titularidad de centros; revisar si identifican personas físicas. Excluir contactos innecesarios y no guardar consultas ni datos de estudiantes.

## 7\. Atribución

Fuente: Gobierno de Canarias, Centros educativos de Canarias. [https\://datos.canarias.es/catalogos/general/dataset/centros-educativos-de-canarias](https://datos.canarias.es/catalogos/general/dataset/centros-educativos-de-canarias). Licencia: [https\://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/). Cambios: filtrado de FP, unión por código, selección de campos y transformación a texto. Curso del corpus: conservar CursoEscolar por registro. El portal informa de una actualización del catálogo el 10/11/2026; no atribuir esa fecha automáticamente a la copia local. Proyecto independiente, sin patrocinio oficial. No reutilizar fotografías ni logotipos. Fran ha revisado y confirmado las condiciones de reutilización, según comunicación del equipo del 26/11/2026.

## 8\. Descargas oficiales y huellas locales

- [centros.csv](https://datos.canarias.es/catalogos/general/dataset/f6b15811-014b-46f7-a858-fe48b062ed05/resource/b5e08adf-841b-4ba5-a599-4339e772d792/download/centros.csv) — SHA-256 local: `00c041f31202487fdd47989a8bb140c10013de0eeb9aeca937fd5a6052721156`.

- [ensenanzas-impartidas-por-centro.csv](https://datos.canarias.es/catalogos/general/dataset/f6b15811-014b-46f7-a858-fe48b062ed05/resource/674c46cf-a087-437c-8178-087c3225e483/download/ensenanzas-impartidas-por-centro.csv) — SHA-256 local: `409f547eb31d9d36fbaf7521000beaa0a17874c4db1ead2e9b717995223ae251`.

- [ensenanzas-autorizadas-por-centro.csv](https://datos.canarias.es/catalogos/general/dataset/f6b15811-014b-46f7-a858-fe48b062ed05/resource/72945ca7-176c-42de-b232-8a05d7bd5cba/download/ensenanzas-autorizadas-por-centro.csv) — SHA-256 local: `eb1aa8a70eb498c91ee839a0a3f1622b9ae34cf2dd47bc7378b5871b2f8fa37e`.

- [servicios-complementarios-por-centro.csv](https://datos.canarias.es/catalogos/general/dataset/f6b15811-014b-46f7-a858-fe48b062ed05/resource/2d564c88-73b2-4698-bfba-ba4303cc03d2/download/servicios-complementarios-por-centro.csv) — SHA-256 local: `a85ee42f8b582ae1d5dbddf137ff1ea8d20992164c50444f1e2fe03767985b3c`.

## 9\. Verificación de versiones — 26/11/2026

Comparación directa byte a byte y SHA-256 de los originales con los cuatro CSV recién descargados y aportados por el equipo con sufijo `_actual`. Las cuatro parejas son idénticas.

| Archivo original | Bytes | SHA-256 y contenido |
| :---- | ----: | :---- |
| centros.csv | 1233240 | Coinciden |
| ensenanzas-autorizadas-por-centro.csv | 6671034 | Coinciden |
| ensenanzas-impartidas-por-centro.csv | 3901309 | Coinciden |
| servicios-complementarios-por-centro.csv | 27334 | Coinciden |

No es necesario regenerar la oferta por cambios en estos cuatro archivos. El EDA y el baseline se han actualizado por la incorporación de las fichas informativas. La comprobación acredita la igualdad de las copias aportadas, no la vigencia de la oferta ni una descarga independiente del servidor. Se mantiene pendiente la fecha de descarga original si no está documentada.

## 10\. Ampliación y control de calidad — 26/11/2026

Hemos revisado la última `revision_aprobada.csv`: contiene 419 combinaciones distintas de Estudio, Nivel y Familia, todas marcadas SI (412 ordinarias y 7 adaptadas), con 157 URL principales distintas. No son 419 títulos únicos. Los campos de acceso y salidas están rellenos; esto no acredita por sí solo exactitud semántica. La continuidad falta en los siete itinerarios adaptados: no la inventamos.

| Aspecto | Hallazgo | Acción |
| :---- | :---- | :---- |
| Correspondencias | Se corrigieron las incidencias de Prevención de Riesgos Profesionales y Carpintería y Mueble | Conservar nivel, familia y título; no unir solo por nombre |
| Duplicados | Varias modalidades comparten ficha | Hemos consolidado las fichas conservando el vínculo con la oferta mediante el mapa de correspondencias. |
| Valores imposibles | No hay auditoría exhaustiva de edades, requisitos ni textos | Revisar contradicciones antes de publicar |
| Sesgo y periodos | Oferta local principalmente 2025/26; fichas nacionales consultadas en 2026 | Mostrar curso y fecha; no garantizar plazas actuales |
| FP Adaptada | 7 registros, 6 cualificaciones | Presentar perfiles relacionados, no equivalencias ni garantía de empleo |
| Fuga de datos | Riesgo de ajustar recuperación con el test | Mantener 12 preguntas de desarrollo separadas de las 40 finales |

Fuentes BOE registradas en la revisión aprobada:

- IMP022\_1: [https\://www\.boe.es/eli/es/rd/2009/08/28/1379/dof/spa/pdf](https://www.boe.es/eli/es/rd/2009/08/28/1379/dof/spa/pdf)  
- HOT092\_1: [https\://www\.boe.es/eli/es/rd/2024/09/17/916](https://www.boe.es/eli/es/rd/2024/09/17/916)  
- ADG306\_1: [https\://www\.boe.es/eli/es/rd/2024/09/17/914](https://www.boe.es/eli/es/rd/2024/09/17/914)  
- COM412\_1: [https\://www\.boe.es/diario\_boe/txt.php?id=BOE-A-2011-20367](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2011-20367)  
- AGA164\_1: [https\://www\.boe.es/buscar/doc.php?id=BOE-A-2015-8772](https://www.boe.es/buscar/doc.php?id=BOE-A-2015-8772)  
- ADG305\_1: [https\://www\.boe.es/eli/es/rd/2024/09/17/914](https://www.boe.es/eli/es/rd/2024/09/17/914)

Marco jurídico de los textos normativos: [artículo 13 del TRLPI](https://www.boe.es/buscar/act.php?id=BOE-A-1996-8930#a13). No extendemos esta exclusión a fotografías, logotipos o textos editoriales. La revisión de TodoFP se apoya en el aviso legal registrado previamente; no constituye una nueva consulta en esta actualización. Si no podemos confirmar el permiso de redistribución, consultaremos al docente y no publicaremos los textos afectados.

## 11\. Linaje actualizado y versiones

CSV locales → `01_eda.ipynb` → corpus de oferta (2.751 documentos). En paralelo: `00_recopilacion_todofp.ipynb` → fichas y cobertura → `00b_contraste_todofp.ipynb` → ZIP de contraste → correcciones de correspondencias y normativa → `revision_aprobada.csv` → deduplicación y consolidación → `informacion_fp_oficial.csv` y `corpus_fp_canarias_ampliado.csv` → EDA y baseline TF-IDF.

Hemos consolidado la versión definitiva de los datos en `corpus_definitivo`, que sustituye a la versión anterior de 2.913 documentos. Conservamos 2.751 documentos de oferta y 163 fichas informativas (156 de FP ordinaria y especialización y 7 de FP Adaptada), con un total de 2.914 documentos (+5,93 % respecto al corpus original). El mapa cubre las 419 combinaciones distintas de Estudio, Nivel y Familia; sus identificadores remiten a las 163 fichas. Hay 157 URL principales distintas. Conservamos el curso de la oferta y la fecha de consulta de las fichas por separado.

### Control de calidad de la versión consolidada

| Indicador | Resultado |
| :---- | ----: |
| Documentos de oferta | 2.751 |
| Fichas informativas | 163 |
| Documentos totales | 2.914 |
| Identificadores únicos | 2.914 |
| Documentos sin texto | 0 |
| Combinaciones de oferta cubiertas | 419/419 (100 %) |
| Fichas con acceso informado | 163/163 |
| Fichas con salidas informadas | 163/163 |
| Fichas con continuidad informada | 156/163 |
| Documentos de oferta sin isla | 119/2.751 (4,33 %) |

Hemos comprobado las claves del mapa contra la oferta y los identificadores de las fichas. Los campos rellenos no garantizan la exactitud semántica. En 154 fichas ordinarias sigue constando `revision_humana=PENDIENTE`, aunque la aprobación estructural está registrada; conservamos esta evidencia y no la confundimos con una auditoría humana. Los campos de acceso y salidas no aplican a los documentos de oferta; los campos de centro e isla no aplican a las fichas nacionales.

### Versiones y huellas SHA-256 locales

Hemos recalculado las huellas sobre los bytes de los archivos disponibles y comprobado que las tres huellas de los CSV consolidados coinciden con `control_consolidacion.json`.

| Archivo | Versión / dimensiones | Bytes | SHA-256 local |
| :---- | :---- | ----: | :---- |
| revision\_aprobada.csv | Evidencia: 419 × 41 | 2438848 | `f704f81a6b9992dee8dce6ca26a62aeee0048ade6c4b96c9c35327434f730e32` |
| fp\_adaptada\_validada.csv | Evidencia: 7 × 18 | 6547 | `37588f25dc03fe6315aaeeb744b4b24d054b18ab977a57dd3d30baed5553b6a0` |
| resultados\_contraste (1).zip | Evidencia de contraste | 340928 | `2c7aac3974d62dac3e481cf8d1a5ee1d27649ed6cea386e8f3ce35c692f07b6e` |
| corpus\_fp\_canarias.csv | Oferta original: 2.751 × 12 | 1659297 | `c9b45ac8b5705447df07ce44f1187a7fe35d7e72c482d459bcba05af75cf6fac` |
| informacion\_fp\_oficial.csv | Definitiva: 163 × 46 | 976627 | `5011fdeaff7d3bfe5e23cd7011eab325c6999f9f56fb87062137072ebbef1294` |
| corpus\_fp\_canarias\_ampliado.csv | Definitiva: 2.914 × 24 | 3012712 | `be86c43d3f3604ff07fafebb13acba86a2899f19af6cf1eea4d0099445e9765f` |
| mapa\_ensenanzas\_fichas.csv | Definitiva: 419 × 4 | 70704 | `5374291d9e32f4590fa430e0d2dc2d3beac8bee9533239e9c0cdef6247349595` |
| control\_consolidacion.json | Control de consolidación | 508 | `9b83061616d473c8c7ef7abe432b4558e8bb8b9c85a483d04bce497f37ef1d2a` |

Las huellas identifican versiones locales, no certifican la vigencia de las fuentes ni su licencia. Si modificamos o regeneramos un archivo, recalcularemos su huella. La reproducción completa requiere conservar los CSV, los cuadernos y las decisiones manuales.

## 12\. Partición, privacidad y atribución de la ampliación

No entrenamos un modelo supervisado: indexamos el corpus documental con TF-IDF. Usamos 12 preguntas de desarrollo para ajustar la recuperación y reservamos 40 preguntas finales (20 directas, 8 multidocumento, 8 sin respuesta y 4 adversariales). El baseline actualizado mantiene 11/12 (91,67 %) en desarrollo, según la evaluación registrada en el cuaderno actualizado. No ejecutamos el test final ni ajustamos el modelo con sus preguntas. Hemos comprobado que no hay preguntas literalmente idénticas entre ambos conjuntos; la revisión semántica y la aprobación del equipo y docente siguen pendientes.

No recogemos diagnósticos, discapacidad individual ni datos de menores; los requisitos normativos de FP Adaptada son información general. No solicitaremos datos sensibles para orientar al alumnado. Excluimos contactos personales innecesarios, consultas identificables y fotografías; no subiremos archivos con esos datos al repositorio. Si se detectan datos personales, restringiremos el acceso al equipo y docente y consultaremos la base jurídica antes de tratarlos.

**Atribución para la memoria:** Gobierno de Canarias, Centros educativos de Canarias, oferta principalmente 2025/26, CC BY 4.0; filtrado, unión y transformación por Error404. Ministerio de Educación, Formación Profesional y Deportes, TodoFP, fichas individuales consultadas el 26/11/2026, reproducción textual condicionada al aviso legal, con URL individual y atribución; no CC BY 4.0. Gobierno de Canarias, BOC n.º 46 de 06/03/2025, Resolución de 21/02/2025, y BOE, disposiciones de cualificaciones citadas en apartado 10; resúmenes propios. Proyecto independiente, sin patrocinio oficial.

**Pendiente:** reconfirmación del aviso legal antes de publicación, aprobación del equipo y docente de la versión candidata del test y revisión semántica de solapamientos. La aprobación registrada es estructural y normativa, no una auditoría humana exhaustiva de cada frase.

### Registro de versión candidata del test final — 26/11/2026

Hemos fijado los siguientes archivos sin modificar su contenido. El test queda reservado para la evaluación final y no debe emplearse para ajustar el modelo.

| Archivo | Filas × columnas | Bytes | SHA-256 |
| :---- | ----: | ----: | :---- |
| set\_preguntas.csv | 40 × 5 | 7716 | `f69e310215c3128cc047490b2c3a08d941f0037fbb19b8dd753e94a1e428a403` |
| preguntas\_desarrollo.csv | 12 × 5 | 2795 | `6c51ff8f951c6ed44ecfddb430085a8cd5953fce75fcb86fe18082fc0d3155ee` |

Distribución comprobada: 20 directas, 8 varias fuentes, 8 sin respuesta y 4 de engaño. Los 40 identificadores del test son únicos dentro de su archivo. No hay preguntas literalmente idénticas a las de desarrollo. Los identificadores Pxx son locales a cada conjunto.

**Estado:** versión candidata fijada por hash, pendiente de ratificación por el equipo y aprobación docente. No damos por realizada ninguna aprobación humana. Tras la ratificación, no modificaremos el test; cualquier cambio justificado requerirá una nueva versión, nuevo hash y registro del motivo. Antes de evaluar comprobaremos la huella y registraremos los resultados por separado.