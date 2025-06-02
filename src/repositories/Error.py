class Error:

    _value = 0.0

    def __init__(self, value):
        if value is None:
            raise Exception("Manage-Error: El valor no puede ser None")
        self._value = value
    
    def setValue(self, value):
        if value is None:
            raise Exception("Manage-Error: El valor no puede ser None")
        self._value = value

    def getValue(self):
        return self._value
        
    def _calcError(self):
        pass