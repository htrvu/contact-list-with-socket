import sys, os
import socket
import json

sys.path.append('..')

from common.request_type import RequestType
from common.utils import base64_encode
from common.utils import print_color, text_format
from connection import is_still_connected

from server.constants import *


contact_list = []
contact_dict = {}

with open(CONTACT_FILE_PATH, 'r') as fp:
    jsvalue = json.load(fp)

    for key in jsvalue:
        small_image_b64 = None
        large_image_b64 = None

        small_image_path = os.path.join(SMALL_IMAGE_DIR, jsvalue[key]['image'])
        large_image_Path = os.path.join(LARGE_IMAGE_DIR, jsvalue[key]['image'])

        if os.path.exists(small_image_path):
            with open(small_image_path, 'rb') as fp:
                small_image_b64 = base64_encode(fp.read())

        if os.path.exists(large_image_Path):
            with open(large_image_Path, 'rb') as fp:
                large_image_b64 = base64_encode(fp.read())

        mini_contact = {
            'id': key,
            'name': jsvalue[key]['name'],
            'image': small_image_b64
        }

        full_contact = {
            'id': key,
            'name': jsvalue[key]['name'],
            'image': large_image_b64,
            'phone_number': jsvalue[key]['phone_number'],
            'email': jsvalue[key]['email'],
            'bio': jsvalue[key]['bio']
        }

        contact_list.append(mini_contact)
        contact_dict[key] = full_contact

def create_response(request: dict):
    response_data = None

    if request['dtype'] == RequestType.BLOCK:
        block_id = request['block_id']
        
        if block_id == -1:
            response_data = {
                'status': 'ok',
                'dtype' : 'block',
                'block_id': block_id,
                'data': contact_list
            }
        elif block_id >= 0:
            blocksize = RequestType.BLOCK_SIZE
            left = block_id * blocksize
            right = min(left + blocksize, len(contact_list))

            if left < right:
                data = contact_list[left:right]
            else:
                data = []

            response_data = {
                'status': 'ok',
                'dtype' : 'block',
                'block_id': block_id,
                'data': data
            }

    elif request['dtype'] == RequestType.SINGLE_ID:
        id = request['id']
        if id in contact_dict:
            response_data = {
                'status': 'ok',
                'dtype': RequestType.SINGLE_ID,
                'data': contact_dict[id]
            }
        else:
            response_data = {
                'status': f'{id} not found in contact list'
            }
    else:
        raise Exception('Invalid request type')
    
    return response_data

def reply_request(appsocket: socket.socket, request: dict):
    message_to_send = str(create_response(request)).encode()
    message_len = len(message_to_send).to_bytes(4, 'little')

    try:
        if not is_still_connected(appsocket):
            appsocket.close()
            return
        
        appsocket.sendall(message_len)
        appsocket.sendall(message_to_send)
        print_color(f'Packet sent to {appsocket.getpeername()}', text_format.OKGREEN)
    except Exception as err:
        print_color(err, text_format.FAIL)