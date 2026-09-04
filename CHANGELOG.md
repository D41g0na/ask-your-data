# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/),
and this project adheres to [Semantic Versionning](https://semver.org/).

## [Unreleased]


### Added
- Database schema managed by Alembic migrations (initial revision `e90c3429c70a`)
- Dedicated PostgreSQL test database, isolated through the `test` Docker Compose profile
- PDF ingestion: text extraction and chunking
- Automatic language detection for chunks
- PostgreSQL persistence for documents and chunks
- Streamlit upload interface with metadata validation
- Connection pooling and typed configuration from environment variables
- Unit and integration test suites, run in CI GitHub Actions

### Changed
- Schema creation now runs through `alembic upgrade head` instead of a Python function

### Removed
- `backend/database/schema.py`: hard-coded table creation, replaced by Alembic migrations.