from itertools import count
from re import I
import sys, os
import connection
import threading
import time
import select

import socket

import signal

from common import global_definition
from common.request import Request
from common.utils import print_color
from common.utils import text_format
from factory import reply_request
from ast import literal_eval
from factory import reply_request

'''
    socket.socket, (ip address, tcp port) = socket.socket()
'''

list_of_client = []


def serve(conn: socket.socket, addr):
    print_color(f'{addr[0]} connected', text_format.OKGREEN)

    while True:
        try:
            if conn.fileno() == -1:
                print_color(f'{addr[0]} connected', text_format.OKBLUE)
                break
            
            message = conn.recv(global_definition.PACKET_LIMIT_SIZE).decode('utf-8')
            message_dict = literal_eval(message)
            threading.thread(target = reply_request, args = (socket, message_dict)).start()
        except socket.error as err:
            print_color(str(err), text_format.FAIL)

def run_server():
    server = connection.Connection(ip_address = global_definition.HOST, port = global_definition.PORT)
    socket = server.get_socket()
    socket.listen(100)

    print('[STATUS] initialize server')

    global list_of_client
    global cnt

    cnt = 0
    list_of_client = []

    print('[STATUS] listtening...')
    while True:    
        conn, addr = socket.accept()
        thread = threading.Thread(target = serve, args = (conn, addr))
        thread.start()

if __name__ == '__main__':
    thread = threading.Thread(target = run_server, args = ())
    thread.start()