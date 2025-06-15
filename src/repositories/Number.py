import numpy as np


class Number:
    __value = ""
    __isValid = False
    __systems = np.array([])
    __sigFigs = 0
    __ops = 0

    def __init__(self, value, validate=True):
        self.__value = self.__utilValue(value) if validate else value
        self.__systems = np.array([])
        self.__sigFigs = 0
        self.__ops = 0

    def isValid(self):
        return self.__isValid

    def getValue(self):
        return self.__value

    def setSystems(self, systems):
        self.__systems = systems

    def getSystems(self):
        return self.__systems

    def setFigs(self, Figs):
        self.__sigFigs = Figs

    def getFigs(self):
        return self.__sigFigs

    def __utilValue(self, value):
        chars_allowed = "0123456789ABCDEF.,"
        for char in value:
            if char.upper() not in chars_allowed:
                raise Exception(
                    f"Manage-Error: El numero {value} ingresado no es valido")
        if value.startswith((".", ",")) or value.endswith((".", ",")):
            raise Exception(
                f"Manage-Error: El numero {value} ingresado no es valido")
        separatorCount = value.count(".") + value.count(",")
        if separatorCount > 1:
            raise Exception(
                f"Manage-Error: El numero {value} ingresado no es valido")
        self.__isValid = True
        return value
