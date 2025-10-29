# This Python file uses the following encoding: utf-8
import sys
import serial
from serial.tools import list_ports
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

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
    with open("values.json", "w") as f:
        json.dump(data, f)


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

        self.ui.drive_check_box.clicked.connect(self.toggle_drive)
        self.ui.echo_check_box.clicked.connect(self.toggle_echo)
        self.ui.encoder_check_box.clicked.connect(self.toggle_encoder)

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
        self.ui.update_integrator_limit_btn.clicked.connect(self.update_integrator_limit)

        self.load_values()

    def closeEvent(self, event):
        self.save_values()
        super().closeEvent(event)

    def load_values(self):
        self.values = read_json_file()
        self.ui.acceleration_input.setText(str(self.values["acceleration"]))
        self.ui.velocity_input.setText(str(self.values["velocity"]))
        self.ui.deceleration_input.setText(str(self.values["deceleration"]))
        self.ui.error_limit_input.setText(str(self.values["error_limit"]))
        self.ui.kp_input.setText(str(self.values["kp"]))
        self.ui.ki_input.setText(str(self.values["ki"]))
        self.ui.kd_input.setText(str(self.values["kd"]))
        self.ui.integrator_limit_input.setText(str(self.values["integrator_limit"]))

    def save_values(self):
        write_json_file(self.values)


    def update_acceleration(self):
        accel = int(self.ui.acceleration_input.text())
        self.values["acceleration"] = accel
        cmd = (self.node_id, "acc", accel)
        self.send_command(*cmd)


    def update_velocity(self):
        vel = int(self.ui.velocity_input.text())
        self.values["velocity"] = vel
        cmd = (self.node_id, "vel", vel)
        self.send_command(*cmd)

    def update_deceleration(self):
        decel = int(self.ui.deceleration_input.text())
        self.values["deceleration"] = decel
        cmd = (self.node_id, "dec", decel)
        self.send_command(*cmd)

    def update_error_limit(self):
        err = int(self.ui.error_limit_input.text())
        self.values["error_limit"] = err
        cmd = (self.node_id, "erl", err)
        self.send_command(*cmd)

    def update_kp(self):
        kp = int(self.ui.kp_input.text())
        self.values["kp"] = kp
        cmd = (self.node_id, "skp", kp)
        self.send_command(*cmd)

    def update_ki(self):
        ki = int(self.ui.ki_input.text())
        self.values["ki"] = ki
        cmd = (self.node_id, "ski", ki)
        self.send_command(*cmd)

    def update_kd(self):
        kd = int(self.ui.kd_input.text())
        self.values["kd"] = kd
        cmd = (self.node_id, "skd", kd)
        self.send_command(*cmd)

    def update_integrator_limit(self):
        integrator = int(self.ui.integrator_limit_input.text())
        self.values["integrator_limit"] = integrator
        cmd = (self.node_id, "ilm", integrator)
        self.send_command(*cmd)

    def save_configuration(self):
        cmd = (self.node_id, "scf", "1")
        self.send_command(*cmd)


    def toggle_drive(self):
        drive = int(self.ui.drive_check_box.isChecked())
        cmd = (self.node_id, "ena", drive)
        self.send_command(*cmd)


    def toggle_echo(self):
        echo = int(self.ui.echo_check_box.isChecked())
        cmd = (self.node_id, "ech", echo)
        self.send_command(*cmd)


    def toggle_encoder(self):
        encoder = int(self.ui.encoder_check_box.isChecked())
        cmd = (self.node_id, "pol", encoder)
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
        except Exception as e:
            print(f"msg: {msg}\n")
            print(f"err: {e}")
        self.ui.msg_table.setItem(0, 1, QTableWidgetItem(msg))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
