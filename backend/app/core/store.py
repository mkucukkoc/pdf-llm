import os, shutil, uuid
from .settings import settings

UPLOAD_DIR = settings.upload_dir


def save_upload(file_bytes: bytes, filename: str) -> str:
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    base = f"{uuid.uuid4().hex}_{filename}"
    path = os.path.join(UPLOAD_DIR, base)
    with open(path, "wb") as f:
        f.write(file_bytes)
    return path
