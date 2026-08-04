"""Main application window for Monstruo."""

from __future__ import annotations

from PySide6.QtWidgets import QWidget


class MainWindow(QWidget):
    """Blank top-level window for the Monstruo application."""

    def __init__(self) -> None:
        """Initialize the blank application window."""
        super().__init__()
        self.setWindowTitle("Monstruo")