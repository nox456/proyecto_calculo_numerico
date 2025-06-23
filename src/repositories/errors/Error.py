class Error:
    _error = 0.0
    _value = 0.0

    def __init__(self, value):
        if value is None:
            raise Exception("Manage-Error: Debe ingresar un valor")
        self._value = value

    def setValue(self, value):
        if value is None:
            raise Exception("Manage-Error: Debe ingresar un valor")
        self._value = value

    def getValue(self):
        return self._value

    def getError(self):
        self._calcError()
        return self._error

    def _calcError(self):
        pass