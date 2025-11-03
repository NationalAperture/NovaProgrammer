# Repository Guidelines

## Project Structure & Module Organization
- Core UI logic lives in `mainwindow.py`, which wires PySide6 widgets to serial commands.
- Generated Qt bindings reside in `ui_form.py`; update it by running `pyside6-uic form.ui -o ui_form.py` whenever `form.ui` changes.
- Styling and defaults are drawn from `styles.qss` and `values.json`; keep these files in sync with UI updates.
- Build artifacts appear under `build/` and `dist/`; treat them as disposable output from packaging.

## Build, Test, and Development Commands
- `python3 -m venv .venv && source .venv/bin/activate`: create and activate a local virtual environment.
- `pip install -r requirements.txt`: install PySide6 and pyserial dependencies.
- `python mainwindow.py`: launch the desktop app with the current UI.
- `python -m PyInstaller mainwindow.spec`: produce distributable binaries into `dist/` using the existing spec file.

## Coding Style & Naming Conventions
- Follow PEP 8 for Python: 4-space indentation, descriptive snake_case identifiers, and class names in PascalCase.
- Keep Qt signal-slot hookups grouped in `MainWindow.__init__`, mirroring widget names defined in `form.ui`.
- Persist shared UI mutations through helper methods like `handle_update` to avoid duplication.

## Testing Guidelines
- No automated test suite exists yet; rely on manual validation by running `python mainwindow.py` and exercising controls.
- When adding logic, prefer extracting side-effect-free helpers that can be unit tested later.
- Document any manual test steps in pull requests so others can repeat them.

## Commit & Pull Request Guidelines
- Use imperative, present-tense commit subjects (`Refactor handle_update usage`) and keep them under ~72 characters.
- Reference related issues in the commit body or PR description, and summarize user-visible changes.
- For UI updates, include screenshots or short descriptions of the before/after state; for serial changes, list the commands touched.
- Ensure PRs describe validation performed (manual steps, packaging runs) and mention any follow-up tasks.
