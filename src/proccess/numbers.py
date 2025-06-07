from helpers.arrays import appendArray
from validations.files import validateFileLine, validateFileElement
from validations.systems import validatePossibleSystems
import numpy as np


def getNumbers(fileContent, manager):
    numbers = np.array([])
    for i in range(len(fileContent)):
        line = validateFileLine(fileContent[i], manager)
        if line is not None:
            lineNumbers = line.split("#")
            for i in range(len(lineNumbers)):
                number = validateFileElement(lineNumbers[i], manager)
                numbers = appendArray(numbers, number)
    return numbers


def setSystems(numbers, systemManager, manager):
    for number in numbers:
        if number.isValid():
            systems = validatePossibleSystems(systemManager, number.getValue(), manager)
            if systems is not None:
                number.setSystems(systems)
