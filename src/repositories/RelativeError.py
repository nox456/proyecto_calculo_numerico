from AbsoluteError import AbsoluteError


class RelativeError(AbsoluteError):

    __relError = 0.0

    def __init__(self, value, aproxValue):
        super().__init__(value)
        self.setValue(value)
        self.setAproxValue(aproxValue)
        self._errorValue = 0.0

    def setAproxValue(self, value):
        if value is None:
            raise Exception("Manage-Error: El valor aproximado no puede ser None")
        self._aproxValue = value

    def getAproxValue(self): 
        return self._aproxValue
    
    def getErrorValue(self):
        return self._errorValue
    
    def getRelError(self):
        if self.__relError == 0.0:
            self.__calcRelError()
        return self.__relError

    def calcRelError(self):
        super()._calcError()
        if self._value == 0:
            raise Exception("Manage-Error: El valor aproximado no puede ser cero para calcular el error relativo")
        self.__relError = self._errorValue / abs(self._value)
