import logging

import pymupdf
from langdetect import DetectorFactory, detect
from langdetect.lang_detect_exception import LangDetectException

DetectorFactory.seed = 0

logger = logging.getLogger(__name__)


def extract_text_from_pdf(pdf_path: str) -> list[dict]:
    """
    Extracts text from a PDF file using PyMuPDF.
    """
    extract = []
    skipped = 0

    # Open file
    doc = pymupdf.open(pdf_path)

    for page in doc.pages():
        text = page.get_text()

        if not text.strip():  # Only append if there is text on the page
            skipped += 1
            continue

        try:
            language = detect(text)
        except LangDetectException:
            language = "unknown"
            logger.warning(
                "Language detection failed on page %s of %s (%s chars)",
                page.number + 1,
                pdf_path,
                len(text),
            )

        extract.append({"page": page.number + 1, "text": text, "language": language})

    doc.close()

    logger.info(
        "Extracted %s pages from %s (%s skipped: no text)",
        len(extract),
        pdf_path,
        skipped,
    )

    return extract
