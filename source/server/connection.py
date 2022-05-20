import socket
from constants import *

def is_still_connected(sock: socket.socket):
    try:
        sock.sendall(b"ping")
    except:
        return False
    return True

class Connection:
    def __init__(self, ip_address = HOST, port = PORT):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            self.server.bind((ip_address, port))
        except:
            raise Exception(f'Could not connect to {ip_address}:{port}')

    def get_socket(self):
        return self.server

    def close(self):
        self.server.close()