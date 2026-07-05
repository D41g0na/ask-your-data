from backend.ingestion.extract import extract_text_from_pdf


def test_extract_text_from_pdf():
    # Test that text can be extracted from a sample PDF file
    pdf_path = "test/backend/test_extract.pdf"

    extracted_text = extract_text_from_pdf(pdf_path)

    assert isinstance(extracted_text, list)
    assert len(extracted_text) > 0  # Ensure that some text was extracted
    assert "page" in extracted_text[0]
    assert "text" in extracted_text[0]
    assert isinstance(extracted_text[0]["page"], int)
    assert isinstance(extracted_text[0]["text"], str)
