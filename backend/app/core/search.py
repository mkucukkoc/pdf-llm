from typing import List
from .embeddings import dense_search
from .bm25_index import bm25_search
from .rerank import bm25_rerank


def hybrid_search(query: str, top_k: int = 5, filter_doc_ids: List[str] | None = None):
    dense = dense_search(query, top_k=top_k * 4, filter_doc_ids=filter_doc_ids)
    bm25 = bm25_search(query, top_k=top_k * 4, filter_doc_ids=filter_doc_ids)
    merged = {c["id"]: c for c in dense}
    for c in bm25:
        merged.setdefault(c["id"], c)
    candidates = list(merged.values())
    ranked = bm25_rerank(query, candidates, top_k=top_k)
    return ranked
