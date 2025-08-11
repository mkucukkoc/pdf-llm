from fastapi import APIRouter
from ..core.search import hybrid_search

router = APIRouter(prefix="/search", tags=["search"])

@router.get("")
def search(q: str, top_k: int = 5):
    res = hybrid_search(q, top_k=top_k)
    return res
