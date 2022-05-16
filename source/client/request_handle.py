import socket
from common.utils import print_color, text_format
import ast
from common.request import RequestType

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

    BYTES_PER_BLOCK = 1024
    
    response_data = None

    while True:
        try:
            response_header = appsocket.recv(4)
            
            if response_header == b'ping':
                continue
            
            response_len = int.from_bytes(response_header, 'little')
            print('[DEBUG]: ' , response_len)

            message_block_count = (response_len + BYTES_PER_BLOCK - 1) // BYTES_PER_BLOCK

            response_data_str = ''
            mess = ''
            for i in range(message_block_count):
                try:
                    mess = appsocket.recv(BYTES_PER_BLOCK).decode('utf-8')
                    response_data_str = response_data_str + mess
                except Exception as e:
                    pass
            
            # print(response_data_str[-100:])
            response_data = ast.literal_eval(response_data_str)
            break
        except Exception as e:
            return # do something

    return response_data
