from fastapi import APIRouter
from ..schemas import SummarizeReq

router = APIRouter(prefix="/summarize", tags=["summarize"])

@router.post("")
def summarize(req: SummarizeReq):
    # Demo: gerçek LLM çağrısı yerine iskelet
    return {
        "doc_id": req.doc_id,
        "level": req.level,
        "summary": "(demo) Bölüm özetleri + global özet burada üretilecek."
    }
