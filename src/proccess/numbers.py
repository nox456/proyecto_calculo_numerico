from helpers.arrays import appendArray
from validations.files import validateFileLine, validateFileElement
from validations.systems import validatePossibleSystems
import numpy as np
from repositories.FileManager import FileManager
from repositories.NumericSystem import NumericSystem
from repositories.Number import Number
from repositories.Formula import Formula
from repositories.ElementalOperations import ElementalOperations
from array import ArrayType
import math
from validations.operations import validateOperations


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


def generateResultsFromFormulas(formulas: ArrayType[Formula], numbers: ArrayType[Number]) -> None:
    numbersParts = getNumbersTrios(numbers)
    for part in numbersParts:
        for formula in formulas:
            formula.evaluateFormula(part)


def getNumbersTrios(numbers: ArrayType[Number]) -> ArrayType[ArrayType[Number]]:
    allNumbers = np.array(numbers)
    parts = np.array_split(allNumbers, math.ceil(len(numbers) / 3))
    return parts


def setOperations(numbers: ArrayType[Number], operationsManager: ElementalOperations) -> None:
    for number in numbers:
        if number.isValid():
            operations = validateOperations(
                operationsManager, number.getValue(), number.getSystems())
            if operations is not None:
                number.setOperations(operations)
