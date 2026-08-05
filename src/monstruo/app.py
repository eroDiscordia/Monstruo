"""Application lifecycle management for Monstruo."""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from monstruo.views.main_window import MainWindow


class Application:
    """Manage the Monstruo application lifecycle."""

    def __init__(self) -> None:
        """Initialize the Qt application."""
        self._application = QApplication(sys.argv)
        self._window = MainWindow()

    def run(self) -> int:
        """Display the main window and start the Qt event loop."""
        self._window.show()
        return self._application.exec()