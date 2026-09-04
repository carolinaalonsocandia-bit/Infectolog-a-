# -*- coding: utf-8 -*-
"""Markdown -> PDF (ReportLab, fuentes base-14 sin incrustar)."""
import re, os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, Preformatted,
                                KeepTogether, HRFlowable)

NAVY   = colors.HexColor('#1F4E79')
INK    = colors.HexColor('#16181D')
GREY   = colors.HexColor('#5A6470')
RULE   = colors.HexColor('#C3CCD6')
BQBG   = colors.HexColor('#F2F6FA')
ROWBG  = colors.HexColor('#F4F7FA')

SUBST = {
    '─':'-', '│':'|', '┌':'+', '┐':'+', '└':'+', '┘':'+',
    '├':'+', '┤':'+', '┬':'+', '┴':'+', '┼':'+',
    '≥':'>=', '≤':'<=', '≠':'!=', '≈':'~', '−':'-',
    '→':'->', '↔':'<->', '↑':'(sube)', '↓':'(baja)',
    '₂':'2', '₄':'4', '⁴':'4', '⁵':'5', '⁶':'6',
    'β':'beta', 'α':'alfa', 'č':'c',
}
_SUB_RE = re.compile('|'.join(map(re.escape, SUBST)))
def deuni(t):
    return _SUB_RE.sub(lambda m: SUBST[m.group()], t)

def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def _wellformed(t):
    """verifica que <b>/<i> queden correctamente anidados"""
    stack = []
    for m in re.finditer(r'</?([bi])>', t):
        tag = m.group(1)
        if m.group(0).startswith('</'):
            if not stack or stack.pop() != tag:
                return False
        else:
            stack.append(tag)
    return not stack

def _emph(t):
    """Énfasis markdown con pila de delimitadores.

    Maneja correctamente el anidamiento, incluidos los casos de nemotecnia
    (***S**erratia*) y los cierres triples (**... *X***).
    """
    n = len(t); i = 0
    parts = []      # fragmentos de salida
    stack = []      # marcas abiertas: {'count': asteriscos, 'idx': posición en parts}
    while i < n:
        if t[i] != '*':
            j = i
            while j < n and t[j] != '*': j += 1
            parts.append(t[i:j]); i = j; continue
        j = i
        while j < n and t[j] == '*': j += 1
        run = j - i
        prev = t[i-1] if i > 0 else ' '
        nxt  = t[j] if j < n else ' '
        can_open  = not nxt.isspace()
        can_close = not prev.isspace()
        while run > 0 and can_close and stack:
            top = stack[-1]
            take = 2 if (run >= 2 and top['count'] >= 2) else 1
            parts.append('</b>' if take == 2 else '</i>')
            parts[top['idx']] = ('<b>' if take == 2 else '<i>') + parts[top['idx']]
            top['count'] -= take; run -= take
            if top['count'] == 0: stack.pop()
        if run > 0 and can_open:
            parts.append('')
            stack.append({'count': run, 'idx': len(parts) - 1})
            run = 0
        if run > 0:
            parts.append('*' * run)
        i = j
    for sm in stack:                      # aperturas sin cierre -> asteriscos literales
        parts[sm['idx']] = '*' * sm['count'] + parts[sm['idx']]
    return ''.join(parts)

def inline(t):
    """markdown en línea -> mini-markup de ReportLab"""
    t = deuni(t)
    t = esc(t)
    t = re.sub(r'`([^`]+)`', r'<font face="Courier" size="8.5">\1</font>', t)
    t = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', t)          # enlaces -> solo texto
    out = _emph(t)
    if not _wellformed(out):
        out = re.sub(r'\*+', '', t)      # repliegue seguro
    return out

# ---------------------------------------------------------------- estilos
S = {}
S['body']  = ParagraphStyle('body', fontName='Times-Roman', fontSize=9.6, leading=13,
                            alignment=TA_JUSTIFY, textColor=INK, spaceAfter=4)
S['h1']    = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=17, leading=20.5,
                            textColor=colors.HexColor('#0F1115'), spaceAfter=3)
S['sub']   = ParagraphStyle('sub', fontName='Helvetica-Bold', fontSize=10, leading=13.5,
                            textColor=NAVY, spaceBefore=4, spaceAfter=5, alignment=TA_LEFT)
S['byline']= ParagraphStyle('byline', fontName='Times-Italic', fontSize=8.4, leading=11,
                            textColor=GREY, spaceAfter=3, alignment=TA_LEFT)
S['h2']    = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=11.8, leading=14.5,
                            textColor=NAVY, spaceBefore=13, spaceAfter=4)
S['h3']    = ParagraphStyle('h3', fontName='Helvetica-Bold', fontSize=10, leading=13,
                            textColor=colors.HexColor('#2C3E50'), spaceBefore=9, spaceAfter=3)
S['li']    = ParagraphStyle('li', parent=S['body'], spaceAfter=2.5)
S['bq']    = ParagraphStyle('bq', fontName='Times-Roman', fontSize=9.2, leading=12.4,
                            textColor=INK, alignment=TA_LEFT, spaceAfter=3)
S['th']    = ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=8.1, leading=10,
                            textColor=colors.white, alignment=TA_LEFT)
S['td']    = ParagraphStyle('td', fontName='Times-Roman', fontSize=8.3, leading=10.4,
                            textColor=INK, alignment=TA_LEFT)
S['foot']  = ParagraphStyle('foot', fontName='Times-Italic', fontSize=8, leading=10.5,
                            textColor=GREY, spaceBefore=8, alignment=TA_LEFT)

FRAME_W = A4[0] - 32*mm

# ---------------------------------------------------------------- parser
def parse(md, story):
    lines = md.split('\n')
    i, n = 0, len(lines)
    seen_h1 = False; seen_sub = False
    while i < n:
        ln = lines[i]

        # bloque de código / algoritmo
        if ln.startswith('```'):
            i += 1; buf = []
            while i < n and not lines[i].startswith('```'):
                buf.append(deuni(lines[i].rstrip())); i += 1
            i += 1
            mx = max((len(x) for x in buf), default=1)
            fs = min(7.8, (FRAME_W - 14) / (mx * 0.6)) if mx else 7.8
            fs = max(4.6, fs)
            cs = ParagraphStyle('code', fontName='Courier', fontSize=fs, leading=fs*1.32,
                                textColor=INK)
            pre = Preformatted('\n'.join(buf), cs)
            box = Table([[pre]], colWidths=[FRAME_W])
            box.setStyle(TableStyle([
                ('BACKGROUND',(0,0),(-1,-1), colors.HexColor('#F6F7F9')),
                ('BOX',(0,0),(-1,-1), 0.6, colors.HexColor('#D5DBE2')),
                ('LEFTPADDING',(0,0),(-1,-1),7), ('RIGHTPADDING',(0,0),(-1,-1),7),
                ('TOPPADDING',(0,0),(-1,-1),6), ('BOTTOMPADDING',(0,0),(-1,-1),6),
            ]))
            story += [Spacer(1,5), box, Spacer(1,6)]
            continue

        # tabla
        if ln.lstrip().startswith('|') and i+1 < n and re.match(r'^\s*\|[\s:\-\|]+\|\s*$', lines[i+1]):
            def cells(r):
                r = r.strip()
                if r.startswith('|'): r = r[1:]
                if r.endswith('|'): r = r[:-1]
                return [c.strip() for c in r.split('|')]
            hdr = cells(ln); i += 2
            rows = []
            while i < n and lines[i].lstrip().startswith('|'):
                rows.append(cells(lines[i])); i += 1
            ncol = len(hdr)
            rows = [(r + ['']*ncol)[:ncol] for r in rows]
            # anchos proporcionales al contenido, con mínimo
            raw = [max([len(hdr[c])] + [len(r[c]) for r in rows] or [1]) for c in range(ncol)]
            raw = [max(3, min(x, 60)) for x in raw]
            tot = sum(raw)
            widths = [FRAME_W * x / tot for x in raw]
            mn = FRAME_W * 0.07
            widths = [max(w, mn) for w in widths]
            f = FRAME_W / sum(widths); widths = [w*f for w in widths]
            data = [[Paragraph(inline(c), S['th']) for c in hdr]] + \
                   [[Paragraph(inline(c), S['td']) for c in r] for r in rows]
            t = Table(data, colWidths=widths, repeatRows=1)
            st = [('BACKGROUND',(0,0),(-1,0), NAVY),
                  ('GRID',(0,0),(-1,-1), 0.45, RULE),
                  ('LINEBELOW',(0,0),(-1,0), 0.8, NAVY),
                  ('VALIGN',(0,0),(-1,-1),'TOP'),
                  ('LEFTPADDING',(0,0),(-1,-1),4.5), ('RIGHTPADDING',(0,0),(-1,-1),4.5),
                  ('TOPPADDING',(0,0),(-1,-1),3.2), ('BOTTOMPADDING',(0,0),(-1,-1),3.2)]
            for r in range(2, len(data), 2):
                st.append(('BACKGROUND',(0,r),(-1,r), ROWBG))
            t.setStyle(TableStyle(st))
            story += [Spacer(1,5), t, Spacer(1,7)]
            continue

        # cita / callout
        if ln.lstrip().startswith('>'):
            buf = []
            while i < n and lines[i].lstrip().startswith('>'):
                buf.append(re.sub(r'^\s*>\s?', '', lines[i])); i += 1
            paras, cur = [], []
            for b in buf:
                if b.strip() == '':
                    if cur: paras.append(' '.join(cur)); cur = []
                else: cur.append(b.strip())
            if cur: paras.append(' '.join(cur))
            inner = [Paragraph(inline(p), S['bq']) for p in paras]
            box = Table([[inner]], colWidths=[FRAME_W])
            box.setStyle(TableStyle([
                ('BACKGROUND',(0,0),(-1,-1), BQBG),
                ('LINEBEFORE',(0,0),(0,-1), 2.6, NAVY),
                ('LEFTPADDING',(0,0),(-1,-1),9), ('RIGHTPADDING',(0,0),(-1,-1),8),
                ('TOPPADDING',(0,0),(-1,-1),6), ('BOTTOMPADDING',(0,0),(-1,-1),5),
            ]))
            story += [Spacer(1,4), KeepTogether(box), Spacer(1,6)]
            continue

        # regla horizontal
        if re.match(r'^\s*---+\s*$', ln):
            story += [Spacer(1,4), HRFlowable(width='100%', thickness=0.6, color=RULE,
                                              spaceBefore=1, spaceAfter=5)]
            i += 1; continue

        # encabezados
        m = re.match(r'^(#{1,4})\s+(.*)$', ln)
        if m:
            lvl, txt = len(m.group(1)), m.group(2).strip()
            if lvl == 1 and not seen_h1:
                seen_h1 = True
                story += [Paragraph(inline(txt), S['h1']),
                          HRFlowable(width='100%', thickness=2, color=NAVY,
                                     spaceBefore=2, spaceAfter=7)]
            else:
                story.append(Paragraph(inline(txt), S['h2' if lvl == 2 else 'h3']))
            i += 1; continue

        # listas
        m = re.match(r'^(\s*)([-*]|\d+\.)\s+(.*)$', ln)
        if m:
            items = []
            while i < n:
                m2 = re.match(r'^(\s*)([-*]|\d+\.)\s+(.*)$', lines[i])
                if not m2: break
                ind = len(m2.group(1)); mark = m2.group(2); body = [m2.group(3)]
                i += 1
                while i < n and lines[i].strip() and lines[i].startswith(' ') \
                      and not re.match(r'^(\s*)([-*]|\d+\.)\s+', lines[i]) \
                      and not lines[i].lstrip().startswith(('#','|','>','```')):
                    body.append(lines[i].strip()); i += 1
                bullet = mark if re.match(r'\d+\.', mark) else '\u2022'
                st = ParagraphStyle('l%d' % ind, parent=S['li'],
                                    leftIndent=12 + ind*8, bulletIndent=2 + ind*8)
                items.append(Paragraph(inline(' '.join(body)), st,
                                       bulletText=deuni(bullet)))
            story += items + [Spacer(1,3)]
            continue

        if ln.strip() == '':
            i += 1; continue

        # párrafo
        buf = [ln.strip()]; i += 1
        while i < n and lines[i].strip() and not re.match(r'^(\s*)([-*]|\d+\.)\s+', lines[i]) \
              and not lines[i].lstrip().startswith(('#','|','>','```')) \
              and not re.match(r'^\s*---+\s*$', lines[i]):
            buf.append(lines[i].strip()); i += 1
        txt = ' '.join(buf)
        # subtítulo temático (primer párrafo en negrita tras el H1)
        if seen_h1 and not seen_sub and txt.startswith('**') and txt.endswith('**'):
            seen_sub = True
            story.append(Paragraph(inline(txt[2:-2]), S['sub'])); continue
        # línea de autoría / nota de cierre en cursiva
        if txt.startswith('*') and txt.endswith('*') and not txt.startswith('**'):
            plain = txt.strip('*')
            sty = S['foot'] if plain.startswith('Documento de estudio') else S['byline']
            story.append(Paragraph(inline(plain), sty)); continue
        story.append(Paragraph(inline(txt), S['body']))
    return story

# ---------------------------------------------------------------- documento
def build(md_path, pdf_path):
    md = open(md_path, encoding='utf-8').read()
    first = md.split('\n', 1)[0]
    title = deuni(first.lstrip('# ').strip()) if first.startswith('#') else os.path.basename(md_path)

    def footer(canv, doc):
        canv.saveState()
        canv.setFont('Times-Roman', 8)
        canv.setFillColor(GREY)
        canv.drawCentredString(A4[0]/2, 11*mm, str(canv.getPageNumber()))
        canv.setStrokeColor(RULE); canv.setLineWidth(0.4)
        canv.line(16*mm, 15.5*mm, A4[0]-16*mm, 15.5*mm)
        canv.setFont('Times-Italic', 7.2)
        canv.drawString(16*mm, 11*mm, 'Rotación de Infectología · Medicina Interna')
        canv.drawRightString(A4[0]-16*mm, 11*mm, title[:62])
        canv.restoreState()

    doc = BaseDocTemplate(pdf_path, pagesize=A4,
                          leftMargin=16*mm, rightMargin=16*mm,
                          topMargin=16*mm, bottomMargin=20*mm,
                          title=title, author='Rotación de Infectología',
                          subject='Temario Rotación por Infectología 2023')
    frame = Frame(16*mm, 20*mm, FRAME_W, A4[1]-36*mm, id='f',
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id='p', frames=[frame], onPage=footer)])
    story = []
    parse(md, story)
    doc.build(story)
    return title

if __name__ == '__main__':
    print(build(sys.argv[1], sys.argv[2]))
