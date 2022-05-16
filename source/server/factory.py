import sys, os
import socket
import json

sys.path.append('..')

from common.contact import Contact
from common.request import Request
from common.response import Response
from common.data import Data


CONTACT_FILE_PATH = '../data/contact_data.json'
LARGE_IMAGE_DIR = '../data/large_image'
SMALL_IMAGE_DIR = '../data/small_image'

contact_list = []
contact_dict = {}

with open(CONTACT_FILE_PATH, 'r') as fp:
    jsvalue = json.load(fp)
    for key in jsvalue:
        contact_list.append(Contact(key, jsvalue[key]))
        contact_dict[key] = Contact(key, jsvalue[key])

def parse_small_image(contact: Contact):
    ret_contact = contact.copy()
    
    print(contact.get_name())

    image = {
        'small_image': open(os.path.join(SMALL_IMAGE_DIR, contact.get_image()), 'rb').read()
    }

    ret_contact.set_image(image)

    return ret_contact

def parse_large_image(contact: Contact):
    ret_contact = contact
    
    image = {
        'large_image': open(os.path.join(LARGE_IMAGE_DIR, contact.get_image()), 'rb').read()
    }

    ret_contact.set_image(image)

    return ret_contact

def parse_image(contact: Contact):
    ret_contact = contact

    image = {
        'small_image': open(os.path.join(SMALL_IMAGE_DIR, contact.get_image()), 'rb').read(),
        'large_image': open(os.path.join(LARGE_IMAGE_DIR, contact.get_image()), 'rb').read()
    }

    ret_contact.set_image(image)

    return ret_contact

def reply_request(socket: socket.socket, request: Request):
    contact = None
    if (request.get_data_type() == Data.Type.SINGLE_ID):
        contact = contact_dict[request.get_index()]

    _contact = contact.copy()
    print(_contact.to_string())
    
    message_len = len(_contact.to_string().encode())
    message_len = message_len.to_bytes(4, 'little')
    
    socket.send(message_len)
    socket.send(_contact.to_string().encode())
    print('Message length: ', len(_contact.to_string().encode()))