import connection
import threading
import time

import socket

from utils import print_color
from utils import text_format
from factory import reply_request
from factory import reply_request

import ast
from constants import *
import logging

'''
    socket.socket, (ip address, tcp port) = socket.socket()
'''

def serve(conn: socket.socket, addr):
    print_color(f'{addr} connected', text_format.OKGREEN)
    logging.log(f'[STATUS] {addr} connected')
    while True:
        if conn.fileno() == -1:
            print_color(f'{addr[0]} disconnected', text_format.OKBLUE)
            logging.log(f'[STATUS] {addr[0]} disconnected')
            break

        message = conn.recv(PACKET_LIMIT_SIZE)

        if message:
            if message == b'byebye':
                print_color(f'{addr} disconnected', text_format.CLOSE)
                logging.log(f'[STATUS] {addr} disconnected')
                conn.close()
                break
            else:
                message = message.decode('utf-8')
                message_dict = ast.literal_eval(message)

                if DEBUGGING:
                    print_color(f'Message as dict: {message_dict}', text_format.DEBUG)

                logging.log(f'[DEBUG] Message as dict: {message_dict}')
                threading.Thread(target = reply_request, args = (conn, message_dict)).start()

def run_server():
    print('[STATUS] initialize server')
    logging.log('[STATUS] initialize server')

    server = connection.Connection(ip_address = HOST, port = PORT)
    socket = server.get_socket()
    socket.listen(100)

    print('[STATUS] listtening...')
    logging.log('[STATUS] listtening...')

    while True:
        conn, addr = socket.accept()
        thread = threading.Thread(target = serve, args = (conn, addr))
        thread.start()

def save_log(logfile):
    logging.set_log_file_path(logfile)

    while True:
        logging.save()
        time.sleep(5)

if __name__ == '__main__':
    server_thread = threading.Thread(target = run_server, args = ())
    server_thread.start()
    logging_thread = threading.Thread(target = save_log, args = ('./server.log', ))
    logging_thread.start()