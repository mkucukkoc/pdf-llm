from pydantic import BaseModel
import os

class Settings(BaseModel):
    app_env: str = os.getenv("APP_ENV", "dev")
    data_dir: str = os.getenv("DATA_DIR", "/data")
    upload_dir: str = os.getenv("UPLOAD_DIR", "/data/uploads")
    cache_dir: str = os.getenv("CACHE_DIR", "/data/cache")

    qdrant_url: str = os.getenv("QDRANT_URL", "http://localhost:6333")
    qdrant_collection: str = os.getenv("QDRANT_COLLECTION", "pdf_chunks")

    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")

settings = Settings()

# dizinleri oluştur
os.makedirs(settings.upload_dir, exist_ok=True)
os.makedirs(settings.cache_dir, exist_ok=True)
