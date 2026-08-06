# Monstruo Architecture

**Version:** 1.0.0-alpha.1
**Status:** Initial Foundation

## Purpose

Document the implemented architecture.

## Current Architecture

```text
src/
└── monstruo/
    ├── __init__.py
    ├── app.py
    ├── main.py
    ├── config/
    │   ├── __init__.py
    │   ├── defaults.yaml
    │   └── settings.py
    ├── controllers/
    │   ├── __init__.py
    │   └── main_controller.py
    ├── models/
    │   ├── __init__.py
    │   └── application_model.py
    ├── services/
    │   ├── __init__.py
    │   └── logging_service.py
    └── views/
        ├── __init__.py
        └── main_window.py
```

## Application Lifecycle

Application lifecycle management is defined in:

```text
src/monstruo/app.py
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

## Controller Layer

The first controller is defined in:

```text
ApplicationModel
MainWindow
```


## Model Layer

The first model is defined in:

```text
src/monstruo/models/application_model.py
```

## Models and Controllers

Not yet implemented.

## Plugin Architecture

Not yet implemented.

## Configuration

YAML configuration is planned but not yet implemented.
