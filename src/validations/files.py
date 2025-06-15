from helpers.arrays import containsArray
from repositories.Number import Number
from proccess.errors import createLogFile
from repositories.FileEntry import FileEntry


def validateFileLine(line, manager):
    try:
        if containsArray(line, "#"):
            return line
        else:
            raise Exception(
                "El formato de la linea es incorrecto")
    except Exception as error:
        createLogFile(manager, error, error.__traceback__, line)
        return None


def validateFileEntry(name, rawContent,  manager):
    try:
        file = FileEntry(name, rawContent, manager.getPath())
        return file
    except Exception as error:
        createLogFile(manager, error, error.__traceback__, name)
        return None


def validateFileElement(element, manager):
    try:
        number = Number(element)
    except Exception as error:
        createLogFile(manager, error, error.__traceback__, element)
        return Number(element, False)
    return number


def validateSourceFileName(name, manager):
    try:
        if containsArray(name, "_"):
            nameAttributes = name.rstrip(".bin").split("_")
            if len(nameAttributes) != 3:
                raise Exception("El nombre del archivo fuente es incorrecto")
            return name
        else:
            raise Exception("El nombre del archivo fuente es incorrecto")
    except Exception as error:
        createLogFile(manager, error, error.__traceback__, name)
        return None
