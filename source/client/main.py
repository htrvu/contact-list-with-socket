import threading
import os, sys
import connection

import time
import select
import datetime

import socket

from common import global_definition
from common.request import Request
from common.data import Data
import json
sample_request = []

sample_request.append(Request.create_request(
    Request.Type.UPDATE,
    Data.Type.SINGLE_ID, 
    'C000003'
))


for req in sample_request:
    print(req.to_string())

import ast
import cv2
import numpy as np


def is_still_connected(sock: socket.socket):
    try:
        sock.sendall(b"ping")
        return True
    except:
        return False

def listen_for_new_message(socket: socket.socket):
    while True:
        header_bstr = socket.recv(4)

        if header_bstr == b'ping':
            continue

        message_len = int.from_bytes(header_bstr, 'little')
        message_len = (message_len + 1023) // 1024
        message_str = ''

        for i in range (message_len):
            message = socket.recv(1024).decode()
            message_str = message_str + message

        jsvalue = json.dumps(message_str)
        print(jsvalue)

def communicate(socket: socket.socket):
    while True:
        message = input()
        if message.lower() == 'q':
            break
        socket.send(message.encode())

def send_request(socket: socket.socket, requets_message, function):
    '''
        Return: status (failed or successfuly)
        Flow: send -> 
    '''

    pass

def receive_response(socket: socket.socket):
    '''
        Return: map response data with request id (failed or successfuly)
    ''' 
    
    pass

def run_client():
    client = connection.Connection(ip_address = global_definition.HOST, port = global_definition.PORT)
    socket = client.get_socket()

    recv = threading.Thread(target = listen_for_new_message, args = (socket, ))
    communicate_thread = threading.Thread(target = communicate, args = (socket, ))

    recv.start()
    communicate_thread.start()

if __name__ == "__main__":
    thread = threading.Thread(target=run_client, args = ())
    thread.start()