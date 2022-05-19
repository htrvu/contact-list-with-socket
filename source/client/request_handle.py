import socket
from utils import print_color, text_format
import ast
from request_type import RequestType

from constants import *
import logging


def create_block_request(block_id):
    return {
        'dtype': RequestType.BLOCK,
        'block_id': block_id
    }

def create_single_id_request(id):
    return {
        'dtype': RequestType.SINGLE_ID,
        'id': id
    }


def request_to_server(appsocket: socket.socket, request: dict):
    request = str(request).encode()
    
    try:
        appsocket.sendall(request)
    except socket.error as err:
        print_color(str(err), text_format.FAIL)
        logging.log(f'[ERROR] Exception raised when sending request to server: {err}' )
        return None

    response_data = None

    while True:
        try:
            response_header = appsocket.recv(4)
            
            if response_header == b'ping':
                continue
            
            response_len = int.from_bytes(response_header, 'little')
            print_color(f'Packet received size: {response_len} (bytes)', text_format.OKGREEN)
            logging.log(f'[STATUS] Packet received size: {response_len} (bytes)' )

            response_bytes = b''
            cur_len = 0
            while True:
                try:
                    part = appsocket.recv(min(BYTES_PER_BLOCK, response_len - cur_len))
                    response_bytes += part
                    cur_len += len(part)

                    if cur_len == response_len:
                        break

                except socket.timeout as err:
                    print_color(str(err), text_format.FAIL)
                    logging.log(f'[ERROR] Exception raised when receiving response from server: {err}' )
                    break

            response_str = response_bytes.decode('utf-8')
            response_data = ast.literal_eval(response_str)
            break
        except socket.error as err:
            print_color(str(err), text_format.FAIL)
            logging.log(f'[ERROR] Exception raised when receiving response from server: {err}' )

    return response_data
