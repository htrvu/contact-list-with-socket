import socket
import sys, os
import ipaddress

sys.path.append('..')

import common.global_definition as global_definition

def is_valid_ip_address(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)
    except ValueError:
        return False
    return True

class Connection:
    def __init__(self, ip_address = global_definition.HOST, port = global_definition.PORT):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            self.server.bind((ip_address, port))
        except:
            raise Exception(f'Could not connect to {ip_address}:{port}')

    def get_socket(self):
        return self.server

    def close(self):
        self.server.close()