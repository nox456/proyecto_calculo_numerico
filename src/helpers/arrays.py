import numpy as np


def appendArray(array, value):
    arrayAux = np.array([None for _ in range(len(array) + 1)])
    for i in range(len(array)):
        arrayAux[i] = array[i]
    arrayAux[len(array)] = value
    return arrayAux
