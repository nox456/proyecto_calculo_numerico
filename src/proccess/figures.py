from helpers.arrays import appendArray
from validations.valFigs import validateFigures

def getSigFigs(figuresManager, numbers):
    for number in numbers:
        if number.isValid():
            sigFigures = validateFigures(figuresManager, number.getValue())
            if sigFigures is not None:
                number.setFigs(sigFigures)