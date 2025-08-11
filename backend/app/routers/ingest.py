from fastapi import APIRouter, UploadFile, File, HTTPException
from ..core.store import save_upload, register_doc
from ..core.ocr import run_ocr
from ..core.layout import extract_pages
from ..core.chunking import make_chunks
from ..core.embeddings import upsert_chunks
import os, uuid

router = APIRouter(prefix="/ingest", tags=["ingest"])

@router.post("")
async def ingest(pdf: UploadFile = File(...), ocr: bool = True):
    if not pdf.filename.lower().endswith(".pdf"):
        raise HTTPException(400, "PDF bekleniyor")

    path = save_upload(await pdf.read(), pdf.filename)
    doc_id = uuid.uuid4().hex

    if ocr:
        try:
            path = run_ocr(path)
        except Exception:
            pass  # taranmış değilse sorun çıkmadan devam et

    register_doc(doc_id, path)
    pages = extract_pages(path)
    chunks = make_chunks(doc_id, pages)
    upsert_chunks(chunks)

    return {"doc_id": doc_id, "pages": len(pages), "chunks": len(chunks)}
