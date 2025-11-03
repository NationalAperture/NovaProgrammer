# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path
import shutil

import serial
from serial.tools import list_ports
import json
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidgetItem,
    QLineEdit,
    QMessageBox,
)
from PySide6.QtGui import QIntValidator

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow


def _asset_root() -> Path:
    """
    Return the directory containing bundled assets when running under PyInstaller,
    or the source directory during development.
    """
    return Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))


def ensure_local_asset(filename: str) -> Path:
    """
    Ensure a writable copy of an asset exists next to the executable / cwd.
    Used for files like values.json that need persistence.
    """
    local_path = Path.cwd() / filename
    if local_path.exists():
        return local_path

    source_path = _asset_root() / filename
    if not source_path.exists():
        raise FileNotFoundError(f"Unable to locate asset: {filename}")

    shutil.copy2(source_path, local_path)
    return local_path


def resolve_asset(filename: str) -> Path:
    """
    Locate an asset, preferring a writable copy in the cwd, then falling back to
    the bundled resource directory.
    """
    local_path = Path.cwd() / filename
    if local_path.exists():
        return local_path

    bundle_path = _asset_root() / filename
    if bundle_path.exists():
        return bundle_path

    raise FileNotFoundError(f"Unable to locate asset: {filename}")


def candidate_ports():
    """
    Return a list of serial port candidates across Windows, Linux, and macOS.
    """
    ports = []
    for port in list_ports.comports():
        dev = port.device  # actual device name, like "COM3" or "/dev/ttyUSB0"
        dev_lower = dev.lower()

        if sys.platform.startswith("win"):
            # Windows: COM1, COM2, ...
            if "com" in dev_lower:
                ports.append(port)

        elif sys.platform.startswith("linux"):
            # Linux: USB adapters (/dev/ttyUSBx), onboard UART (/dev/ttyAMAx)
            if "ttyusb" in dev_lower or "ttyama" in dev_lower:
                ports.append(port)

        elif sys.platform.startswith("darwin"):
            # macOS: /dev/tty.* or /dev/cu.*
            if "tty." in dev_lower or "cu." in dev_lower:
                ports.append(port)

    return ports


def read_json_file():
    path = ensure_local_asset("values.json")
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def write_json_file(data):
    path = ensure_local_asset("values.json")
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def attach_int_validator(
    line_edit: QLineEdit, min_val: int = -2_147_483_648, max_val: int = 2_147_483_647
):
    v = QIntValidator(min_val, max_val, line_edit)
    line_edit.setValidator(v)
    # Optional: a little UX polish
    line_edit.setPlaceholderText("Integer only")
    line_edit.returnPressed.connect(lambda: validate_and_warn(line_edit))
    line_edit.editingFinished.connect(lambda: validate_and_warn(line_edit))


def validate_and_warn(line_edit: QLineEdit):
    text = line_edit.text().strip()
    # QIntValidator treats empty text as Intermediate; warn if you require a value
    if text == "":
        warn("Value is required and must be an integer.")
        line_edit.setFocus()
        return

    if not line_edit.hasAcceptableInput():
        warn("Value must be an integer.")
        line_edit.setFocus()
        line_edit.selectAll()


def validated(le: QLineEdit):
    val = True
    if le is None:
        return True
    validate_and_warn(le)
    if not le.hasAcceptableInput() or le.text().strip() == "":
        val = False

    return val


def warn(msg: str):
    QMessageBox.warning(None, "Invalid Input", msg)


class MainWindow(QMainWindow):
    LINE_EDIT_FIELDS = (
        {
            "key": "velocity",
            "widget": "velocity_input",
            "button": "update_velocity_btn",
            "command": "vel",
            "cast": int,
        },
        {
            "key": "acceleration",
            "widget": "acceleration_input",
            "button": "update_acceleration_btn",
            "command": "acc",
            "cast": int,
        },
        {
            "key": "deceleration",
            "widget": "deceleration_input",
            "button": "update_deceleration_btn",
            "command": "dec",
            "cast": int,
        },
        {
            "key": "error_limit",
            "widget": "error_limit_input",
            "button": "update_error_limit_btn",
            "command": "erl",
            "cast": int,
        },
        {
            "key": "kp",
            "widget": "kp_input",
            "button": "update_kp_btn",
            "command": "skp",
            "cast": int,
        },
        {
            "key": "ki",
            "widget": "ki_input",
            "button": "update_ki_btn",
            "command": "ski",
            "cast": int,
        },
        {
            "key": "kd",
            "widget": "kd_input",
            "button": "update_kd_btn",
            "command": "skd",
            "cast": int,
        },
        {
            "key": "integrator_limit",
            "widget": "integrator_limit_input",
            "button": "update_integrator_limit_btn",
            "command": "ilm",
            "cast": int,
        },
        {
            "key": "lower_limit",
            "widget": "lower_limit_input",
            "button": "update_lower_limit_btn",
            "command": "sll",
            "cast": int,
        },
        {
            "key": "upper_limit",
            "widget": "upper_limit_input",
            "button": "update_upper_limit_btn",
            "command": "slu",
            "cast": int,
        },
        {
            "key": "ghr",
            "widget": "ghr_input",
            "button": "update_ghr_btn",
            "command": "ghr",
            "cast": int,
        },
        {
            "key": "tpi",
            "widget": "tpi_input",
            "button": "update_tpi_btn",
            "command": "tpi",
            "cast": int,
        },
        {
            "key": "cpr",
            "widget": "cpr_input",
            "button": "update_cpr_btn",
            "command": "cpr",
            "cast": int,
        },
    )

    COMBO_FIELDS = (
        {"key": "stage_type", "widget": "stage_type_box", "command": "sst"},
        {"key": "unit_type", "widget": "unit_type_box", "command": "sut"},
        {"key": "limit_behavior", "widget": "limit_behavior_box", "command": "slm"},
    )

    TOGGLE_FIELDS = (
        {"key": "drive_enable", "widget": "drive_check_box", "command": "ena"},
        {"key": "echo_enable", "widget": "echo_check_box", "command": "ech"},
        {"key": "encoder_polarity", "widget": "encoder_check_box", "command": "pol"},
    )

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Nova MC-6 Programmer")

        self.serial_port = serial.Serial()
        self.node_id = self.ui.node_ids.currentText()
        self.jog = 350
        self.hs_jog = 900
        self.values = {}

        self.load_values()
        self.set_validator()
        self._bind_line_edit_updates()
        self._bind_combo_updates()
        self._bind_toggle_updates()
        self._bind_additional_signals()

    def set_validator(self):
        for field in self.LINE_EDIT_FIELDS:
            widget = getattr(self.ui, field["widget"])
            field_values = self.values.get(field["key"], {})
            min_val = field_values.get("min_val")
            max_val = field_values.get("max_val")
            if min_val is None or max_val is None:
                continue
            attach_int_validator(widget, min_val=min_val, max_val=max_val)

    def closeEvent(self, event):
        self.save_values()
        super().closeEvent(event)

    def load_values(self):
        self.values = read_json_file()
        for field in self.LINE_EDIT_FIELDS:
            widget = getattr(self.ui, field["widget"])
            widget.setText(str(self.values[field["key"]]["value"]))

        for field in self.COMBO_FIELDS:
            widget = getattr(self.ui, field["widget"])
            widget.setCurrentIndex(self.values[field["key"]]["value"])

        for field in self.TOGGLE_FIELDS:
            widget = getattr(self.ui, field["widget"])
            widget.setChecked(bool(self.values[field["key"]]["value"]))

    def save_values(self):
        write_json_file(self.values)

    def handle_update(self, cmd, value, key, line_edit=None, cast=None):
        if line_edit is not None and not validated(line_edit):
            return
        if cast is not None:
            value = cast(value)
        self.values[key]["value"] = value
        command = (self.node_id, cmd, value)
        self.send_command(*command)

    def save_configuration(self):
        cmd = (self.node_id, "scf", "1")
        self.send_command(*cmd)

    def set_node_id(self):
        cmd = ("*", "adr", self.node_id)
        self.send_command(*cmd)

    def forward_jog(self):
        jog = self.hs_jog if self.ui.hs_check_box.isChecked() else self.jog
        cmd = (self.node_id, "jog", jog)
        self.send_command(*cmd)

    def reverse_jog(self):
        jog = self.hs_jog if self.ui.hs_check_box.isChecked() else self.jog
        cmd = (self.node_id, "jog", -jog)
        self.send_command(*cmd)

    def abort_motion(self):
        cmd = (self.node_id, "jog", 0)
        self.send_command(*cmd)

    def update_node_id(self):
        self.node_id = self.ui.node_ids.currentText()

    def search_ports(self):
        self.ui.port_combo_box.clear()
        ports = candidate_ports()
        for port, desc, hwid in reversed(ports):
            self.ui.port_combo_box.addItem(port)

    def toggle_port_connection(self):
        if self._serial_is_open():
            self.disconnect_from_port()
        else:
            self.connect_to_port()

    def disconnect_from_port(self):
        self.serial_port.close()
        self.ui.toggle_port_btn.setText("Connect to Port")
        self.ui.buad_rate_combo_box.setEnabled(True)
        self.ui.port_combo_box.setEnabled(True)

    def connect_to_port(self):
        port = self.ui.port_combo_box.currentText()
        buad_rate = self.ui.buad_rate_combo_box.currentText()

        self.serial_port = serial.Serial(port=port, baudrate=buad_rate, timeout=1)

        # Now that the port is connected disable buadrate and port selection.
        self.ui.buad_rate_combo_box.setEnabled(False)
        self.ui.port_combo_box.setEnabled(False)

        self.ui.toggle_port_btn.setText("Disconnect from Port")

    def send_command(self, node_id, cmd, param):
        if not self._serial_is_open():
            warn("Serial port is not connected.")
            return
        msg = f"{node_id} {cmd} {param}\r\n"
        self.record_sent_command(msg)
        self.serial_port.write(msg.encode())
        recv_msg = self.serial_port.readline()
        self.record_received_command(recv_msg)

    def record_sent_command(self, msg):
        self.ui.msg_table.insertRow(0)
        try:
            msg = msg.strip()
        except Exception as e:
            print(f"msg: {msg}\n")
            print(f"err: {e}")
        self.ui.msg_table.setItem(0, 0, QTableWidgetItem(msg))

    def record_received_command(self, msg):
        try:
            msg = msg.decode().strip()
            self.ui.msg_table.setItem(0, 1, QTableWidgetItem(msg))
        except Exception as e:
            print(f"msg: {msg}\n")
            print(f"err: {e}")

    def _bind_line_edit_updates(self):
        for field in self.LINE_EDIT_FIELDS:
            button = getattr(self.ui, field["button"])
            line_edit = getattr(self.ui, field["widget"])
            button.clicked.connect(
                lambda _, f=field, le=line_edit: self.handle_update(
                    f["command"], le.text(), f["key"], le, f.get("cast")
                )
            )

    def _bind_combo_updates(self):
        for field in self.COMBO_FIELDS:
            combo = getattr(self.ui, field["widget"])
            combo.currentIndexChanged.connect(
                lambda _, f=field, widget=combo: self.handle_update(
                    f["command"], widget.currentIndex() + 1, f["key"]
                )
            )

    def _bind_toggle_updates(self):
        for field in self.TOGGLE_FIELDS:
            checkbox = getattr(self.ui, field["widget"])
            checkbox.clicked.connect(
                lambda _, f=field, widget=checkbox: self.handle_update(
                    f["command"], int(widget.isChecked()), f["key"]
                )
            )

    def _bind_additional_signals(self):
        simple_connections = [
            (self.ui.set_id_btn.clicked, self.set_node_id),
            (self.ui.search_port_btn.pressed, self.search_ports),
            (self.ui.toggle_port_btn.pressed, self.toggle_port_connection),
            (self.ui.forward_job_btn.pressed, self.forward_jog),
            (self.ui.reverse_jog_btn.pressed, self.reverse_jog),
            (self.ui.forward_job_btn.released, self.abort_motion),
            (self.ui.reverse_jog_btn.released, self.abort_motion),
            (self.ui.stop_btn.pressed, self.abort_motion),
            (self.ui.save_configuration_btn.clicked, self.save_configuration),
        ]

        for signal, handler in simple_connections:
            signal.connect(handler)

        self.ui.node_ids.currentIndexChanged.connect(lambda *_: self.update_node_id())

    def _serial_is_open(self):
        if hasattr(self.serial_port, "is_open"):
            return self.serial_port.is_open
        if hasattr(self.serial_port, "isOpen"):
            return self.serial_port.isOpen()
        return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        stylesheet_path = resolve_asset("styles.qss")
        app.setStyleSheet(stylesheet_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        pass
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
