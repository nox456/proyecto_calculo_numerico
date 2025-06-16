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

    def toDecimal(self):
        if self.__value is None:
            return None
        value = 0
        hexDict = {
            "0": "0",
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "a": "10",
            "b": "11",
            "c": "12",
            "d": "13",
            "e": "14",
            "f": "15"
        }
        if "Decimal" in self.__systems:
            value = int(self.__value)
        elif "Hexadecimal" in self.__systems and "Binario" not in self.__systems:
            for i in range(len(str(self.__value))):
                exponent = len(str(self.__value)) - i - 1
                n = int(hexDict[str(self.__value)[i].lower()])
                value += n * 16 ** exponent
        elif "Binario" in self.__systems:
            for i in range(len(str(self.__value))):
                exponent = len(str(self.__value)) - i - 1
                n = int(str(self.__value)[i])
                value += n * 2 ** exponent
        return value
