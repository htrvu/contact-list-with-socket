LOOP_BACK = '127.0.0.1'
HOST = 'localhost'
PORT = 15215


PACKET_LIMIT_SIZE = 1024 # bytes

def set_host(ip_address):
    global HOST
    HOST = ip_address