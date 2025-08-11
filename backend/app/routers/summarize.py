from fastapi import APIRouter
from ..schemas import SummarizeReq
from ..core.summarizer import summarize_document

router = APIRouter(prefix="/summarize", tags=["summarize"])

@router.post("")
def summarize(req: SummarizeReq):
    data = summarize_document(req.doc_id)
    return {"doc_id": req.doc_id, "level": req.level, **data}
