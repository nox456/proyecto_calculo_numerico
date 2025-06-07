from helpers.arrays import appendArray
from validations.valFigs import validateFigures

def getSigFigs(figuresManager, numbers, fileManager):
    for number in numbers:
        if number.isValid():
            sigFigures = validateFigures(figuresManager, number.getValue(), fileManager)
            if sigFigures is not None:
                number.setFigs(sigFigures)