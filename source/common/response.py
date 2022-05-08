'''
    This file is used to handle response from server
    The information of a response contains:
        - IP address: send to?
        - Data
        - response ID (...) ~ request ID: which request to response
'''

from data import Data
import global_definition

class Response:
    def __init__(self, address: str, data : Data, request_id: str, send_from = (global_definition.HOST, global_definition.PORT)):
        self.__send_to = address
        self.__data = data
        self.__request_id = request_id
        self.__send_from = send_from
    
    def get_destination_address(self):
        return self.__send_to
    
    def get_data(self):
        return self.__data

    def get_request_id(self):
        return self.__request_id
    
    def get_source_address(self):
        return self.__send_from

    def update(self):
        '''
            @todo: 
                - define a setter method
        '''
        pass

class HandleResponse:
    def __init__(self):
        self.__response_queue = []
    
    def next_response(self):
        if (len(self.__response_queue) == 0):
            return None

        return self.__response_queue.pop(0)

    def push_response(self, response: Response):
        self.__response_queue.append(response)