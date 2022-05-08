'''
    This file is used to handle request from client
    The information of a request contains:
        - IP address: send from?
        - Request ID (...)
        - Reqetst for what [id, block]?
        - Value of id or block
    
    Sample: "[__GET__] 123123 [__SINGLE_ID__] U000001"
'''

import global_definition
from data import Data

class Request:
    class Type:
        GET = '[__GET__]'
        UPDATE = '[__UPDATE__]' # ... 

    def __init__(self, send_from, message, send_to = (global_definition.HOST, global_definition.PORT)):
        message = Request.parse_message(message)
        
        self.__request_type = message['request_type']
        self.__request_id = message['request_id']
        self.__data_type = message['data_type']
        self.__index = message['index']

        self._source_address = send_from
        self._destination_address = send_to


    def get_request_type(self):
        return self.__request_type

    def get_data_type(self):
        return self.__data_type

    def get_source_address(self):
        return self.__source_address
    
    def get_destination_address(self):
        return self.__destination_address

    def parse_message(message: str):
        messarray = message.strip().split(' ')

        if (len(messarray)):
            raise Exception('Request wrong format')

        if (messarray[0] not in [Request.Type.GET, Request.Type.UPDATE]):
            raise ValueError('Invalid request type')

        if (message[1] not in [Data.Type.BY_BLOCK, Data.Type.SINGLE_ID]):
            raise ValueError('Invalid query request')
 
        return {
            'request_type': messarray[0],
            'request_id': message[1],
            'data_type': messarray[2],
            'index': int(message[3]) # id is the block id or id of any contact 
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
