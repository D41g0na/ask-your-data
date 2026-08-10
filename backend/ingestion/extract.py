import pymupdf
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

DetectorFactory.seed = 0



def extract_text_from_pdf(pdf_path: str) -> list[dict]:
    """
    Extracts text from a PDF file using PyMuPDF.
    """
    extract = []
    # Open file
    doc = pymupdf.open(pdf_path)

    for page in doc.pages():
        text = page.get_text()

        if not text.strip():  # Only append if there is text on the page
            continue

        try:
            language = detect(text)
        except LangDetectException:
            language = "unknown"
            
        extract.append({"page": page.number + 1, "text": text, "language": language})

    doc.close()

    return extract
