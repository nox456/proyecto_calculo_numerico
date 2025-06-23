from array import ArrayType
import numpy as np
from helpers.arrays import appendArray
from validations.selector import validateSelector
from validations.files import validateFormula
from repositories.FileManager import FileManager
from repositories.Formula import Formula
import math


def checkIsMatrix(fileManager: FileManager) -> bool:
    print("Tipos de datos:")
    print("- 1. Matrices")
    print("- 2. Numeros")
    choice = validateSelector(1, 2, "Elija el tipo de dato a usar (1-2): ", fileManager)
    return True if choice == 1 else False


def getFormulas(fileContent: ArrayType[str], manager: FileManager, isMatrix: bool, triosCount: int) -> ArrayType[Formula]:
    formulas = np.array([])
    for i in range(len(fileContent)):
        for j in range(math.ceil(triosCount / 3)):
            formula = validateFormula(fileContent[i], manager, isMatrix)
            formulas = appendArray(formulas, formula)
    return formulas
