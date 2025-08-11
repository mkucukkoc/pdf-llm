from fastapi import APIRouter
from ..schemas import QARequest, QAReply
from ..core.search import hybrid_search

router = APIRouter(prefix="/qa", tags=["qa"])

@router.post("", response_model=QAReply)
def qa(req: QARequest):
    top = hybrid_search(req.query, top_k=req.top_k, filter_doc_ids=req.doc_ids)

    # Basit cevap: ilk chunklardan derleyelim (demo)
    answer = (
        f"Soru: {req.query}\n\n"
        f"Yanıt (kaynaklı):\n"
        + "\n".join([f"- {c['text'][:180]}... (Kaynak: s.{c['page']}, {c['id']})" for c in top])
    )
    citations = [{"page": c["page"], "chunk_id": c["id"]} for c in top]

    return {"answer": answer, "citations": citations, "confidence": 0.6}
