'''
    This file is used to define global variables and functions

    Code conduct:
        CONSTANT: noun - fully uppercase and each word separated by '_'
'''


LOOP_BACK = '127.0.0.1'
HOST = 'localhost'
PORT = 15215

def set_host(ip_address):
    global HOST
    HOST = ip_address

