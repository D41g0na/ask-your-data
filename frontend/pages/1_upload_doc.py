import uuid
from datetime import datetime
from pathlib import Path

import streamlit as st
from utils.metadata_utils import clean_metadata, validate_metadata

from backend.database.repository_document import insert_document
from backend.ingestion.pipeline import index_document

# ROOT_DIR = Path(__file__).resolve().parents[2]
# sys.path.insert(0, str(ROOT_DIR))


st.title("Upload documents")
st.write("Add metadata to your documents. Metadata improves search and filtering.")

# NOTA: quand passage sur Docker gérer le path pour le volume
INPUT_DATA_DIR = Path("backend/input_data")
INPUT_DATA_DIR.mkdir(parents=True, exist_ok=True)

st.subheader("1. Upload_file")

uploaded_file = st.file_uploader("Choose a file", type=["pdf"], key="file_uploader")

# Add metadata to the uploaded_file
st.subheader("2. Add metadata")

with st.container(border=True):
    st.write("Example of metadata:")
    st.code("""
        author = Jane Austen
        publication_year = 1813
    """)
st.info(
    "Kind reminder that the metadata should be relevant to the content of the document and can be used to filter or sort the documents later on."
)

# Metadata management
base_metadata = {}
added_metadata = {}
reserved_keys = {
    "source",
    "uploaded_at",
    "page",
    "chunk_id",
}  # Example of reserved keys that should not be used by the user

nb_metadata = st.number_input(
    "Number of metadata fields", min_value=0, max_value=10, value=3
)

for i in range(nb_metadata):
    col1, col2 = st.columns(2)

    with col1:
        key = st.text_input(f"Metadata key {i + 1}", key=f"metadata_key_{i}")

    with col2:
        value = st.text_input(f"Metadata value {i + 1}", key=f"metadata_value_{i}")

    clean_key, clean_value = clean_metadata(key, value)

    if clean_key and clean_value:
        is_valid, message = validate_metadata(clean_key, added_metadata, reserved_keys)

        if is_valid:
            added_metadata[clean_key] = clean_value

        else:
            st.warning(message)

# Save the uploaded file and its metadata in the database
if uploaded_file:
    if st.button("Save file"):
        try:
            document_id = str(uuid.uuid4())
            file_path = INPUT_DATA_DIR / f"{document_id}_{uploaded_file.name}.pdf"

            # Base metadata to be added to all documents
            base_metadata = {
                "source": uploaded_file.name,
                "uploaded_at": datetime.now().isoformat(),
            }

            final_metadata = {**base_metadata, **added_metadata}

            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            insert_document(
                document_id,
                uploaded_file.name,
                str(file_path),
                final_metadata,
            )

            nb_chunks = index_document(document_id, str(file_path))

        except Exception as e:
            st.error(f"An error occurred while saving the document: {e}")
        else:
            st.success(f"Document saved in database with ID: {document_id}")
            st.success(f"Document indexed into {nb_chunks} chunks.")
