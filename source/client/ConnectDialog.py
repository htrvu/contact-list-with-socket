from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox

import socket
import sys

sys.path.append('..')

from client.ui_connectdialog import Ui_ConnectDialog
from client.components.my_messagebox import MyMessageBox

from client.connection import Connection

class ConnectSignals(QObject):
    connected = pyqtSignal(socket.socket)
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
        port = int(self.ui.hostPort.text())

        try:
            conn = Connection(host, port)
            my_socket = conn.get_socket()
            self.signals.connected.emit(my_socket)
            self.close()
        except:
            self.__show_error_msg('Could not connect to server')

    def __exit_btn_clicked(self):
        self.signals.exit.emit()
        self.close()

    def __show_error_msg(self, msg):
        MyMessageBox(msg, self).exec_()

