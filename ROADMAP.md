### Phase 1 - MVP

#### Product
- Upload 1 document (PDF)
- Ask a query
- Obtain an answer

#### Tech
-Text extraction (PyMuPDF OK)
- Chunking
- Embeddings
- Vector storage

#### IA
- RAG
- Prompt engineering

#### UI
- Streamlit
    - Upload
    - Query
    - Answer


### Phase 2 - Quality

#### IA
- Tuning chunk / overlap
- Top K retrieval
- Add metadata

#### Product
- Show sources used in answer
- Show chunk
- Fallback

#### Debug
- Test
    - query in scope
    - query out of scope


### Phase 3 - User experiences

#### Product
- Multi documents
- Historisation
- Reset documents

#### UX
- Loader / feedback
- Error log
