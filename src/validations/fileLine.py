from helpers.arrays import containsArray


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
