import re, uuid
from typing import List, Dict

MAX_TOKENS = 350
OVERLAP = 80

# çok basit kelime bazlı bölücü (demo)

def sliding_window(words: list[str], max_len=MAX_TOKENS, overlap=OVERLAP):
    i = 0
    n = len(words)
    while i < n:
        j = min(n, i + max_len)
        yield words[i:j]
        if j == n:
            break
        i = j - overlap


def make_chunks(doc_id: str, page_texts: list[dict]) -> List[Dict]:
    chunks = []
    for page in page_texts:
        text = page.get("text", "").strip()
        if not text:
            continue
        words = text.split()
        for idx, window in enumerate(sliding_window(words)):
            t = " ".join(window)
            chunks.append({
                "id": f"{doc_id}-{page['page_num']}-{idx}",
                "doc_id": doc_id,
                "page": page["page_num"],
                "section": page.get("section"),
                "text": t
            })
    return chunks
