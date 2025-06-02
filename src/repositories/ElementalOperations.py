import numpy as np

class ElementalOperations:

    __number = "0"
    __base = np.array([])

    def __init__(self, number = "0", base = np.array([])):
        if len(number) == 0:
            raise Exception("Manage-Error: El numero no puede estar vacio")
        self.__number = self.__utilNumber(number)
        self.__base = base

    # Setters and Getters
    def setNumber(self, number):
        if len(number) == 0:
            raise Exception("Manage-Error: El numero no puede estar vacio")
        self.__number = self.__utilNumber(number)

    def getNumber(self):
        return self.__number
    
    def setBase(self, base):
        if len(base) == 0:
            raise Exception("Manage-Error: La base no puede estar vacia")
        self.__base = base

    def getBase(self):
        return self.__base

    # Utilitarias

    
    def __getOperations(self):
        for operation in self.__base:
            if operation == "Decimal":
                pass
            elif operation == "Binario":
                pass
            elif operation == "Hexadecimal":
                pass
            else:
                raise Exception("Manage-Error: Operacion no valida")
            


    def decimalOperation(self, number):
        


    def __utilNumber(self, number):
        chars_allowed = "0123456789ABCDEF.,"
        for char in number:
            if char.upper() not in chars_allowed:
                raise Exception(
                    "Manage-Error: El numero ingresado no es valido")
        if number.startswith((".", ",")) or number.endswith((".", ",")):
            raise Exception(
                "Manage-Error: El numero ingresado no es valido")
        separatorCount = number.count(".") + number.count(",")
        if separatorCount > 1:
            raise Exception(
                "Manage-Error: El numero ingresado no es valido")
        if number == "0":
            return "0"
        else:
            return number.lstrip("0")