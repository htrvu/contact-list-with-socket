from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox

import socket
import sys

sys.path.append('..')

from client.ui_connectdialog import Ui_ConnectDialog
from client.components.my_messagebox import MyMessageBox


class ConnectSignals(QObject):
    # connected = pyqtSignal(socket.socket)
    connected = pyqtSignal(str)
    exit = pyqtSignal()


class ConnectDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ConnectDialog, self).__init__(parent)
        self.ui = Ui_ConnectDialog()
        self.ui.setupUi(self)

        self.setWindowTitle('Connect to Server')
        self.setWindowIcon(QtGui.QIcon('./assets/icons/contact.png'))

        self.signals = ConnectSignals()

        self.ui.connectBtn.clicked.connect(self.__connect_btn_clicked)
        self.ui.exitBtn.clicked.connect(self.__exit_btn_clicked)

        # self.show()

    def __connect_btn_clicked(self):
        host = self.ui.hostIP.text()
        port = self.ui.hostPort.text()

        # make connection
        # if thanh cong:
        # ...
        # else:
            # bao loi

        # jus demo
        if host != '127.0.0.1':
            self.__show_error_msg('Can\'t connect to Server!')
        else:
            self.signals.connected.emit(host + '_' + port)
            self.close()

    def __exit_btn_clicked(self):
        self.signals.exit.emit()
        self.close()

    def __show_error_msg(self, msg):
        # qmessagebox for msg
        msg_box = MyMessageBox(self)        
        msg_box.setStyleSheet("QMessageBox {background-color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #acb6e5,  stop:1 #86fde8); } QLabel {color: #2d1299; font-size: 20px; font-weight: bold;}")

        btn = msg_box.addButton(MyMessageBox.Ok)
        btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        btn.setStyleSheet('''
QPushButton {
	background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #2d1299,  stop:1 #2980b9);
	padding: 4px 16px;
	font-size: 18px;
    font-weight: bold;
	color: #fff;
	border: none;
	border-radius: 12px;
	outline: none;
}

QPushButton:hover {
	background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #8e2de2,  stop:1 #4a00e0);
}
        ''')
        
        msg_box.setText(msg)
        msg_box.setWindowTitle('Error Message')
        msg_box.setWindowIcon(QtGui.QIcon('./assets/icons/contact.png'))
        msg_box.exec_()

