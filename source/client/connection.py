from http.client import PROXY_AUTHENTICATION_REQUIRED
import socket
import sys
import ipaddress

from PyQt5.QtCore import QObject, pyqtSignal

sys.path.append('..')

def is_valid_ip_address(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)
    except ValueError:
        return False
    return True

class Connection:
    def __init__(self, ip_address: str, port: int):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            self.client.connect((ip_address, port))
        except:
            raise Exception(f'Could not connect to {ip_address}:{port}')

        self.client.settimeout(5)

    def get_socket(self):
        return self.client

    def close(self):
        self.client.close()


class ConnectRunner(QObject):
    ok = pyqtSignal(socket.socket)
    fail = pyqtSignal()
    finished = pyqtSignal()

    def __init__(self, host, port):
        super(ConnectRunner, self).__init__()
        self.__host = host
        self.__port = port

    def run(self):
        try:
            conn = Connection(self.__host, self.__port)
            self.socket = conn.get_socket()
            self.ok.emit(self.socket)
        except:
            self.fail.emit()
        self.finished.emit()


class ReconnectRunner(QObject):
    ok = pyqtSignal()
    fail = pyqtSignal()
    finished = pyqtSignal()

    def __init__(self, socket, host, port):
        super(ReconnectRunner, self).__init__()
        self.__socket = socket
        self.__host = host
        self.__port = port        

    def run(self):
        try:
            self.__socket.connect((self.__host, self.__port))
            self.ok.emit()
        except:
            self.fail.emit()
        self.finished.emit()
