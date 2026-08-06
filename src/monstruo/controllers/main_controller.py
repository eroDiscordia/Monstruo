"""Main-window controller for Monstruo."""

from __future__ import annotations

from monstruo.views.main_window import MainWindow


class MainController:
    """Coordinate the main application window."""

    def __init__(self, window: MainWindow) -> None:
        """Initialize the controller.

        Args:
            window: Main application window managed by this controller.
        """
        self._window = window

    def show_main_window(self) -> None:
        """Display the main application window."""
        self._window.show()