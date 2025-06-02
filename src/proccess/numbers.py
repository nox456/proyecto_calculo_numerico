from helpers.arrays import appendArray
from validations.fileLine import validateFileLine


def getNumbers(fileContent):
    numbers = []
    for i in range(len(fileContent)):
        line = validateFileLine(fileContent[i])
        if line is not None:
            lineNumbers = line.split("#")
            for number in lineNumbers:
                numbers = appendArray(numbers, number)
    return numbers
