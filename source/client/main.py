import threading
import os, sys
import connection

import time
import select
import datetime

import socket

from common import global_definition
import json

def request_to_server(appsocket: socket.socket, request: dict):
    request = str(request).encode()
    
    try:
        socket.send(request)
    except socket.timeout:
        pass

    BYTES_PER_BLOCK = 1024
    
    response_data = None

    while True:
        try:
            response_header = appsocket.recv(4)
            
            if response_header == b'ping':
                continue
            
            response_len = int.from_bytes(response_header, 'little')
            message_block_count = (response_len + BYTES_PER_BLOCK - 1) // BYTES_PER_BLOCK

            response_data_str = ''

            for i in range(message_block_count):
                response_data = response_data + appsocket.recv(BYTES_PER_BLOCK).decode('utf-8')

            response_data = json.loads(response_data_str)

            break
        except socket.timeout:
            pass # do something

    return response_data

if __name__ == "__main__":
    print('hehe')