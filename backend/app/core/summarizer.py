import json
from collections import defaultdict
from typing import Dict
from .settings import settings

INDEX_FILE = settings.bm25_index_path


def summarize_document(doc_id: str) -> Dict:
    pages = defaultdict(str)
    try:
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            for line in f:
                obj = json.loads(line)
                if obj.get("doc_id") != doc_id:
                    continue
                pages[obj["page"]] += " " + obj.get("text", "")
    except FileNotFoundError:
        return {"sections": [], "global_summary": ""}

    sections = []
    all_text = []
    for page, text in sorted(pages.items()):
        words = text.strip().split()
        summary = " ".join(words[:50])
        sections.append({
            "pages": str(page),
            "summary": summary,
            "citation": {"doc_id": doc_id, "page": page, "chunk_id": f"{doc_id}-{page}-0"},
        })
        all_text.extend(words)
    global_summary = " ".join(all_text[:100])
    return {"sections": sections, "global_summary": global_summary}
