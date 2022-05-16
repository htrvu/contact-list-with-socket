from pkg_resources import require
from common.data import Data
import common.global_definition as global_definition

import random


class Request:
    class Type:
        GET = '[__GET__]'
        UPDATE = '[__UPDATE__]'

    def __init__(self, message):

        self.__request_type = str
        self.__request_id = str
        self.__data_type = str
        self.__index = str

        message = Request.parse_message(message)

        self.__request_type = message['request_type']
        self.__request_id = message['request_id']
        self.__data_type = message['data_type']
        self.__index = message['index']

    def create_request(request_type, data_type: str, index, request_id: int = random.randint(0, 1 << 32)):
        if request_type not in [Request.Type.GET, Request.Type.UPDATE]:
            raise ValueError('Request type not correct')

        if data_type not in [Data.Type.SINGLE_ID, Data.Type.BY_BLOCK]:
            raise ValueError('Data type not correct')

        request = Request(f'{request_type} {request_id} {data_type} {index}')
        return request

    def to_string(self):
        return f'{self.__request_type} {self.__request_id} {self.__data_type} {self.__index}'

    def get_index(self):
        return self.__index

    def get_request_id(self):
        return self.__request_id

    def get_request_type(self):
        return self.__request_type

    def get_data_type(self):
        return self.__data_type

    def parse_message(message: str):
        messarray = message.strip().split(' ')
        if (len(messarray) != 4):
            raise Exception('Request wrong format')

        if (messarray[0] not in [Request.Type.GET, Request.Type.UPDATE]):
            raise ValueError('Invalid request type')

        if (messarray[2] not in [Data.Type.BY_BLOCK, Data.Type.SINGLE_ID]):
            raise ValueError('Invalid query request')
 
        return {
            'request_type': messarray[0],
            'request_id': messarray[1],
            'data_type': messarray[2],
            'index': messarray[3] # id is the block id or id of any contact 
        }

class HandleRequest:
    def __init__(self):
        self.__request_queue = []
    
    def next_request(self):
        if (len(self.__request_queue) == 0):
            return None

        return self.__request_queue.pop(0)

    def push_request(self, request: Request):
        self.__request_queue.append(request)