import sys

HOST = '0.0.0.0'
PORT = 15215

REQUEST_LIMIT_SIZE = 1024 # bytes

CONTACT_FILE_PATH = 'data/contact_data.json'
LARGE_IMAGE_DIR = 'data/large_image'
SMALL_IMAGE_DIR = 'data/small_image'

DEBUGGING = '-x' in sys.argv