# Monstruo

Monstruo is a native KDE desktop management application for Arch Linux and CachyOS.

## Status

**Milestone 1 — Blank Qt Application**

Monstruo currently opens a blank native Qt window titled **Monstruo**.

The application does not yet contain menus, buttons, controls, or desktop-management features.

## Technology Stack

- Python 3.14
- PySide6
- Qt 6
- YAML
- Git

## Architecture Goals

- MVC architecture
- Modular design
- Plugin-ready architecture
- YAML configuration
- Strong typing
- Documentation-first development
- Git-first development
- Production-quality code

## Development Setup

Create the virtual environment:

```fish
python -m venv .venv
```

Activate it:

```fish
source .venv/bin/activate.fish
```

Install in editable mode:

```fish
python -m pip install --editable .
```

Run Monstruo:

```fish
python -m monstruo.main
```

## Documentation

See `docs/DEVELOPER_GUIDE.md`.

## License

MIT License.
# Monstruo
