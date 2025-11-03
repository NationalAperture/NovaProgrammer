# Nova MC-6 Programmer

This desktop application provides a PySide6 interface for configuring Nova MC-6 motion controllers. It wraps the device’s serial command set with a friendlier UI so you can browse available serial ports, connect, and tweak motion parameters without hand-crafting commands.

## Key Features
- Search and select available serial ports, then connect/disconnect with one click.
- Read and persist controller parameters in `values.json`, keeping UI defaults in sync.
- Update kinematics (velocity, acceleration, deceleration), PID tuning, limits, and miscellaneous device options via dedicated controls.
- View the command log in real time: every command sent and response received appears in the message table for easy inspection.
- Package the app with PyInstaller to ship distributions for machines that lack a Python environment.

## Repository Layout
- `mainwindow.py` — main PySide6 window, signal bindings, and serial messaging.
- `ui_form.py` — generated Qt widget bindings (run `pyside6-uic form.ui -o ui_form.py` after editing `form.ui`).
- `form.ui` — Qt Designer layout source.
- `styles.qss` — theme applied at startup.
- `values.json` — persisted parameter defaults loaded at launch.
- `tests/` — pytest-based regression suite for UI logic.
- `requirements.txt` — runtime dependencies (PySide6, pyserial).

## Development Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install pytest  # for running tests
```

Launch the app with:
```bash
python mainwindow.py
```
Qt will load `styles.qss`, hydrate controls from `values.json`, and wait for you to connect to a serial port. When you toggle a setting or press an update button, the action is validated, written back into `values.json`, and dispatched over serial.

## Working on the UI
Use Qt Designer (or edit XML manually) to update `form.ui`, then regenerate bindings:
```bash
pyside6-uic form.ui -o ui_form.py
```

## Testing & Packaging
- Run automated checks:
  ```bash
  QT_QPA_PLATFORM=offscreen .venv/bin/python -m pytest
  ```
  The offscreen flag ensures tests run without a display server.
- Build a distributable binary:
  ```bash
  python -m PyInstaller mainwindow.spec
  ```
  Artifacts land in `dist/`.

## Contributing Tips
- Keep `values.json` aligned with any new widgets or parameters; the app reads/writes keys based on the config tables in `mainwindow.py`.
- Route new controller actions through `handle_update` to leverage shared validation and logging.
- Document manual test steps in pull requests, especially when adding serial commands or UI controls.
