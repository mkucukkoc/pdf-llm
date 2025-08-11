from fastapi import APIRouter, HTTPException
from ..core.store import get_doc_path
import os, pdfplumber

router = APIRouter(prefix="/tables", tags=["tables"])

@router.get("")
def extract_tables(doc_id: str, pages: str | None = None):
    path = get_doc_path(doc_id)
    if not path or not os.path.exists(path):
        raise HTTPException(404, "doc_id bulunamadı")

    page_nums = None
    if pages:
        page_nums = [int(p.strip()) for p in pages.split(",") if p.strip().isdigit()]

    tables = []
    with pdfplumber.open(path) as pdf:
        total = len(pdf.pages)
        target_pages = page_nums or range(1, total + 1)
        for pno in target_pages:
            if pno < 1 or pno > total:
                continue
            page = pdf.pages[pno - 1]
            extracted = page.extract_tables() or []
            for idx, table in enumerate(extracted):
                csv = "\n".join([",".join(row) for row in table])
                tables.append({
                    "page": pno,
                    "table_id": f"{doc_id}-{pno}-{idx}",
                    "csv": csv,
                })
    return {"doc_id": doc_id, "tables": tables}
