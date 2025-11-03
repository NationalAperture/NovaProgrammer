# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1133, 558)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toggle_port_btn = QPushButton(self.centralwidget)
        self.toggle_port_btn.setObjectName(u"toggle_port_btn")
        font = QFont()
        font.setPointSize(15)
        self.toggle_port_btn.setFont(font)

        self.gridLayout.addWidget(self.toggle_port_btn, 0, 3, 1, 1)

        self.port_combo_box = QComboBox(self.centralwidget)
        self.port_combo_box.setObjectName(u"port_combo_box")
        self.port_combo_box.setFont(font)

        self.gridLayout.addWidget(self.port_combo_box, 0, 2, 1, 1)

        self.search_port_btn = QPushButton(self.centralwidget)
        self.search_port_btn.setObjectName(u"search_port_btn")
        self.search_port_btn.setFont(font)

        self.gridLayout.addWidget(self.search_port_btn, 0, 1, 1, 1)

        self.buad_rate_combo_box = QComboBox(self.centralwidget)
        self.buad_rate_combo_box.addItem("")
        self.buad_rate_combo_box.addItem("")
        self.buad_rate_combo_box.addItem("")
        self.buad_rate_combo_box.addItem("")
        self.buad_rate_combo_box.addItem("")
        self.buad_rate_combo_box.addItem("")
        self.buad_rate_combo_box.setObjectName(u"buad_rate_combo_box")
        self.buad_rate_combo_box.setFont(font)
        self.buad_rate_combo_box.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.buad_rate_combo_box.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.gridLayout.addWidget(self.buad_rate_combo_box, 0, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.reverse_jog_btn = QPushButton(self.widget)
        self.reverse_jog_btn.setObjectName(u"reverse_jog_btn")
        self.reverse_jog_btn.setFont(font)

        self.gridLayout_2.addWidget(self.reverse_jog_btn, 1, 2, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.stop_btn = QPushButton(self.widget)
        self.stop_btn.setObjectName(u"stop_btn")
        self.stop_btn.setFont(font)

        self.gridLayout_2.addWidget(self.stop_btn, 2, 0, 1, 3)

        self.forward_job_btn = QPushButton(self.widget)
        self.forward_job_btn.setObjectName(u"forward_job_btn")
        self.forward_job_btn.setFont(font)

        self.gridLayout_2.addWidget(self.forward_job_btn, 1, 0, 1, 1)

        self.node_ids = QComboBox(self.widget)
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.addItem("")
        self.node_ids.setObjectName(u"node_ids")
        self.node_ids.setFont(font)

        self.gridLayout_2.addWidget(self.node_ids, 0, 1, 1, 1)

        self.set_id_btn = QPushButton(self.widget)
        self.set_id_btn.setObjectName(u"set_id_btn")
        self.set_id_btn.setFont(font)

        self.gridLayout_2.addWidget(self.set_id_btn, 0, 2, 1, 1)

        self.hs_check_box = QCheckBox(self.widget)
        self.hs_check_box.setObjectName(u"hs_check_box")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hs_check_box.sizePolicy().hasHeightForWidth())
        self.hs_check_box.setSizePolicy(sizePolicy)
        self.hs_check_box.setFont(font)

        self.gridLayout_2.addWidget(self.hs_check_box, 1, 1, 1, 1)

        self.msg_table = QTableWidget(self.widget)
        if (self.msg_table.columnCount() < 2):
            self.msg_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.msg_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.msg_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.msg_table.setObjectName(u"msg_table")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(False)
        font1.setItalic(False)
        self.msg_table.setFont(font1)
        self.msg_table.setAlternatingRowColors(True)
        self.msg_table.horizontalHeader().setCascadingSectionResizes(False)
        self.msg_table.horizontalHeader().setDefaultSectionSize(185)
        self.msg_table.horizontalHeader().setStretchLastSection(True)
        self.msg_table.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.msg_table, 3, 0, 1, 3)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 2)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.save_configuration_btn = QPushButton(self.widget_2)
        self.save_configuration_btn.setObjectName(u"save_configuration_btn")
        self.save_configuration_btn.setFont(font)

        self.verticalLayout.addWidget(self.save_configuration_btn)

        self.scrollArea = QScrollArea(self.widget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(90, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 522, 606))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)

        self.update_tpi_btn = QPushButton(self.scrollAreaWidgetContents)
        self.update_tpi_btn.setObjectName(u"update_tpi_btn")
        self.update_tpi_btn.setFont(font)

        self.gridLayout_3.addWidget(self.update_tpi_btn, 13, 2, 1, 1)

        self.acceleration_input = QLineEdit(self.scrollAreaWidgetContents)
        self.acceleration_input.setObjectName(u"acceleration_input")
        self.acceleration_input.setFont(font)

        self.gridLayout_3.addWidget(self.acceleration_input, 2, 1, 1, 1)

        self.update_ki_btn = QPushButton(self.scrollAreaWidgetContents)
        self.update_ki_btn.setObjectName(u"update_ki_btn")
        self.update_ki_btn.setMinimumSize(QSize(90, 35))
        self.update_ki_btn.setFont(font)

        self.gridLayout_3.addWidget(self.update_ki_btn, 7, 2, 1, 1)

        self.integrator_limit_input = QLineEdit(self.scrollAreaWidgetContents)
        self.integrator_limit_input.setObjectName(u"integrator_limit_input")
        self.integrator_limit_input.setFont(font)

        self.gridLayout_3.addWidget(self.integrator_limit_input, 9, 1, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_11, 11, 0, 1, 1)

        self.upper_limit_input = QLineEdit(self.scrollAreaWidgetContents)
        self.upper_limit_input.setObjectName(u"upper_limit_input")
        self.upper_limit_input.setFont(font)

        self.gridLayout_3.addWidget(self.upper_limit_input, 11, 1, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)

        self.ki_input = QLineEdit(self.scrollAreaWidgetContents)
        self.ki_input.setObjectName(u"ki_input")
        self.ki_input.setFont(font)

        self.gridLayout_3.addWidget(self.ki_input, 7, 1, 1, 1)

        self.kp_input = QLineEdit(self.scrollAreaWidgetContents)
        self.kp_input.setObjectName(u"kp_input")
        self.kp_input.setFont(font)

        self.gridLayout_3.addWidget(self.kp_input, 6, 1, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)

        self.update_acceleration_btn = QPushButton(self.scrollAreaWidgetContents)
        self.update_acceleration_btn.setObjectName(u"update_acceleration_btn")
        self.update_acceleration_btn.setMinimumSize(QSize(90, 35))
        self.update_acceleration_btn.setFont(font)

        self.gridLayout_3.addWidget(self.update_acceleration_btn, 2, 2, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_6, 6, 0, 1, 1)

        self.update_kd_btn = QPushButton(self.scrollAreaWidgetContents)
        self.update_kd_btn.setObjectName(u"update_kd_btn")
        self.update_kd_btn.setMinimumSize(QSize(90, 35))
        self.update_kd_btn.setFont(font)

        self.gridLayout_3.addWidget(self.update_kd_btn, 8, 2, 1, 1)

        self.stage_type_box = QComboBox(self.scrollAreaWidgetContents)
        self.stage_type_box.addItem("")
        self.stage_type_box.addItem("")
        self.stage_type_box.addItem("")
        self.stage_type_box.setObjectName(u"stage_type_box")
        self.stage_type_box.setFont(font)

        self.gridLayout_3.addWidget(self.stage_type_box, 1, 0, 1, 1)

        self.drive_check_box = QCheckBox(self.scrollAreaWidgetContents)
        self.drive_check_box.setObjectName(u"drive_check_box")
        self.drive_check_box.setFont(font)
        self.drive_check_box.setChecked(False)

        self.gridLayout_3.addWidget(self.drive_check_box, 0, 0, 1, 1)

        self.update_velocity_btn = QPushButton(self.scrollAreaWidgetContents)
        self.update_velocity_btn.setObjectName(u"update_velocity_btn")
        self.update_velocity_btn.setMinimumSize(QSize(90, 35))
        self.update_velocity_btn.setFont(font)

        self.gridLayout_3.addWidget(self.update_velocity_btn, 3, 2, 1, 1)

        self.update_error_limit_btn = QPushButton(self.scrollAreaWidgetContents)
        self.update_error_limit_btn.setObjectName(u"update_error_limit_btn")
        self.update_error_limit_btn.setMinimumSize(QSize(90, 35))
        self.update_error_limit_btn.setFont(font)

        self.gridLayout_3.addWidget(self.update_error_limit_btn, 5, 2, 1, 1)

        self.kd_input = QLineEdit(self.scrollAreaWidgetContents)
        self.kd_input.setObjectName(u"kd_input")
        self.kd_input.setFont(font)

        self.gridLayout_3.addWidget(self.kd_input, 8, 1, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_9, 9, 0, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_5, 5, 0, 1, 1)

        self.update_ghr_btn = QPushButton(self.scrollAreaWidgetContents)
        self.update_ghr_btn.setObjectName(u"update_ghr_btn")
        self.update_ghr_btn.setFont(font)

        self.gridLayout_3.addWidget(self.update_ghr_btn, 12, 2, 1, 1)

        self.limit_behavior_box = QComboBox(self.scrollAreaWidgetContents)
        self.limit_behavior_box.addItem("")
        self.limit_behavior_box.addItem("")
        self.limit_behavior_box.addItem("")
        self.limit_behavior_box.setObjectName(u"limit_behavior_box")
        self.limit_behavior_box.setFont(font)

        self.gridLayout_3.addWidget(self.limit_behavior_box, 1, 2, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_7, 7, 0, 1, 1)

        self.encoder_check_box = QCheckBox(self.scrollAreaWidgetContents)
        self.encoder_check_box.setObjectName(u"encoder_check_box")
        self.encoder_check_box.setFont(font)

        self.gridLayout_3.addWidget(self.encoder_check_box, 0, 2, 1, 1)

        self.update_deceleration_btn = QPushButton(self.scrollAreaWidgetContents)
        self.update_deceleration_btn.setObjectName(u"update_deceleration_btn")
        self.update_deceleration_btn.setMinimumSize(QSize(90, 35))
        self.update_deceleration_btn.setFont(font)

        self.gridLayout_3.addWidget(self.update_deceleration_btn, 4, 2, 1, 1)

        self.velocity_input = QLineEdit(self.scrollAreaWidgetContents)
        self.velocity_input.setObjectName(u"velocity_input")
        self.velocity_input.setFont(font)

        self.gridLayout_3.addWidget(self.velocity_input, 3, 1, 1, 1)

        self.error_limit_input = QLineEdit(self.scrollAreaWidgetContents)
        self.error_limit_input.setObjectName(u"error_limit_input")
        self.error_limit_input.setFont(font)

        self.gridLayout_3.addWidget(self.error_limit_input, 5, 1, 1, 1)

        self.update_kp_btn = QPushButton(self.scrollAreaWidgetContents)
        self.update_kp_btn.setObjectName(u"update_kp_btn")
        self.update_kp_btn.setMinimumSize(QSize(90, 35))
        self.update_kp_btn.setFont(font)

        self.gridLayout_3.addWidget(self.update_kp_btn, 6, 2, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_8, 8, 0, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_10, 10, 0, 1, 1)

        self.echo_check_box = QCheckBox(self.scrollAreaWidgetContents)
        self.echo_check_box.setObjectName(u"echo_check_box")
        self.echo_check_box.setFont(font)

        self.gridLayout_3.addWidget(self.echo_check_box, 0, 1, 1, 1)

        self.lower_limit_input = QLineEdit(self.scrollAreaWidgetContents)
        self.lower_limit_input.setObjectName(u"lower_limit_input")
        self.lower_limit_input.setFont(font)

        self.gridLayout_3.addWidget(self.lower_limit_input, 10, 1, 1, 1)

        self.deceleration_input = QLineEdit(self.scrollAreaWidgetContents)
        self.deceleration_input.setObjectName(u"deceleration_input")
        self.deceleration_input.setFont(font)

        self.gridLayout_3.addWidget(self.deceleration_input, 4, 1, 1, 1)

        self.update_upper_limit_btn = QPushButton(self.scrollAreaWidgetContents)
        self.update_upper_limit_btn.setObjectName(u"update_upper_limit_btn")
        self.update_upper_limit_btn.setFont(font)

        self.gridLayout_3.addWidget(self.update_upper_limit_btn, 11, 2, 1, 1)

        self.update_integrator_limit_btn = QPushButton(self.scrollAreaWidgetContents)
        self.update_integrator_limit_btn.setObjectName(u"update_integrator_limit_btn")
        self.update_integrator_limit_btn.setMinimumSize(QSize(90, 35))
        self.update_integrator_limit_btn.setFont(font)

        self.gridLayout_3.addWidget(self.update_integrator_limit_btn, 9, 2, 1, 1)

        self.update_lower_limit_btn = QPushButton(self.scrollAreaWidgetContents)
        self.update_lower_limit_btn.setObjectName(u"update_lower_limit_btn")
        self.update_lower_limit_btn.setMinimumSize(QSize(0, 35))
        self.update_lower_limit_btn.setFont(font)

        self.gridLayout_3.addWidget(self.update_lower_limit_btn, 10, 2, 1, 1)

        self.unit_type_box = QComboBox(self.scrollAreaWidgetContents)
        self.unit_type_box.addItem("")
        self.unit_type_box.addItem("")
        self.unit_type_box.addItem("")
        self.unit_type_box.addItem("")
        self.unit_type_box.addItem("")
        self.unit_type_box.setObjectName(u"unit_type_box")
        self.unit_type_box.setFont(font)

        self.gridLayout_3.addWidget(self.unit_type_box, 1, 1, 1, 1)

        self.update_cpr_btn = QPushButton(self.scrollAreaWidgetContents)
        self.update_cpr_btn.setObjectName(u"update_cpr_btn")
        self.update_cpr_btn.setFont(font)

        self.gridLayout_3.addWidget(self.update_cpr_btn, 14, 2, 1, 1)

        self.ghr_input = QLineEdit(self.scrollAreaWidgetContents)
        self.ghr_input.setObjectName(u"ghr_input")
        self.ghr_input.setFont(font)

        self.gridLayout_3.addWidget(self.ghr_input, 12, 1, 1, 1)

        self.tpi_input = QLineEdit(self.scrollAreaWidgetContents)
        self.tpi_input.setObjectName(u"tpi_input")
        self.tpi_input.setFont(font)

        self.gridLayout_3.addWidget(self.tpi_input, 13, 1, 1, 1)

        self.cpr_input = QLineEdit(self.scrollAreaWidgetContents)
        self.cpr_input.setObjectName(u"cpr_input")
        self.cpr_input.setFont(font)

        self.gridLayout_3.addWidget(self.cpr_input, 14, 1, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_12, 12, 0, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_13, 13, 0, 1, 1)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_14, 14, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.gridLayout.addWidget(self.widget_2, 1, 2, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1133, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggle_port_btn.setText(QCoreApplication.translate("MainWindow", u"Connect to Port", None))
        self.search_port_btn.setText(QCoreApplication.translate("MainWindow", u"Search Ports", None))
        self.buad_rate_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"9600", None))
        self.buad_rate_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"14400", None))
        self.buad_rate_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"19200", None))
        self.buad_rate_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"38400", None))
        self.buad_rate_combo_box.setItemText(4, QCoreApplication.translate("MainWindow", u"57600", None))
        self.buad_rate_combo_box.setItemText(5, QCoreApplication.translate("MainWindow", u"115200", None))

        self.reverse_jog_btn.setText(QCoreApplication.translate("MainWindow", u"Reverse Jog", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Node ID:", None))
        self.stop_btn.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.forward_job_btn.setText(QCoreApplication.translate("MainWindow", u"Forward Jog", None))
        self.node_ids.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.node_ids.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.node_ids.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.node_ids.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.node_ids.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.node_ids.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.node_ids.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.node_ids.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.node_ids.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.node_ids.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.node_ids.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.node_ids.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.node_ids.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.node_ids.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.node_ids.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.node_ids.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.node_ids.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.node_ids.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.node_ids.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.node_ids.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))
        self.node_ids.setItemText(20, QCoreApplication.translate("MainWindow", u"21", None))
        self.node_ids.setItemText(21, QCoreApplication.translate("MainWindow", u"22", None))
        self.node_ids.setItemText(22, QCoreApplication.translate("MainWindow", u"23", None))
        self.node_ids.setItemText(23, QCoreApplication.translate("MainWindow", u"24", None))
        self.node_ids.setItemText(24, QCoreApplication.translate("MainWindow", u"25", None))
        self.node_ids.setItemText(25, QCoreApplication.translate("MainWindow", u"26", None))
        self.node_ids.setItemText(26, QCoreApplication.translate("MainWindow", u"27", None))
        self.node_ids.setItemText(27, QCoreApplication.translate("MainWindow", u"28", None))
        self.node_ids.setItemText(28, QCoreApplication.translate("MainWindow", u"29", None))
        self.node_ids.setItemText(29, QCoreApplication.translate("MainWindow", u"30", None))
        self.node_ids.setItemText(30, QCoreApplication.translate("MainWindow", u"31", None))
        self.node_ids.setItemText(31, QCoreApplication.translate("MainWindow", u"32", None))

        self.set_id_btn.setText(QCoreApplication.translate("MainWindow", u"Set ID", None))
        self.hs_check_box.setText(QCoreApplication.translate("MainWindow", u"High Speed", None))
        ___qtablewidgetitem = self.msg_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Message Sent", None));
        ___qtablewidgetitem1 = self.msg_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Message Received", None));
        self.save_configuration_btn.setText(QCoreApplication.translate("MainWindow", u"Save Configuration", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Acceleration:", None))
        self.update_tpi_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.update_ki_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Upper Limit:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Velocity:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Deceleration:", None))
        self.update_acceleration_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"KP:", None))
        self.update_kd_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.stage_type_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear", None))
        self.stage_type_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Rotory", None))
        self.stage_type_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Goniometer", None))

        self.drive_check_box.setText(QCoreApplication.translate("MainWindow", u"Drive Enabled", None))
        self.update_velocity_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.update_error_limit_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Integrator Limit:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Error Limit:", None))
        self.update_ghr_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.limit_behavior_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Report", None))
        self.limit_behavior_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Offset", None))
        self.limit_behavior_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Stop", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"KI:", None))
        self.encoder_check_box.setText(QCoreApplication.translate("MainWindow", u"Encoder Polarity", None))
        self.update_deceleration_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.update_kp_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"KD:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Lower Limit:", None))
        self.echo_check_box.setText(QCoreApplication.translate("MainWindow", u"Echo Enabled", None))
        self.update_upper_limit_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.update_integrator_limit_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.update_lower_limit_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.unit_type_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Encoder Counts", None))
        self.unit_type_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Milimeters", None))
        self.unit_type_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Inches", None))
        self.unit_type_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Radians", None))
        self.unit_type_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Mils", None))

        self.update_cpr_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"GHR:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TPI:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"CPR:", None))
    # retranslateUi

