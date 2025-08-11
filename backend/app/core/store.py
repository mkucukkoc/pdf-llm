import os, shutil, uuid, json
from .settings import settings

UPLOAD_DIR = settings.upload_dir

DOCSTORE = settings.docstore_path


def save_upload(file_bytes: bytes, filename: str) -> str:
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    base = f"{uuid.uuid4().hex}_{filename}"
    path = os.path.join(UPLOAD_DIR, base)
    with open(path, "wb") as f:
        f.write(file_bytes)
    return path


def register_doc(doc_id: str, path: str):
    with open(DOCSTORE, "a", encoding="utf-8") as f:
        f.write(json.dumps({"doc_id": doc_id, "path": path}) + "\n")


def get_doc_path(doc_id: str) -> str | None:
    if not os.path.exists(DOCSTORE):
        return None
    with open(DOCSTORE, "r", encoding="utf-8") as f:
        for line in f:
            try:
                rec = json.loads(line)
            except Exception:
                continue
            if rec.get("doc_id") == doc_id:
                return rec.get("path")
    return None
