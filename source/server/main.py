from itertools import count
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

'''
    socket.socket, (ip address, tcp port) = socket.socket()
'''

list_of_client = []

def is_still_connected(sock: socket.socket):
    try:
        sock.sendall(b"ping")
        return True
    except:
        return False

def serve(conn: socket.socket, addr):
    print_color(f'{addr[0]} connected', text_format.OKGREEN)
    while True:
        try:
            if is_still_connected(conn) == False:
                print_color(f'{addr[0]} diconnected', text_format.FAIL)
                return
            
            message = conn.recv(global_definition.PACKET_LIMIT_SIZE).decode()
            request = None

            try:
                request = Request(message = message)
            except Exception as e:
                request = None
                print(e)

            if request != None:
                print(request.to_string())
                reply_thread = threading.Thread(target = reply_request, args = (conn, request))
                reply_thread.start()
        except:
            pass

def remove_connection(conn):
    global list_of_client
    if conn in list_of_client:
        conn.close()
        list_of_client.remove(conn)

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