from helpers.arrays import containsArray
from helpers.formulas import checkFormula
from repositories.Number import Number
from repositories.FileEntry import FileEntry
from repositories.FileManager import FileManager
from array import ArrayType
from typing import TextIO


def validateFileLine(line: ArrayType[str], manager: FileManager) -> ArrayType[str]:
    try:
        if containsArray(line, "#"):
            return line
        else:
            raise Exception(
                "El formato de la linea es incorrecto")
    except Exception as error:
        from proccess.errors import createLogFile
        createLogFile(manager, error, error.__traceback__, line)
        return None


def validateFileEntry(name: str, rawContent: TextIO,  manager: FileManager) -> FileEntry:
    try:
        file = FileEntry(name, rawContent, manager.getPath())
        return file
    except Exception as error:
        from proccess.errors import createLogFile
        createLogFile(manager, error, error.__traceback__, name)
        return None


def validateFileElement(element: str, manager: FileManager) -> Number:
    try:
        number = Number(element)
    except Exception as error:
        from proccess.errors import createLogFile
        createLogFile(manager, error, error.__traceback__, element)
        return Number(element, False)
    return number


def validateSourceFileName(name: str, manager: FileManager) -> str:
    try:
        if containsArray(name, "_"):
            nameAttributes = name.rstrip(".bin").split("_")
            if len(nameAttributes) != 3:
                raise Exception("El nombre del archivo fuente es incorrecto")
            return name
        else:
            raise Exception("El nombre del archivo fuente es incorrecto")
    except Exception as error:
        from proccess.errors import createLogFile
        createLogFile(manager, error, error.__traceback__, name)
        return None


def validateFormula(formula: str, manager: FileManager) -> bool:
    try:
        checkFormula(formula)
        return True
    except Exception as error:
        from proccess.errors import createLogFile
        createLogFile(manager, error, error.__traceback__, formula)
        return None
