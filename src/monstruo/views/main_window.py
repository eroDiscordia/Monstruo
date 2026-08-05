"""Main application window for Monstruo."""

from __future__ import annotations

from PySide6.QtWidgets import QWidget


class MainWindow(QWidget):
    """Blank top-level window for the Monstruo application."""

    def __init__(self, title: str) -> None:
        """Initialize the blank application window.

        Args:
            title: Text displayed in the native window title bar.
        """
        super().__init__()
        self.setWindowTitle(title)