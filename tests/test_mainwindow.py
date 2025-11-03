import pytest
from unittest.mock import MagicMock
from PySide6.QtWidgets import QApplication

import mainwindow


class DummySerial:
    def __init__(self, *_, **__):
        self._is_open = False

    def write(self, _):
        pass

    def readline(self):
        return b""

    def close(self):
        self._is_open = False

    def isOpen(self):
        return self._is_open


@pytest.fixture(scope="session")
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


@pytest.fixture
def main_window(monkeypatch, qapp):
    monkeypatch.setattr(mainwindow.serial, "Serial", DummySerial)
    win = mainwindow.MainWindow()
    win.node_id = "1"
    yield win
    win.deleteLater()


def test_handle_update_persists_and_sends(monkeypatch, main_window):
    monkeypatch.setattr(mainwindow, "validated", lambda *_: True)
    main_window.send_command = MagicMock()

    main_window.handle_update(
        "vel",
        "123",
        "velocity",
        main_window.ui.velocity_input,
    )

    assert main_window.values["velocity"]["value"] == "123"
    main_window.send_command.assert_called_once_with("1", "vel", "123")


def test_handle_update_casts_value(monkeypatch, main_window):
    monkeypatch.setattr(mainwindow, "validated", lambda *_: True)
    main_window.send_command = MagicMock()

    main_window.handle_update("cpr", "42", "cpr", None, int)

    assert main_window.values["cpr"]["value"] == 42
    main_window.send_command.assert_called_once_with("1", "cpr", 42)


def test_handle_update_stops_on_failed_validation(monkeypatch, main_window):
    monkeypatch.setattr(mainwindow, "validated", lambda *_: False)
    main_window.send_command = MagicMock()
    original_value = main_window.values["velocity"]["value"]

    main_window.handle_update("vel", "999", "velocity", main_window.ui.velocity_input)

    assert main_window.values["velocity"]["value"] == original_value
    main_window.send_command.assert_not_called()
