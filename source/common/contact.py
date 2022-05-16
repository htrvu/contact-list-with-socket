from collections.abc import Sequence
import os

import copy
from common.utils import base64_encode

class Contact:

    LARGE_IMAGE_DIR = '../data/large_image'
    SMALL_IMAGE_DIR = '../data/small_image'

    def __init__(self, id, data: dict):
        self.__id = id
        self.__name = data['name']
        self.__phone_number = data['phone_number']
        self.__email = data['email']

        self.__image = None

        if data['image']:
            if os.path.exists(os.path.join(Contact.SMALL_IMAGE_DIR, data['image'])):
                with open(os.path.join(Contact.SMALL_IMAGE_DIR, data['image']), 'rb') as fp:
                    self.__image = base64_encode(fp.read())
            else:
                self.__image = data['image']
        self.__bio = data['bio']
        
    def to_string(self):
        data = {
            'id' : self.__id,
            'name': self.__name,
            'phone_number': self.__phone_number,
            'email': self.__email,
            'image': self.__image,
            'bio': self.__bio
        }
        
        return str(data)

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_phone_number(self):
        return self.__phone_number
    
    def get_email(self):
        return self.__email

    def get_image(self):
        return self.__image

    def get_bio(self):
        return self.__bio

    def set_id(self, id: str):
        self.__id = id

    def set_name(self, name: str):
        self.__name = name
    
    def set_phone_number(self, phone_number: str):
        self.__phone_number = phone_number
    
    def set_email(self, email: str):
        self.__email = email

    def set_image(self, image: Sequence[str, dict]):
        self.__image = image

    def set_bio(self, bio: str):
        self.__bio = bio

    def copy(self):
        return Contact(self.__id, {
            'name': self.__name,
            'phone_number': self.__phone_number,
            'email': self.__email,
            'image': self.__image,
            'bio': self.__bio
        })
        
