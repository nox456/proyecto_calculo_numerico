from Error import Error


class AbsoluteError(Error):

    _aproxValue = 0.0
    _errorValue = 0.0

    def __init__(self, value):
        super().__init__(value)
        self.setValue(value)
        self._aproxValue = 0.0
        self._errorValue = 0.0

    def setAproxValue(self, value):
        if value is None:
            raise Exception("Manage-Error: El valor aproximado no puede ser None")
        self._aproxValue = value

    def getAproxValue(self): 
        return self._aproxValue
    
    def getErrorValue(self):
        return self._errorValue

    def _calcError(self):
        self._errorValue = abs(self._value - self._aproxValue)