import connection
import threading
import time

import socket


import colorama
colorama.init()

from utils import print_color
from utils import text_format
from factory import reply_request
from factory import reply_request

import ast
from constants import *
import app_logging as logging

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
        
        try:
            message = conn.recv(REQUEST_LIMIT_SIZE)
        except socket.error:
            logging.log('[ERROR] Something went wrong, close connection to {addr}')
            print_color(f'Something went wrong, close connection to {addr}', text_format.FAIL)
            conn.close()
            break

        if message:
            if message == b'close_connection':
                print_color(f'{addr} disconnected', text_format.CLOSE)
                logging.log(f'[STATUS] {addr} disconnected')
                conn.close()
                break
            else:
                message = message.decode('utf-8')

                try:
                    message_dict = ast.literal_eval(message)
                except:
                    print_color(f'Request in wrong format.', text_format.FAIL)
                    logging.log(f'Request in wrong format: {message}')
                    continue

                if DEBUGGING:
                    print_color(f'Message as dict: {message_dict}', text_format.DEBUG)

                logging.log(f'[DEBUG] Message as dict: {message_dict}')
                reply_request(conn, message_dict)

def run_server():
    print_color('[STATUS] initialize server', text_format.OKBLUE)
    logging.log('[STATUS] initialize server')

    server = connection.Connection(ip_address = HOST, port = PORT)
    socket = server.get_socket()

    # socket.listten(backlog) - Backlog: The maximum length of the pending connections queue.
    socket.listen(100)

    print_color('[STATUS] listtening...', text_format.OKBLUE)
    logging.log('[STATUS] listtening...')

    while True:
        try:
            conn, addr = socket.accept()
        except KeyboardInterrupt as err:
            break

        thread = threading.Thread(target = serve, args = (conn, addr))
        thread.start()

def save_log(logfile):
    save_log.keep = True
    logging.set_log_file_path(logfile)

    while True:
        if not save_log.keep:
            break
        logging.save()
        time.sleep(5)

    print('break')
    logging.save()
    

if __name__ == '__main__':
    server_thread = threading.Thread(target = run_server, args = ())
    logging_thread = threading.Thread(target = save_log, args = ('./server.log', ))

    server_thread.start()
    logging_thread.start()

    server_thread.join()
    save_log.keep = False
    logging_thread.join()