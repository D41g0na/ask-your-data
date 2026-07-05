import pymupdf


def extract_text_from_pdf(pdf_path: str) -> list[dict]:
    """
    Extracts text from a PDF file using PyMuPDF.
    """
    extract = []
    # Open file
    doc = pymupdf.open(pdf_path)
    for page in doc:
        text = page.get_text()
        if text.strip():  # Only append if there is text on the page
            extract.append({"page": page.number + 1, "text": text})

    doc.close()

    return extract
