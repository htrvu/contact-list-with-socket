import socket
import sys
import ipaddress

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