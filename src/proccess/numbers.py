from helpers.arrays import appendArray
from validations.files import validateFileLine, validateFileElement
from validations.systems import validatePossibleSystems
import numpy as np
from repositories.FileManager import FileManager
from repositories.NumericSystem import NumericSystem
from repositories.Number import Number
from array import ArrayType


def getNumbers(fileContent: ArrayType[str], manager: FileManager) -> ArrayType[Number]:
    numbers = np.array([])
    for i in range(len(fileContent)):
        line = validateFileLine(fileContent[i], manager)
        if line is not None:
            lineNumbers = line.split("#")
            for i in range(len(lineNumbers)):
                number = validateFileElement(lineNumbers[i], manager)
                numbers = appendArray(numbers, number)
    return numbers


def setSystems(numbers: ArrayType[Number], systemManager: NumericSystem, manager: FileManager) -> None:
    for number in numbers:
        if number.isValid():
            systems = validatePossibleSystems(systemManager, number.getValue(), manager)
            if systems is not None:
                number.setSystems(systems)
