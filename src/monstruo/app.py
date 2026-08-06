"""Application lifecycle management for Monstruo."""

from __future__ import annotations

import logging
import sys
from typing import Any

from PySide6.QtWidgets import QApplication

from monstruo.config.settings import Settings
from monstruo.controllers.main_controller import MainController
from monstruo.services.logging_service import LoggingService
from monstruo.views.main_window import MainWindow


class Application:
    """Manage the Monstruo application lifecycle."""

    def __init__(self) -> None:
        """Initialize the Qt application and its dependencies."""
        LoggingService.configure()

        self._logger = logging.getLogger(__name__)
        self._logger.info("Starting Monstruo")

        self._settings = Settings()
        self._configuration = self._settings.load()

        application_name = self._get_application_name(self._configuration)

        self._application = QApplication(sys.argv)
        self._application.setApplicationName(application_name)

        self._window = MainWindow(title=application_name)
        self._controller = MainController(window=self._window)

        self._logger.info("Monstruo initialized")

    def run(self) -> int:
        """Display the main window and start the Qt event loop."""
        self._controller.show_main_window()
        return self._application.exec()

    @staticmethod
    def _get_application_name(configuration: dict[str, Any]) -> str:
        """Read and validate the configured application name.

        Args:
            configuration: Loaded application configuration.

        Returns:
            The configured application name.

        Raises:
            ValueError: If the application name is missing or invalid.
        """
        application = configuration.get("application")

        if not isinstance(application, dict):
            raise ValueError(
                "Configuration section 'application' must be a mapping."
            )

        name = application.get("name")

        if not isinstance(name, str) or not name.strip():
            raise ValueError(
                "Configuration value 'application.name' must be a non-empty string."
            )

        return name.strip()