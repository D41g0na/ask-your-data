from pathlib import Path

from backend.ingestion.extract import extract_text_from_pdf


def test_extract_text_from_pdf():
    # Test that text can be extracted from a sample PDF file
    pdf_path = Path(__file__).parent / "test_extract.pdf"

    extracted_text = extract_text_from_pdf(pdf_path)

    assert isinstance(extracted_text, list)
    assert len(extracted_text) > 0  # Ensure that some text was extracted
    assert "page" in extracted_text[0]
    assert "text" in extracted_text[0]
    assert "language" in extracted_text[0]
    assert isinstance(extracted_text[0]["page"], int)
    assert isinstance(extracted_text[0]["text"], str)
    assert isinstance(extracted_text[0]["language"], str)

def test_extract_text_from_empty_pdf():
    # Test that extracting text from an empty PDF returns an empty list
    pdf_path_none = Path(__file__).parent / "test_extract_none.pdf"

    extracted_text = extract_text_from_pdf(pdf_path_none)

    assert isinstance(extracted_text, list)
    assert len(extracted_text) == 0 

def test_extract_text_from_pdf_with_non_text_content():
    # Test that extracting text from a PDF with non-text content returns an empty list
    pdf_path_number = Path(__file__).parent / "test_extract_number.pdf"

    extracted_text = extract_text_from_pdf(pdf_path_number)

    assert isinstance(extracted_text, list)
    assert len(extracted_text) == 1 
    assert extracted_text[0]["language"] == "unknown"
