import sys
import time

import threading

from PyQt5 import QtWidgets

from MainWindow import MainWindow
from ConnectDialog import ConnectDialog
import app_logging as logging
from utils import print_color, text_format

def start_window(my_socket):
    save_log_thread = threading.Thread(target = logging_thread, args = ('./client.log', ))
    save_log_thread.start()
    main_window = MainWindow(my_socket)
    main_window.show()

def logging_thread(log_file_path):
    logging_thread.keep = True
    logging.set_log_file_path(log_file_path)
    
    while True:
        if not logging_thread.keep:
            break

        logging.save()
        time.sleep(5)
    
    print_color('Wait for a few seconds to completly save the log...', text_format.OKCYAN)
    logging.save()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    connect_dialog = ConnectDialog()
    connect_dialog.signals.connected.connect(start_window)
    connect_dialog.signals.exit.connect(app.exit)

    connect_dialog.show()

    exit_code = app.exec_()

    logging_thread.keep = False
    sys.exit(exit_code)
