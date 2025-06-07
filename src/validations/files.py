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
                f"FileLine-Error: El formato de la linea es incorrecto: {line}")
    except Exception as e:
        print(e)
        createLogFile(manager, e)
        return None


def validateFileEntry(name, rawContent,  manager):
    try:
        file = FileEntry(name, rawContent, manager.getPath())
        return file
    except Exception as e:
        print(e)
        createLogFile(manager, e)
        return None


def validateFileElement(element, manager):
    try:
        number = Number(element)
    except Exception as e:
        print(e)
        createLogFile(manager, e)
        return Number(element, False)
    return number


def validateSourceFileName(name, manager):
    try:
        if containsArray(name, "_"):
            nameAttributes = name.rstrip(".bin").split("_")
            if len(nameAttributes) != 3:
                raise Exception(
                    f"SourceFileName-Error: El nombre del archivo fuente es incorrecto: {name}")
            return name
        else:
            raise Exception(
                f"SourceFileName-Error: El nombre del archivo fuente es incorrecto: {name}")
    except Exception as e:
        print(e)
        createLogFile(manager, e)
        return None
