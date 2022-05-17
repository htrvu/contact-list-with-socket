LOOP_BACK = '127.0.0.1'
# HOST = 'localhost'
HOST = '10.0.159.89'
PORT = 15215

PACKET_LIMIT_SIZE = 512 # bytes

def set_host(ip_address):
    global HOST
    HOST = ip_address