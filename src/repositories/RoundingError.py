from repositories.Error import Error


class RoundingError(Error):
    __roundedValue = 0.0

    def __init__(self, value, roundedValue):
        super().__init__(value)
        self.__roundedValue = roundedValue

    def getRoundingError(self):
        self._calcError()
        return self._error

    def _calcError(self):
        self._error = abs(self._value - self.__roundedValue)