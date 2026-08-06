# Changelog

## [Unreleased]

### Changed

- Refactored application startup into a dedicated `Application` class.
- Simplified `main.py` so it only starts the application lifecycle.
- Set the project version to `1.0.0-alpha.1`.
- Combined the author name and email into one package metadata entry.
- Moved responsibility for showing the main window from `Application` to `MainController`.

### Added

- Initial repository
- Blank PySide6 application
- Project documentation
- Added `MainController` as the first MVC controller.
- Added the `controllers` package.