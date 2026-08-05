"""Logging configuration for Monstruo."""

from __future__ import annotations

import logging


class LoggingService:
    """Configure application-wide logging."""

    @staticmethod
    def configure(level: int = logging.INFO) -> None:
        """Configure the root logger.

        Args:
            level: Minimum logging level to emit.
        """
        logging.basicConfig(
            level=level,
            format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        )