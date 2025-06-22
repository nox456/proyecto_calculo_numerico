from helpers.arrays import containsArray
from repositories.Number import Number


def validateFileLine(line):
    try:
        if containsArray(line, "#"):
            return line
        else:
            raise Exception(
                "FileLine-Error: El formato de la linea es incorrecto")
    except Exception as e:
        print(e)
        return None


def validateFileElement(element):
    try:
        number = Number(element)
    except Exception as e:
        print(e)
        return Number(element, False)
    return number


def validateSourceFileName(name):
    try:
        if containsArray(name, "_"):
            return name
        else:
            raise Exception(
                "SourceFileName-Error: El nombre del archivo fuente es incorrecto")
    except Exception as e:
        print(e)
        return None
