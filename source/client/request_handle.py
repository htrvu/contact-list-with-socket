import socket
from common.utils import print_color, text_format
import ast
from common.request_type import RequestType

from client.constants import *


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
        appsocket.send(request)
    except Exception as err:
        print_color(str(err), text_format.FAIL)
        return None

    response_data = None
    while True:
        try:
            response_header = appsocket.recv(4)
            
            if response_header == b'ping':
                continue
            
            response_len = int.from_bytes(response_header, 'little')
            print('[DEBUG]: bytes len =' , response_len)

            response_bytes = b''
            cur_len = 0
            while True:
                try:
                    part = appsocket.recv(min(BYTES_PER_BLOCK, response_len - cur_len))
                    response_bytes += part
                    cur_len += len(part)

                    if cur_len == response_len:
                        break
                except Exception as e:
                    pass

            response_str = response_bytes.decode('utf-8')
            print('[DEBUG]: actual len=', len(response_str))

            response_data = ast.literal_eval(response_str)

            break
        except Exception as e:
            return # do something

    return response_data
