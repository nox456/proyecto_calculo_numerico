from repositories.AbsoluteError import AbsoluteError


class RelativeError(AbsoluteError):

    def __init__(self, value, aproxValue):
        super().__init__(value, aproxValue)

    def getError(self):
        self._calcRelError()
        return self._error

    def _calcRelError(self):
        if self._value == 0:
            raise Exception("Manage-Error: El valor no puede ser cero para calcular el error relativo")
        self._error = super().getAbsError() / abs(self._value)