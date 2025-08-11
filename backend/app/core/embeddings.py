from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient, models
from .settings import settings
from .bm25_index import add_chunks
import numpy as np

_embedder = None
_qdrant = None

def get_embedder():
    global _embedder
    if _embedder is None:
        _embedder = SentenceTransformer("thenlper/gte-large")
    return _embedder


def get_qdrant():
    global _qdrant
    if _qdrant is None:
        _qdrant = QdrantClient(url=settings.qdrant_url)
        try:
            _qdrant.get_collection(settings.qdrant_collection)
        except Exception:
            _qdrant.recreate_collection(
                collection_name=settings.qdrant_collection,
                vectors_config=models.VectorParams(size=1024, distance=models.Distance.COSINE)
            )
    return _qdrant


def embed_texts(texts: list[str]) -> np.ndarray:
    model = get_embedder()
    return model.encode(texts, normalize_embeddings=True)


def upsert_chunks(chunks: list[dict]):
    qdr = get_qdrant()
    vectors = embed_texts([c["text"] for c in chunks])
    points = []
    for v, c in zip(vectors, chunks):
        points.append(models.PointStruct(
            id=c["id"],
            vector=v.tolist(),
            payload=c
        ))
    qdr.upsert(collection_name=settings.qdrant_collection, points=points)
    add_chunks(chunks)


def dense_search(query: str, top_k: int = 20, filter_doc_ids: list[str] | None = None):
    qdr = get_qdrant()
    qvec = embed_texts([query])[0]
    flt = None
    if filter_doc_ids:
        flt = models.Filter(must=[models.FieldCondition(key="doc_id", match=models.MatchAny(any=filter_doc_ids))])
    result = qdr.search(collection_name=settings.qdrant_collection, query_vector=qvec.tolist(), limit=top_k, query_filter=flt)
    return [r.payload | {"score": r.score} for r in result]
