import fitz  # PyMuPDF
from typing import List, Dict

# Basit sayfa metni çıkarımı (demo). Gelişmişi: blok/bbox ile döndür.

def extract_pages(pdf_path: str) -> List[Dict]:
    doc = fitz.open(pdf_path)
    pages = []
    for i, p in enumerate(doc):
        text = p.get_text("text")
        pages.append({
            "page_num": i + 1,
            "text": text,
            "blocks": [],
            "images": []
        })
    return pages


def page_png(pdf_path: str, page: int, dpi: int = 150) -> bytes:
    doc = fitz.open(pdf_path)
    pix = doc[page - 1].get_pixmap(dpi=dpi)
    return pix.tobytes("png")
