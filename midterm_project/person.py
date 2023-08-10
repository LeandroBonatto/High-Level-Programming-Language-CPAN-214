class Person:
    def __init__(self, name, address, phone_num):
        self.__name = name
        self.__address = address
        self.__phone_num = phone_num

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_phone_num(self):
        return self.__phone_num

    def set_phone_num(self, phone_num):
        self.__phone_num = phone_num