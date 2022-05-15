'''
    This file is used to define utility functions
'''

def image_to_bytes(path):
    with open(path, "rb") as image:
        f = image.read()
        b = bytearray(f)
        return b