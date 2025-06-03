from repositories.Error import Error
import math


class TruncateError(Error):
    __truncatedValue = 0.0
    __x = 0.0
    

    def __init__(self, value, truncatedValue):
        super().__init__(value)
        self.__truncatedValue = truncatedValue

    def setTruncatedValue(self, truncatedValue):
        if truncatedValue is None:
            raise Exception("Manage-Error: Debe ingresar un valor truncado")
        self.__truncatedValue = truncatedValue

    def getTruncateError(self):
        self._calcError()
        return self._error
    
    # def aproximate(self, x, n):
    #     sum = 0.0
    #     for i in range(n):
    #         sum += (-1)**i * (x**(2*i)) / math.factorial((2*i))
    #     return sum

    def _calcError(self):
        self._error = abs(self._value - self.__truncatedValue)