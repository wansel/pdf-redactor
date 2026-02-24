import fitz  # PyMuPDF
# import pymupdf
# import PyMuPDF

# Abrir o PDF
doc = fitz.open("exemplo.pdf")
# doc = pymupdf.open("328585-aula-00.pdf")

# Iterar por cada página
for page in doc:
    texto = ""
    areas = page.search_for(texto)
    for area in areas:
        page.add_redact_annot(area, fill=(1, 1, 1))  # branco
    page.apply_redactions()

# Salvar o novo PDF
doc.save("out/exemplo.pdf")
