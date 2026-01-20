from typing import List
from PyPDF2 import PdfReader

def load_pdf_text(path: str) -> str:
    reader = PdfReader(path)
    pages = []
    for page in reader.pages:
        text = page.extract_text() or ""
        pages.append(text)
    return "\\n\\n".join(pages)

def chunk_text(text: str, max_chars: int = 6000) -> List[str]:
    chunks = []
    current = []
    current_len = 0

    for paragraph in text.split("\\n\\n"):
        p = paragraph.strip()
        if not p:
            continue

        if current_len + len(p) > max_chars and current:
            chunks.append("\\n\\n".join(current))
            current = [p]
            current_len = len(p)
        else:
            current.append(p)
            current_len += len(p)

    if current:
        chunks.append("\\n\\n".join(current))

    return chunks
