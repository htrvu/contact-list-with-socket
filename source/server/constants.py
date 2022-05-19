import sys

HOST = '0.0.0.0'
PORT = 15215

PACKET_LIMIT_SIZE = 512 # bytes
BYTES_PER_BLOCK = 4096

CONTACT_FILE_PATH = 'data/contact_data.json'
LARGE_IMAGE_DIR = 'data/large_image'
SMALL_IMAGE_DIR = 'data/small_image'

DEBUGGING = '-x' in sys.argv