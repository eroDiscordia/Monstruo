"""Main-window controller for Monstruo."""

from __future__ import annotations

from monstruo.models.application_model import ApplicationModel
from monstruo.views.main_window import MainWindow


class MainController:
    """Coordinate the main application window."""

    def __init__(
        self,
        model: ApplicationModel,
        window: MainWindow,
    ) -> None:
        """Initialize the controller.

        Args:
            model: Validated application data.
            window: Main application window managed by this controller.
        """
        self._model = model
        self._window = window

    def initialize_view(self) -> None:
        """Apply model data to the main window."""
        self._window.setWindowTitle(self._model.name)

    def show_main_window(self) -> None:
        """Display the main application window."""
        self._window.show()