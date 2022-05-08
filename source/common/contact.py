class Contact:
    def __init__(self, id, data: dict):
        self.__id = id
        self.__name = data['name']
        self.__phone_number = data['phone_number']
        self.__email = data['email']
        self.__image = data['image']
        self.__bio = data['bio']

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

    def set_image(self, image: str):
        self.__image = image

    def set_bio(self, bio: str):
        self.__bio = bio
