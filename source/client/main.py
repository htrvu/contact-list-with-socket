import sys

from PyQt5 import QtWidgets

sys.path.append('..')

from client.MainWindow import MainWindow
from client.ConnectDialog import ConnectDialog

client_socket = None

def start_window(my_socket):
    global client_socket
    client_socket = my_socket
    main_window = MainWindow(client_socket)
    main_window.show()


def close_socket(my_socket):
    my_socket.send(b'byebye')
    my_socket.close()
    

if __name__ == "__main__":
    # thread = threading.Thread(target=run_client, args = ())
    # thread.start()
    app = QtWidgets.QApplication(sys.argv)

    connect_dialog = ConnectDialog()
    connect_dialog.signals.connected.connect(start_window)
    connect_dialog.signals.exit.connect(app.exit)

    connect_dialog.show()

    exit_code = app.exec_()
    if client_socket:
        close_socket(client_socket)

    sys.exit(exit_code)
