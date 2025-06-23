from repositories.Error import Error


class TruncateError(Error):
    """Representación de un error truncado.

    Attributes:
        value (float): Valor original.
        truncatedValue (float): Valor truncado.
        error (float): Error truncado.
    """
    __truncatedValue = 0.0
    __x = 0.0

    def __init__(self, value: float, truncatedValue: float):
        super().__init__(value)
        self.__truncatedValue = truncatedValue

    def setTruncatedValue(self, truncatedValue: float) -> None:
        """Establece el valor truncado.

        Args:
            truncatedValue (float): Valor truncado.
        """
        if truncatedValue is None:
            raise Exception("Manage-Error: Debe ingresar un valor truncado")
        self.__truncatedValue = truncatedValue

    def getTruncateError(self) -> float:
        """Devuelve el error truncado.

        Returns:
            float: Error truncado.
        """
        self._calcError()
        return self._error

    def _calcError(self) -> None:
        """Calcula el error truncado.

        Returns:
            float: Error truncado.
        """
        self._error = abs(self._value - self.__truncatedValue)
