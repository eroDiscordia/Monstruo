# Monstruo Architecture

**Version:** 0.1.0
**Status:** Initial Foundation

## Purpose

Document the implemented architecture.

## Current Architecture

```text
src/
└── monstruo/
    ├── __init__.py
    ├── main.py
    └── views/
        ├── __init__.py
        └── main_window.py
```

## Application Entry Point

`src/monstruo/main.py`

Responsibilities:

1. Create `QApplication`
2. Create `MainWindow`
3. Show the window
4. Start the Qt event loop
5. Return the exit status

## View Layer

`src/monstruo/views/main_window.py` defines the blank `MainWindow`.

## Models and Controllers

Not yet implemented.

## Plugin Architecture

Not yet implemented.

## Configuration

YAML configuration is planned but not yet implemented.
