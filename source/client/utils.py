'''
    This file is used to define utility functions
'''

import base64
import datetime

def base64_decode(str):
    str = base64.b64decode(str)
    return str.decode('utf-8')

def base64_encode(str):
    return base64.b64encode(str).decode('utf-8')

class text_format:
    HEADER = ['\033[95m', '']
    OKBLUE = ['\033[94m', '']
    OKCYAN = ['\033[96m', '']
    OKGREEN = ['\033[92m', '']
    WARNING = ['\033[93m', 'Warning: ']
    FAIL = ['\033[91m', 'Failed: ']
    ENDC = ['\033[0m', '']
    BOLD = ['\033[1m', '']
    UNDERLINE = ['\033[4m', '']
    NORMAL = ['','']
    DEBUG = ['\033[91m', '[DEBUG]: ']
    CLOSE = ['\033[91m', '']

def print_color(message, option = text_format.NORMAL, end = '\n'):
    print(f'{option[0]}{option[1]}{message} {text_format.ENDC[0]}', end = end)
    
def date_format_str():
    return r"%Y-%m-%d"

def datetime_format_str():
    return r"%Y-%m-%d %H:%M:%S"

def date_today():
    return datetime.datetime.now().strftime(date_format_str())

def datetime_now_str():
    return datetime.datetime.now().strftime(datetime_format_str())

def time_in_range(start: datetime, end: datetime, x: datetime, time_format = datetime_format_str()):
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end