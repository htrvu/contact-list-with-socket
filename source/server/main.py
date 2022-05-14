from itertools import count
import sys, os
import connection
import threading
import time
import select

import socket

sys.path.append('..')

import common.global_definition as global_definition


# check timeout

def serve(conn: socket.socket, addr):
    print(f'{addr[0]} connected')

    while True:
        try:
            message = conn.recv(2048).decode()
            if message:
                print(f'[{addr[0]}]: {message}')
                conn.send('Message received'.encode())
            else:
                print(f'[{addr[0]} disconnected]')
                remove_connection(conn)
        except:
            continue
        time.sleep(0.1)

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

    while True:
        print('[STATUS] listtening...')
        conn, addr = socket.accept()
        list_of_client.append(conn)

        print(type(conn))

        thread = threading.Thread(target = serve, args = (conn, addr))
        thread.start()
        time.sleep(1)

if __name__ == '__main__':
    thread = threading.Thread(target = run_server, args = ())
    thread.start()