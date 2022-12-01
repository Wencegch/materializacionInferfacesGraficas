class Persona:
    def __init__(self, nombre="", apellido="", direccion="", edad = 0):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def __str__(self):
        return self.__nombre + ", " + self.__apellido + ", "  + self.__direccion + ", " + str(self.__edad) + " años"