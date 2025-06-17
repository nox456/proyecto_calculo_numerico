import numpy as np
# from lib.types import Array
from typing import Any
from array import ArrayType


def appendArray(array: ArrayType[Any], value: Any) -> ArrayType[Any]:
    arrayAux = np.array([None for _ in range(len(array) + 1)])
    for i in range(len(array)):
        arrayAux[i] = array[i]
    arrayAux[len(array)] = value
    return arrayAux


def containsArray(array: ArrayType[Any], value: Any) -> bool:
    for i in range(len(array)):
        if array[i] == value:
            return True
    return False
