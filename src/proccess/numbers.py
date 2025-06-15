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


def toDecimal(number):
    if number is None:
        return None
    value = 0
    hexDict = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "a": "10",
        "b": "11",
        "c": "12",
        "d": "13",
        "e": "14",
        "f": "15"
    }
    if "Decimal" in number.getSystems():
        value = int(number.getValue())
    elif "Hexadecimal" in number.getSystems() and "Binario" not in number.getSystems():
        for i in range(len(str(number.getValue()))):
            exponent = len(str(number.getValue())) - i - 1
            n = int(hexDict[str(number.getValue())[i].lower()])
            value += n * 16 ** exponent
    elif "Binario" in number.getSystems():
        for i in range(len(str(number.getValue()))):
            exponent = len(str(number.getValue())) - i - 1
            n = int(str(number.getValue())[i])
            value += n * 2 ** exponent
    return value
