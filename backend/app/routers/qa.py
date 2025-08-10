from fastapi import APIRouter
from ..schemas import QARequest, QAReply
from ..core.embeddings import dense_search
from ..core.rerank import bm25_rerank

router = APIRouter(prefix="/qa", tags=["qa"])

@router.post("", response_model=QAReply)
def qa(req: QARequest):
    candidates = dense_search(req.query, top_k=30, filter_doc_ids=req.doc_ids)
    top = bm25_rerank(req.query, candidates, top_k=req.top_k)

    # Basit cevap: ilk chunklardan derleyelim (demo)
    answer = (
        f"Soru: {req.query}\n\n"
        f"Yanıt (kaynaklı):\n"
        + "\n".join([f"- {c['text'][:180]}... (Kaynak: s.{c['page']}, {c['id']})" for c in top])
    )
    citations = [{"page": c["page"], "chunk_id": c["id"]} for c in top]

    return {"answer": answer, "citations": citations, "confidence": 0.6}
