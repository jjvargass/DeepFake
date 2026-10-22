#!/usr/bin/env python3
"""Convierte .docx a Markdown extrayendo las imágenes."""
import sys
import zipfile
from pathlib import Path

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.oxml.ns import qn

NS_A = "http://schemas.openxmlformats.org/drawingml/2006/main"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


def iter_blocks(parent):
    body = parent.element.body
    for child in body.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, parent)
        elif child.tag == qn("w:tbl"):
            yield Table(child, parent)


def run_text(run):
    text = ""
    for node in run._element.iter():
        if node.tag == qn("w:t"):
            text += node.text or ""
        elif node.tag in (qn("w:br"), qn("w:cr")):
            text += "\n"
    return text


def fmt_run(run, text):
    if not text:
        return ""
    if run.bold and run.italic:
        return f"***{text}***"
    if run.bold:
        return f"**{text}**"
    if run.italic:
        return f"*{text}*"
    return text


def para_markdown(para):
    parts = []
    # recorrer runs e hipervínculos en orden
    from docx.text.run import Run
    for child in para._element.iterchildren():
        if child.tag == qn("w:r"):
            r = Run(child, para)
            parts.append(fmt_run(r, run_text(r)))
        elif child.tag == qn("w:hyperlink"):
            text = "".join(t.text or "" for t in child.iter(qn("w:t")))
            rid = child.get(qn("r:id"))
            url = para.part.rels[rid].target_ref if rid else None
            if url:
                parts.append(f"[{text}]({url})")
            else:
                parts.append(text)
    text = "".join(parts)
    return text.strip("\n").strip()


def para_images(para, img_counter, out_dir):
    """Devuelve lista de nombres de imagen en este párrafo, en orden."""
    images = []
    for blip in para._element.iter(f"{{{NS_A}}}blip"):
        rid = blip.get(f"{{{NS_R}}}embed")
        if not rid:
            continue
        part = para.part.related_parts[rid]
        ext = Path(part.partname).suffix or ".png"
        img_counter[0] += 1
        name = f"imagen-{img_counter[0]:02d}{ext}"
        (out_dir / name).write_bytes(part.blob)
        images.append(name)
    return images


def table_markdown(table):
    rows = []
    for row in table.rows:
        cells = []
        for cell in row.cells:
            txt = "\n".join(para_markdown(p) for p in cell.paragraphs).strip()
            cells.append(txt.replace("|", "\\|"))
        rows.append(cells)
    if not rows:
        return ""
    if len(rows) == 1 and len(rows[0]) == 1:
        return "```bash\n" + rows[0][0] + "\n```"
    md = ["| " + " | ".join(rows[0]) + " |",
          "|" + " --- |" * len(rows[0])]
    for r in rows[1:]:
        md.append("| " + " | ".join(r) + " |")
    return "\n".join(md)


def convert(docx_path, md_path):
    docx_path = Path(docx_path)
    md_path = Path(md_path)
    short = {"Instalacion_Miniconda": "miniconda-img",
             "Entornos_Virtuales_con_Python_-_Conda": "env-img",
             "01-Face-swap_Intercambio_de_rostro": "face-swap-img"}
    out_dir = Path(short.get(md_path.stem, md_path.stem + "-img"))
    out_dir.mkdir(exist_ok=True)

    doc = Document(docx_path)
    img_counter = [0]
    lines = []
    in_code = False

    for block in iter_blocks(doc):
        if isinstance(block, Table):
            lines.append("")
            lines.append(table_markdown(block))
            lines.append("")
            continue

        para = block
        style = (para.style.name or "").lower()

        for name in para_images(para, img_counter, out_dir):
            lines.append(f"![{name}]({out_dir}/{name})")
            lines.append("")

        text = para_markdown(para)
        if not text:
            continue

        if style.startswith("heading"):
            try:
                level = int(style.split()[-1])
            except ValueError:
                level = 1
            lines.append("#" * min(level, 6) + " " + text)
        elif "title" in style:
            lines.append("# " + text)
        elif "list bullet" in style:
            lines.append(f"- {text}")
        elif "list number" in style:
            lines.append(f"1. {text}")
        else:
            lines.append(text)
        lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"OK: {md_path} ({img_counter[0]} imágenes)")


if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])
