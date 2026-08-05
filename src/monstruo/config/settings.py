"""Configuration loading for Monstruo."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


class Settings:
    """Load and provide Monstruo configuration values."""

    def __init__(self, config_path: Path | None = None) -> None:
        """Initialize the settings loader.

        Args:
            config_path: Optional path to a YAML configuration file.
                When omitted, Monstruo's bundled defaults are used.
        """
        self._config_path = config_path or Path(__file__).with_name("defaults.yaml")

    def load(self) -> dict[str, Any]:
        """Load and validate the YAML configuration.

        Returns:
            The loaded configuration as a dictionary.

        Raises:
            FileNotFoundError: If the configuration file does not exist.
            ValueError: If the YAML document is empty or is not a mapping.
            yaml.YAMLError: If the YAML syntax is invalid.
        """
        if not self._config_path.is_file():
            raise FileNotFoundError(
                f"Configuration file not found: {self._config_path}"
            )

        with self._config_path.open(encoding="utf-8") as config_file:
            configuration = yaml.safe_load(config_file)

        if configuration is None:
            raise ValueError(
                f"Configuration file is empty: {self._config_path}"
            )

        if not isinstance(configuration, dict):
            raise ValueError(
                "The configuration document must contain a top-level mapping."
            )

        return configuration