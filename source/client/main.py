import sys
import time

import threading

from PyQt5 import QtWidgets

from MainWindow import MainWindow
from ConnectDialog import ConnectDialog
import logging

def start_window(my_socket):
    main_window = MainWindow(my_socket)
    main_window.show()

def logging_thread(log_file_path):
    logging.set_log_file_path(log_file_path)
    while True:
        logging.save()
        time.sleep(5)

if __name__ == "__main__":

    save_log_thread = threading.Thread(target = logging_thread, args = ('./client.log', ))
    save_log_thread.start()

    app = QtWidgets.QApplication(sys.argv)

    connect_dialog = ConnectDialog()
    connect_dialog.signals.connected.connect(start_window)
    connect_dialog.signals.exit.connect(app.exit)

    connect_dialog.show()

    exit_code = app.exec_()
    sys.exit(exit_code)
