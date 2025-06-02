from helpers.arrays import appendArray
from validations.files import validateFileLine, validateFileElement
from validations.systems import validatePossibleSystems


def getNumbers(fileContent):
    numbers = []
    for i in range(len(fileContent)):
        line = validateFileLine(fileContent[i])
        if line is not None:
            lineNumbers = line.split("#")
            for i in range(len(lineNumbers)):
                number = validateFileElement(lineNumbers[i])
                numbers = appendArray(numbers, number)
    return numbers


def setSystems(numbers, systemManager):
    for number in numbers:
        if number.isValid():
            systems = validatePossibleSystems(systemManager, number.getValue())
            if systems is not None:
                number.setSystems(systems)
