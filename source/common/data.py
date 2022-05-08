'''
    This file is used to define data structure to communicate on this app

    Format:
        sigle contact: 
            usr_id: {
                name: str,
                phone_number: str,
                email_address: str,
                image_path: str,
                bio: str
            }


        block of contacts:
            block_id: id (int),
            block_data: {
                single_contact_1,
                single_contact_2,
                single_contact_3
                ...
            }
        
        full list of contact have the same type with block of contacts with block_id = -1
'''

class Data:
    BLOCK_SIZE = 5 # contacts per block

    class Type:
        SINGLE_ID = '[__SINGLE_ID__]'
        BY_BLOCK = '[__BY_BLOCK__]'

    def __init__(self, type: Type, data: dict):
        self.__data = {}
        self.update_data(type, data)

    def dumps(data: str):
        '''
            @todo:
                - parse the data from string
                - return a Data object
        '''
        pass

    def valid_data(type: Type, data: dict):
        '''
            Validation the data, make sure that the data is in correct format

            @todo
                - check valid image image path
                - check data format (check by type)
        '''
        return True

    def get_type(self):
        return self.__data['type']
    
    def get_data(self):
        return self.__data['data']

    def update_data(self, type: Type, data: dict):
        if (Data.valid_data(type, data)):
            self.__data = {
                'type' : type,
                'data' : data
            }
        else:
            raise Exception('Invalid data type')