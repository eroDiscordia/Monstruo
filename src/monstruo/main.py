"""Application entry point for Monstruo."""

from __future__ import annotations

from monstruo.app import Application


def main() -> int:
    """Create and run the Monstruo application."""
    application = Application()
    return application.run()


if __name__ == "__main__":
    raise SystemExit(main())