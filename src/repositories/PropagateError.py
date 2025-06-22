from repositories.Error import Error
import math


class PropagationError(Error):
    __propagationValue = 0.0

    def __init__(self, value, propagationValue):
        super().__init__(value)
        self.__propagationValue = propagationValue

    def setPropagationValue(self, propagationValue):
        if propagationValue is None:
            raise Exception("Manage-Error: Debe ingresar un valor truncado")
        self.__propagationValue = propagationValue

    def getPropagationError(self):
        self._calcError()
        return self._error
    
    def __aproximate(self, x):
        return (x + 0.1) * 3 - 0.3

    def _calcError(self):
        self.setPropagationValue(self.__aproximate(self.__propagationValue))
        self._error = abs(self._value - self.__propagationValue)