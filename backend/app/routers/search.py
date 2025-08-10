from fastapi import APIRouter
from ..core.embeddings import dense_search

router = APIRouter(prefix="/search", tags=["search"])

@router.get("")
def search(q: str, top_k: int = 10):
    res = dense_search(q, top_k=top_k)
    return res
