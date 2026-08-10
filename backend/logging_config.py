import logging
import os

_CONFIGURED = False


def setup_logging(level: str | None = None) -> None:
    """Configure logging for the whole application. Safe to call several times."""
    global _CONFIGURED
    if _CONFIGURED:
        return

    logging.basicConfig(
        level=level or os.getenv("LOG_LEVEL", "INFO"),
        format="%(asctime)s %(levelname)-8s %(name)s | %(message)s",
        datefmt="%H:%M:%S",
        force=True,
    )

    # Third-party libraries are chatty at DEBUG - keep them out of the way.
    logging.getLogger("psycopg").setLevel(logging.WARNING)

    _CONFIGURED = True