import os, json
from typing import List, Dict
from rank_bm25 import BM25Okapi
from .settings import settings

INDEX_FILE = settings.bm25_index_path


def add_chunks(chunks: List[Dict]):
    """Persist chunks for BM25 search"""
    os.makedirs(os.path.dirname(INDEX_FILE), exist_ok=True)
    with open(INDEX_FILE, "a", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")


def _load_corpus(filter_doc_ids: List[str] | None = None):
    texts, metas = [], []
    if not os.path.exists(INDEX_FILE):
        return texts, metas
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        for line in f:
            try:
                obj = json.loads(line)
            except Exception:
                continue
            if filter_doc_ids and obj.get("doc_id") not in filter_doc_ids:
                continue
            texts.append(obj.get("text", "").split())
            metas.append(obj)
    return texts, metas


def bm25_search(query: str, top_k: int = 20, filter_doc_ids: List[str] | None = None):
    texts, metas = _load_corpus(filter_doc_ids)
    if not texts:
        return []
    bm25 = BM25Okapi(texts)
    scores = bm25.get_scores(query.split())
    results = []
    for meta, score in zip(metas, scores):
        r = meta.copy()
        r["score"] = float(score)
        results.append(r)
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_k]
