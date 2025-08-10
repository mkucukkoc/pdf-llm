# Basit BM25 + dense skor harmanı (demo). Gelişmiş: bge-reranker-large.
from rank_bm25 import BM25Okapi


def bm25_rerank(query: str, candidates: list[dict], top_k: int = 5):
    corpus = [c["text"].split() for c in candidates]
    bm25 = BM25Okapi(corpus)
    scores = bm25.get_scores(query.split())
    for c, s in zip(candidates, scores):
        c["bm25"] = float(s)
        c["final_score"] = 0.5 * c.get("score", 0) + 0.5 * c["bm25"]  # dense(0..1?) + bm25
    ranked = sorted(candidates, key=lambda x: x["final_score"], reverse=True)
    return ranked[:top_k]
