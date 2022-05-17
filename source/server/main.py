import connection
import threading

import socket

from common.utils import print_color
from common.utils import text_format
from factory import reply_request
from factory import reply_request

import ast

from server.constants import *


'''
    socket.socket, (ip address, tcp port) = socket.socket()
'''

def serve(conn: socket.socket, addr):
    print_color(f'{addr} connected', text_format.OKGREEN)
    while True:
        if conn.fileno() == -1:
            print_color(f'{addr[0]} connected', text_format.OKBLUE)
            break

        message = conn.recv(PACKET_LIMIT_SIZE)

        if message:
            if message == b'byebye':
                print_color(f'{addr} disconnected', text_format.CLOSE)
                conn.close()
                break
            else:
                message = message.decode('utf-8')
                print(type(message))
                print('[*] DEBUG: ', message)
                message_dict = ast.literal_eval(message)
                print('[DEBUG DICT]: ', message_dict)
                threading.Thread(target = reply_request, args = (conn, message_dict)).start()

def run_server():
    print('[STATUS] initialize server')

    server = connection.Connection(ip_address = HOST, port = PORT)
    socket = server.get_socket()
    socket.listen(100)

    print('[STATUS] listtening...')

    while True:
        conn, addr = socket.accept()
        thread = threading.Thread(target = serve, args = (conn, addr))
        thread.start()


if __name__ == '__main__':
    thread = threading.Thread(target = run_server, args = ())
    thread.start()