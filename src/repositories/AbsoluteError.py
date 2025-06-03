from repositories.Error import Error


class AbsoluteError(Error):

    _aproxValue = 0.0

    def __init__(self, value, aproxValue):
        super().__init__(value)
        self._aproxValue = aproxValue

    def setAproxValue(self, aproxValue):
        if aproxValue is None:
            raise Exception("Manage-Error: Debe ingresar un valor aproximado")
        self._aproxValue = aproxValue

    def getAproxValue(self):
        return self._aproxValue

    def getAbsError(self):
        self._calcAbsError()
        return self._error

    def _calcAbsError(self):
        self._error = abs(self._value - self._aproxValue)