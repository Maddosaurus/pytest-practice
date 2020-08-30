import json
import logging
from typing import Any, Dict


def partly_pretty_format(data: Dict[str, Any]) -> str:
    return f'common_name: {data["common_name"]} -> {data["not_before"]} - {data["not_after"]} issuer_name: {data["issuer_name"]}'


def setup_logging():
    """Set up console logger for normal operation."""
    logger = logging.getLogger("pytest_practice")
    logger.setLevel(logging.DEBUG)

    # Console logging
    log_formatter = logging.Formatter("[%(levelname)-8s] [%(name)-24s] %(message)s")
    log_handler = logging.StreamHandler()
    log_handler.setFormatter(log_formatter)
    log_handler.setLevel(logging.DEBUG)

    logger.addHandler(log_handler)
