from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal, QObject, QThread
from PyQt5.QtWidgets import QMessageBox

import socket
import sys

from ui_connectdialog import Ui_ConnectDialog
from components.my_messagebox import MyMessageBox

from connection import Connection, ConnectRunner

from components.my_dialog import MyDialog

import logging

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

    def __connect_threading(self, host, port):
        self.__dialog = MyDialog('Message', 'Connecting...', self)
        self.__dialog.show()

        self.__thread = QThread()
        self.__target = ConnectRunner(host, port)
        self.__target.moveToThread(self.__thread)

        self.__thread.started.connect(self.__target.run)

        self.__target.finished.connect(self.__thread.quit)
        self.__target.ok.connect(self.__show_connect_msg)
        self.__target.fail.connect(lambda: self.__show_connect_msg(None))

        # Step 6: Start the thread
        self.__thread.start()

    def __connect_btn_clicked(self):
        host = self.ui.hostIP.text()
        port_str = self.ui.hostPort.text()

        if not host or not port_str:
            self.__show_error_msg('Please enter host IP and port!')
            logging.log(f'[ERROR] Wrong ip address: {host}')
            return

        if not port_str.isdigit():
            self.__show_error_msg('Port must be a number!')
            logging.log(f'[ERROR] Wrong port: {port_str}')
            return

        port = int(port_str)

        self.__connect_threading(host, port)

    def __exit_btn_clicked(self):
        self.signals.exit.emit()
        self.close()

    def __show_connect_msg(self, result):
        self.__dialog.close()

        if result is not None:
            self.signals.connected.emit(result)
            self.close()
        else:
            self.__show_error_msg('Could not connect to server!')
            logging.log('Could not connect to server')
            return

    def __show_error_msg(self, msg):
        MyMessageBox(msg, [], self).exec_()

