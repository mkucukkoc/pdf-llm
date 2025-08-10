from pydantic import BaseModel
from typing import List, Optional

class IngestResponse(BaseModel):
    doc_id: str
    pages: int

class QARequest(BaseModel):
    query: str
    doc_ids: Optional[List[str]] = None
    top_k: int = 5

class QAReply(BaseModel):
    answer: str
    citations: list
    confidence: float

class SummarizeReq(BaseModel):
    doc_id: str
    level: str = "global"
