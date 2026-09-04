# Herramientas

Scripts para regenerar la carpeta [`pdf/`](../pdf/) a partir de los resúmenes en
Markdown. No son material de estudio: solo sirven para reconstruir los PDF si se
edita o se agrega un resumen.

| Archivo | Función |
|---|---|
| `md2pdf.py` | Conversor de Markdown a PDF (ReportLab). Maneja títulos, tablas, listas, citas destacadas y los algoritmos en texto, conservando su alineación. |
| `generar_pdf.py` | Recorre `resumenes/`, genera un PDF por documento y los agrupa en subcarpetas por sección. |

## Uso

Desde la raíz del repositorio:

```bash
pip install reportlab pikepdf
python3 herramientas/generar_pdf.py
```

## Notas de diseño

- **No se incrustan fuentes**: se usan las catorce fuentes estándar de PDF
  (Times, Helvetica, Courier), que todo lector reconoce. Por eso cada documento
  pesa unos 16 KB en lugar de 300 KB.
- Como esas fuentes solo cubren el juego de caracteres WinAnsi, `md2pdf.py`
  sustituye los caracteres que no existen en él: `≥` pasa a `>=`, `→` a `->`,
  `PaO₂` a `PaO2`, `β` a `beta`, y los caracteres de dibujo de los algoritmos a
  `-`, `|` y `+`. La sustitución está en el diccionario `SUBST`.
- El énfasis (negrita e itálica) se procesa con una pila de delimitadores, para
  que las nemotecnias del tipo `***S**erratia*` se rendericen correctamente.
- `pikepdf` es opcional: si está instalado, reduce el peso alrededor de un 25 %.
