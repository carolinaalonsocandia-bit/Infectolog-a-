#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenera la carpeta pdf/ a partir de los resúmenes en Markdown.

Uso, desde la raíz del repositorio:

    pip install reportlab pikepdf
    python3 herramientas/generar_pdf.py

Produce un PDF por documento, agrupados en subcarpetas por sección, listos
para subirse a Drive o imprimirse. Las fuentes no se incrustan (se usan las
estándar de PDF), por lo que los archivos pesan ~16 KB cada uno.
"""
import os, re, glob, sys, traceback

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from md2pdf import build

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "pdf")

SECS = [("01-antimicrobianos",       "I. Antimicrobianos"),
        ("02-microbiologia",         "II. Microbiologia"),
        ("03-hospitalaria",          "III. Infectologia hospitalaria"),
        ("04-ambulatoria",           "IV. Infectologia ambulatoria"),
        ("05-inmunocomprometidos",   "V. Inmunocomprometidos"),
        ("06-vih",                   "VI. VIH y complicaciones"),
        ("07-zoonosis-viajeros",     "VII. Zoonosis e infecciones en viajeros"),
        ("08-vacunas",               "VIII. Vacunas")]


def safe(name):
    """Nombre de archivo válido en Windows, macOS y Linux."""
    name = re.sub(r'[\\/:*?"<>|]', '-', name)
    return re.sub(r'\s+', ' ', name).strip()[:120]


def compress(path):
    """Reduce ~25 % el peso con pikepdf. Opcional: si no está, no pasa nada."""
    try:
        import pikepdf
    except ImportError:
        return
    pdf = pikepdf.open(path)
    pdf.save(path + ".tmp",
             object_stream_mode=pikepdf.ObjectStreamMode.generate,
             compress_streams=True, recompress_flate=True,
             stream_decode_level=pikepdf.StreamDecodeLevel.generalized)
    pdf.close()
    os.replace(path + ".tmp", path)


def do(md, outdir, fname, errors):
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, fname + ".pdf")
    try:
        build(md, path)
        compress(path)
        return os.path.getsize(path)
    except Exception as e:
        errors.append((md, repr(e), traceback.format_exc()[-500:]))
        return 0


def main():
    errors, sizes = [], []
    sizes.append(do(f"{ROOT}/INDICE.md", OUT, "00 - Indice general de resumenes", errors))
    sizes.append(do(f"{ROOT}/README.md", OUT, "00 - Como usar estos resumenes", errors))

    for d, label in SECS:
        outdir = os.path.join(OUT, safe(label))
        rm = f"{ROOT}/resumenes/{d}/README.md"
        if os.path.exists(rm):
            sizes.append(do(rm, outdir, "00 - Indice de la seccion", errors))
        for f in sorted(glob.glob(f"{ROOT}/resumenes/{d}/*.md")):
            if f.endswith("README.md"):
                continue
            titulo = open(f, encoding="utf-8").read().split("\n", 1)[0].lstrip("# ").strip()
            num = os.path.basename(f)[:2]
            sizes.append(do(f, outdir, safe(f"{num} - {titulo}"), errors))

    ok = [s for s in sizes if s]
    print("PDF generados: %d   errores: %d" % (len(ok), len(errors)))
    print("Total: %.2f MB   promedio: %.0f KB" % (sum(ok) / 1048576, sum(ok) / len(ok) / 1024))
    for e in errors:
        print("\nERROR en", e[0], "\n", e[1], "\n", e[2])
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
