from frontend.utils.metadata_utils import clean_metadata, validate_metadata


def test_clean_metadata():
    # Test with normal input
    key0, value0 = "Author", "Jane Austen"
    key1, value1 = "", "test"
    key2, value2 = "Title", ""

    assert clean_metadata(key0, value0) == ("author", "Jane Austen")
    assert clean_metadata(key1, value1) == (None, "test")
    assert clean_metadata(key2, value2) == ("title", None)


def test_validate_metadata():
    reserved_keys = {"source": "", "uploaded_at": "", "page": "", "chunk_id": ""}

    clean_key0 = "author"
    clean_key1 = "source"

    added_metadata0 = {}
    added_metadata1 = {"author": "Jane Austen"}

    assert validate_metadata(clean_key0, added_metadata0, reserved_keys) == (True, None)
    assert validate_metadata(clean_key1, added_metadata0, reserved_keys) == (
        False,
        '"source" is a reserved metadata key. Please choose a different key.',
    )
    assert validate_metadata(clean_key0, added_metadata1, reserved_keys) == (
        False,
        'Duplicate metadata key: "author". Please ensure all metadata keys are unique.',
    )
