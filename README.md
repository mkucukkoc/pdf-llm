# PDF‑LLM (Minimal İskelet)

FastAPI + Qdrant + Celery ile PDF üstünde RAG tabanlı arama/QA/özet için minimal iskelet.

## Hızlı Başlangıç

1. `.env.example` → `.env` kopyalayın ve gerekiyorsa düzenleyin.

2. Docker ile ayağa kaldırın:

```bash
docker compose build
docker compose up
```

3. API dokümanı: http://localhost:8000/docs

### Örnek Akış
- `POST /ingest` ile PDF yükleyin (gerekirse `ocr=true`).
- `GET /search?q=...` ile arama yapın.
- `POST /qa` ile kaynaklı cevap alın.
- `POST /summarize` ile (demo) özetleyin.
- `GET /preview?doc_path=...&page=1` ile sayfa PNG görün.

## Notlar
- Bu repo **demo iskelet**tir. Güvenlik (doc_id→path mapping), gerçek reranker, tablo çıkarımı ve LLM çağrıları sadeleştirilmiştir.
- Üretimde: bge‑reranker‑large, gelişmiş layout (bbox), tablo çıkarımı (pdfplumber), doc_id bazlı depolama ve kimlik doğrulama ekleyin.
