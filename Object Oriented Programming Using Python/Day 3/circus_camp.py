class Parrot:
    __counter = 7000

    def __init__(self, name, color):
        Parrot.__counter += 1
        self.__name = name
        self.__color = color
        self.__unique_number = Parrot.__counter

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_unique_number(self):
        return self.__unique_number
