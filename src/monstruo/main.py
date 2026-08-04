"""Application entry point for Monstruo."""

from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from monstruo.views.main_window import MainWindow


def main() -> int:
    """Create and run the Monstruo application."""
    application = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    return application.exec()


if __name__ == "__main__":
    raise SystemExit(main())