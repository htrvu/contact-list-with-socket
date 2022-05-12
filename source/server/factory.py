import sys, os
import socket
import json

sys.path.append('..')

import common.contact as contact

CONTACT_FILE_PATH = '../data/contact_data.json'
LARGE_IMAGE_DIR = '../data/large_image'
SMALL_IMAGE_DIR = '../data/small_image'

contact_list = []

with open(CONTACT_FILE_PATH, 'r') as fp:
    jsvalue = json.load(fp)
    for key in jsvalue:
        contact_list.append(contact.Contact(key, jsvalue[key]))
