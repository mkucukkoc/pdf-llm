import subprocess, os
from .settings import settings

# ocrmypdf ile PDF -> searchable PDF

def run_ocr(input_pdf: str) -> str:
    out_pdf = input_pdf.replace(".pdf", ".ocr.pdf")
    cmd = [
        "ocrmypdf",
        "--optimize", "3",
        "--output-type", "pdf",
        "--language", "tur+eng",
        input_pdf,
        out_pdf
    ]
    subprocess.run(cmd, check=True)
    return out_pdf
