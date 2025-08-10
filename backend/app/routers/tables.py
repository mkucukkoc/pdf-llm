from fastapi import APIRouter

router = APIRouter(prefix="/tables", tags=["tables"])

@router.get("")
def extract_tables(doc_id: str, pages: str | None = None):
    # TODO: pdfplumber ile tablo çıkarımı (demo placeholder)
    return {"doc_id": doc_id, "tables": []}
