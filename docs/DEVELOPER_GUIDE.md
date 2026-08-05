# Monstruo Developer Guide

**Version:** 1.0.0-alpha.1

## Purpose

Describe how Monstruo is developed and why architectural decisions are made.

## Milestone 1

Objective: Create a blank native Qt window titled **Monstruo**.

### Source Layout

```text
src/
└── monstruo/
    ├── main.py
    └── views/
        └── main_window.py
```

### Verification

- Application launches.
- Window title is `Monstruo`.
- Window is blank.
- Exit status is `0`.

### Lessons Learned

- Use a Python virtual environment.
- Verify every step before proceeding.
- Keep documentation synchronized with implementation.
