# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path

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
    with open("values.json", "r") as f:
        data = json.load(f)
        return data


def write_json_file(data):
    with open("values.json", "w", encoding="utf-8") as f:
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

        self.ui.drive_check_box.clicked.connect(self.toggle_drive)
        self.ui.echo_check_box.clicked.connect(self.toggle_echo)
        self.ui.encoder_check_box.clicked.connect(self.toggle_encoder)

        self.ui.stage_type_box.currentIndexChanged.connect(self.update_stage_type)
        self.ui.unit_type_box.currentIndexChanged.connect(self.update_unit_type)
        self.ui.limit_behavior_box.currentIndexChanged.connect(
            self.update_limit_behavior
        )

        self.ui.node_ids.currentIndexChanged.connect(self.update_node_id)
        self.ui.set_id_btn.clicked.connect(self.set_node_id)
        self.ui.search_port_btn.pressed.connect(self.search_ports)
        self.ui.toggle_port_btn.pressed.connect(self.toggle_port_connection)
        self.ui.forward_job_btn.pressed.connect(self.forward_jog)
        self.ui.reverse_jog_btn.pressed.connect(self.reverse_jog)
        self.ui.forward_job_btn.released.connect(self.abort_motion)
        self.ui.reverse_jog_btn.released.connect(self.abort_motion)
        self.ui.stop_btn.pressed.connect(self.abort_motion)

        self.ui.save_configuration_btn.clicked.connect(self.save_configuration)
        self.ui.update_acceleration_btn.clicked.connect(self.update_acceleration)
        self.ui.update_velocity_btn.clicked.connect(self.update_velocity)
        self.ui.update_deceleration_btn.clicked.connect(self.update_deceleration)
        self.ui.update_error_limit_btn.clicked.connect(self.update_error_limit)
        self.ui.update_kp_btn.clicked.connect(self.update_kp)
        self.ui.update_ki_btn.clicked.connect(self.update_ki)
        self.ui.update_kd_btn.clicked.connect(self.update_kd)
        self.ui.update_integrator_limit_btn.clicked.connect(
            self.update_integrator_limit
        )
        self.ui.update_lower_limit_btn.clicked.connect(self.update_lower_limit)
        self.ui.update_upper_limit_btn.clicked.connect(self.update_upper_limit)
        self.ui.update_ghr_btn.clicked.connect(self.update_ghr)
        self.ui.update_tpi_btn.clicked.connect(self.update_tpi)
        self.ui.update_cpr_btn.clicked.connect(self.update_cpr)

    def set_validator(self):
        attach_int_validator(
            self.ui.velocity_input,
            min_val=self.values["velocity"]["min_val"],
            max_val=self.values["velocity"]["max_val"],
        )
        attach_int_validator(
            self.ui.acceleration_input,
            min_val=self.values["acceleration"]["min_val"],
            max_val=self.values["acceleration"]["max_val"],
        )
        attach_int_validator(
            self.ui.deceleration_input,
            min_val=self.values["deceleration"]["min_val"],
            max_val=self.values["deceleration"]["max_val"],
        )
        attach_int_validator(
            self.ui.error_limit_input,
            min_val=self.values["error_limit"]["min_val"],
            max_val=self.values["error_limit"]["max_val"],
        )
        attach_int_validator(
            self.ui.kp_input,
            min_val=self.values["kp"]["min_val"],
            max_val=self.values["kp"]["max_val"],
        )
        attach_int_validator(
            self.ui.ki_input,
            min_val=self.values["ki"]["min_val"],
            max_val=self.values["ki"]["max_val"],
        )
        attach_int_validator(
            self.ui.kd_input,
            min_val=self.values["kd"]["min_val"],
            max_val=self.values["kd"]["max_val"],
        )
        attach_int_validator(
            self.ui.integrator_limit_input,
            min_val=self.values["integrator_limit"]["min_val"],
            max_val=self.values["integrator_limit"]["max_val"],
        )
        attach_int_validator(
            self.ui.lower_limit_input,
            min_val=self.values["lower_limit"]["min_val"],
            max_val=self.values["lower_limit"]["max_val"],
        )
        attach_int_validator(
            self.ui.upper_limit_input,
            min_val=self.values["upper_limit"]["min_val"],
            max_val=self.values["upper_limit"]["max_val"],
        )
        attach_int_validator(
            self.ui.ghr_input,
            min_val=self.values["ghr"]["min_val"],
            max_val=self.values["ghr"]["max_val"],
        )
        attach_int_validator(
            self.ui.tpi_input,
            min_val=self.values["tpi"]["min_val"],
            max_val=self.values["tpi"]["max_val"],
        )
        attach_int_validator(
            self.ui.cpr_input,
            min_val=self.values["cpr"]["min_val"],
            max_val=self.values["cpr"]["max_val"],
        )

    def closeEvent(self, event):
        self.save_values()
        super().closeEvent(event)

    def load_values(self):
        self.values = read_json_file()
        self.ui.acceleration_input.setText(str(self.values["acceleration"]["value"]))
        self.ui.velocity_input.setText(str(self.values["velocity"]["value"]))
        self.ui.deceleration_input.setText(str(self.values["deceleration"]["value"]))
        self.ui.error_limit_input.setText(str(self.values["error_limit"]["value"]))
        self.ui.kp_input.setText(str(self.values["kp"]["value"]))
        self.ui.ki_input.setText(str(self.values["ki"]["value"]))
        self.ui.kd_input.setText(str(self.values["kd"]["value"]))
        self.ui.integrator_limit_input.setText(
            str(self.values["integrator_limit"]["value"])
        )
        self.ui.drive_check_box.setChecked(self.values["drive_enable"]["value"])
        self.ui.echo_check_box.setChecked(self.values["echo_enable"]["value"])
        self.ui.encoder_check_box.setChecked(self.values["encoder_polarity"]["value"])
        self.ui.lower_limit_input.setText(str(self.values["lower_limit"]["value"]))
        self.ui.upper_limit_input.setText(str(self.values["upper_limit"]["value"]))
        self.ui.ghr_input.setText(str(self.values["ghr"]["value"]))
        self.ui.tpi_input.setText(str(self.values["tpi"]["value"]))
        self.ui.cpr_input.setText(str(self.values["cpr"]["value"]))
        self.ui.stage_type_box.setCurrentIndex(self.values["stage_type"]["value"])
        self.ui.unit_type_box.setCurrentIndex(self.values["unit_type"]["value"])
        self.ui.limit_behavior_box.setCurrentIndex(
            self.values["limit_behavior"]["value"]
        )

    def save_values(self):
        write_json_file(self.values)

    def update_acceleration(self):
        self.handle_update(
            "acc",
            self.ui.acceleration_input.text(),
            "acceleration",
            self.ui.acceleration_input,
            int,
        )

    def update_velocity(self):
        self.handle_update(
            "vel",
            self.ui.velocity_input.text(),
            "velocity",
            self.ui.velocity_input,
            int,
        )

    def update_deceleration(self):
        self.handle_update(
            "dec",
            self.ui.deceleration_input.text(),
            "deceleration",
            self.ui.deceleration_input,
            int,
        )

    def update_error_limit(self):
        self.handle_update(
            "erl",
            self.ui.error_limit_input.text(),
            "error_limit",
            self.ui.error_limit_input,
            int,
        )

    def update_kp(self):
        self.handle_update("skp", self.ui.kp_input.text(), "kp", self.ui.kp_input, int)

    def update_ki(self):
        self.handle_update("ski", self.ui.ki_input.text(), "ki", self.ui.ki_input, int)

    def update_kd(self):
        self.handle_update("skd", self.ui.kd_input.text(), "kd", self.ui.kd_input, int)

    def update_integrator_limit(self):
        self.handle_update(
            "ilm",
            self.ui.integrator_limit_input.text(),
            "integrator_limit",
            self.ui.integrator_limit_input,
            int,
        )

    def update_lower_limit(self):
        self.handle_update(
            "sll",
            self.ui.lower_limit_input.text(),
            "lower_limit",
            self.ui.lower_limit_input,
            int,
        )

    def update_upper_limit(self):
        self.handle_update(
            "slu",
            self.ui.upper_limit_input.text(),
            "upper_limit",
            self.ui.upper_limit_input,
            int,
        )

    def update_ghr(self):
        self.handle_update(
            "ghr",
            self.ui.ghr_input.text(),
            "ghr",
            self.ui.ghr_input,
            int,
        )

    def update_tpi(self):
        self.handle_update(
            "tpi",
            self.ui.tpi_input.text(),
            "tpi",
            self.ui.tpi_input,
            int,
        )

    def update_cpr(self):
        self.handle_update(
            "cpr",
            self.ui.cpr_input.text(),
            "cpr",
            self.ui.cpr_input,
            int,
        )

    def update_stage_type(self):
        self.handle_update(
            "sst",
            self.ui.stage_type_box.currentIndex(),
            "stage_type",
        )

    def update_unit_type(self):
        self.handle_update(
            "sut",
            self.ui.unit_type_box.currentIndex(),
            "unit_type",
        )

    def update_limit_behavior(self):
        self.handle_update(
            "slb",
            self.ui.limit_behavior_box.currentIndex(),
            "limit_behavior",
        )

    def toggle_drive(self):
        self.handle_update(
            "ena",
            int(self.ui.drive_check_box.isChecked()),
            "drive_enabled",
        )

    def toggle_echo(self):
        self.handle_update(
            "ech",
            int(self.ui.echo_check_box.isChecked()),
            "echo_enabled",
        )

    def toggle_encoder(self):
        self.handle_update(
            "pol",
            int(self.ui.encoder_check_box.isChecked()),
            "encoder_polarity",
        )

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
        if self.serial_port.isOpen():
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(Path(f"styles.qss").read_text())
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
