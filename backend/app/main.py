from fastapi import FastAPI
from .routers import ingest, search, qa, summarize, tables, preview

app = FastAPI(title="PDF-LLM API", version="0.1.0")

app.include_router(ingest.router)
app.include_router(search.router)
app.include_router(qa.router)
app.include_router(summarize.router)
app.include_router(tables.router)
app.include_router(preview.router)

@app.get("/")
def root():
    return {"ok": True, "service": "pdf-llm"}
