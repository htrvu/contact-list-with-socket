import threading
import os, sys
import connection

import time
import select
import datetime

import socket

sys.path.append('..')
import common.global_definition as global_definition


def listen_for_new_message(socket: socket.socket):
    while True:
        # 1 gói max 1bytes
        # 4 bytes - total
        # 
        message = socket.recv(1024).decode()
        print('[STATUS]: ', message)

def communicate(socket: socket.socket):
    while True:
        message = input()
        if message.lower() == 'q':
            break
        date_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = str(date_now) + ' ' + message
        socket.send(message.encode())

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