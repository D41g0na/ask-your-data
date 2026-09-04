# ask-your-data
Ready-to-use chatbot to query your own data. You provide documents, the app indexes them (RAG) and answers your questions via an API and a simple interface.

### Prerequisites

Python 3.12+, uv, Docker

### Installation

```
uv sync
```

### Configuration

Copy `.env.example` in `.env` and `test/.env_test.example` in `test/.env_test.

### Database

Run Postgres, then `alembic upgrade head` to create schema.

### Running the app

```
uv run streamlit run frontend.app
```

### Running the tests

# Unit test only - no database required
pytest test/unit

# Integration tests - require the test database
docker compose --profile test up -d
pytest test/integration