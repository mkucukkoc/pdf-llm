from fastapi import APIRouter, Response
from ..core.layout import page_png

router = APIRouter(prefix="/preview", tags=["preview"])

@router.get("")
def preview(doc_path: str, page: int = 1):
    # Güvenlik için: gerçek sistemde doc_path yerine doc_id -> path map tutun.
    png = page_png(doc_path, page)
    return Response(content=png, media_type="image/png")
