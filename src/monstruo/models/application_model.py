"""Application data model for Monstruo."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ApplicationModel:
    """Store validated application-level data."""

    name: str

    def __post_init__(self) -> None:
        """Validate and normalize model values."""
        normalized_name = self.name.strip()

        if not normalized_name:
            raise ValueError("Application name must be a non-empty string.")

        object.__setattr__(self, "name", normalized_name)