# Resúmenes — Rotación de Infectología

Resúmenes de estudio para la **Rotación por Infectología, Becados de Medicina Interna**,
construidos sobre el *Temario Rotación por Infectología — actualización a junio 2023*
(Programa de Medicina Interna, Pontificia Universidad Católica de Chile).

El formato, la estructura y el nivel de profundidad replican los documentos de referencia
de la carpeta de Infectología (Endocarditis Infecciosa, Infecciones Asociadas a Catéter
Venoso Central, Tuberculosis y VIH).

---

## Cómo está organizado

Un documento por tema del temario, agrupados en las ocho secciones originales.
Cada documento sigue la misma pauta:

1. Título, subtítulo temático y glosario de siglas
2. Nota de alcance y fuentes en que se basa
3. Índice numerado
4. Desarrollo por secciones, con tablas comparativas y figuras (algoritmos) en texto
5. Cajas destacadas: *errores frecuentes*, *lo que más se pregunta*
6. Estudios clínicos clave
7. Perlas de alto rendimiento para la beca
8. Bibliografía esencial

## Categorías del temario

| Categoría | Significado | Profundidad del resumen |
|---|---|---|
| **A** | Diagnosticar y tener conocimiento acabado del tratamiento. Contenido vital para decisiones autónomas del internista. | Documento extenso, con dosis, duraciones y algoritmos de decisión |
| **B** | Diagnosticar, conocer el tratamiento y reconocer el momento de derivar al subespecialista. | Documento intermedio, con foco en diagnóstico, manejo inicial y criterios de derivación |
| **C** | Diagnosticar, conocer el manejo inicial y reconocer la necesidad de derivación. Contenido de profundización. | Documento breve, orientado a generalidades y a entender el manejo del subespecialista |

## Índice general

**85 resúmenes**, distribuidos en las ocho secciones del temario:

| Sección | Documentos |
|---|---|
| [I. Antimicrobianos](resumenes/01-antimicrobianos/README.md) | 11 |
| [II. Microbiología (enfocada a laboratorio)](resumenes/02-microbiologia/README.md) | 9 |
| [III. Infectología hospitalaria](resumenes/03-hospitalaria/README.md) | 23 |
| [IV. Infectología ambulatoria](resumenes/04-ambulatoria/README.md) | 15 |
| [V. Infecciones en inmunocomprometidos](resumenes/05-inmunocomprometidos/README.md) | 8 |
| [VI. Infección por VIH y sus complicaciones](resumenes/06-vih/README.md) | 5 |
| [VII. Otras zoonosis e infecciones en viajeros](resumenes/07-zoonosis-viajeros/README.md) | 9 |
| [VIII. Vacunas](resumenes/08-vacunas/README.md) | 5 |

El índice detallado, tema por tema y con su categoría, está en
[`INDICE.md`](INDICE.md). La pauta de formato común a todos los documentos está en
[`plantilla/PLANTILLA.md`](plantilla/PLANTILLA.md).

## Versión en PDF

La carpeta [`pdf/`](pdf/) contiene **los 95 documentos en PDF**, con la misma
organización en ocho subcarpetas por sección. Están pensados para leer en el
teléfono durante un turno, imprimir o subir a Drive.

### Cómo subirlos a Google Drive

1. En GitHub, entrar a la rama `claude/infectologia-temario-resumen-amw0jr` y usar
   **Code → Download ZIP**.
2. Descomprimir y abrir la carpeta `pdf/`.
3. Seleccionar todo su contenido —las ocho subcarpetas y los dos índices— y
   arrastrarlo a la carpeta de Drive
   [Resúmenes Infectología — Temario 2023](https://drive.google.com/drive/folders/1hAKmbos4a-NhMezOoGc9NaDwB3WrW8cz),
   que está vacía y lista para recibirlos.

> **Por qué vacía.** Drive no fusiona carpetas del mismo nombre: crea una segunda.
> Por eso la carpeta se dejó sin contenido, para que al arrastrar quede la
> estructura exacta y sin duplicados.

### Regenerar los PDF

Si se edita o agrega un resumen, los PDF se reconstruyen con:

```bash
pip install reportlab pikepdf
python3 herramientas/generar_pdf.py
```

El detalle del conversor está en [`herramientas/`](herramientas/README.md).

## Temas que ya tienen documento en la carpeta de Drive

Cuatro temas del temario ya están cubiertos por los documentos de referencia y **no se
duplican** aquí; los resúmenes de este repositorio los citan como material base:

| Tema del temario | Sección | Documento existente |
|---|---|---|
| Endocarditis infecciosa (III-B) | Hospitalaria | *Endocarditis Infecciosa* |
| Infección asociada a catéter venoso central (III-A) | Hospitalaria | *Infecciones Asociadas a Catéter Venoso Central* |
| Tuberculosis pulmonar (III-B) | Hospitalaria | *Tuberculosis* |
| Infección por VIH — diagnóstico y generalidades (VI-A/B) | VIH | *VIH* |

## Advertencia de uso

Material de estudio, no un protocolo institucional. Las dosis corresponden a adultos con
función renal normal salvo que se indique lo contrario, y **siempre deben contrastarse con
el formulario y los protocolos locales de la Red de Salud UC CHRISTUS** y con la
susceptibilidad local antes de aplicarlas a un paciente.

Las recomendaciones se basan en guías vigentes y se cita la fuente en cada documento.
Cuando un punto es controvertido o la evidencia es de baja calidad, se señala
explícitamente. Cuando una normativa nacional puede haber sido actualizada después del
cierre de este material, se indica que debe verificarse la versión vigente en MINSAL o ISP.
