from proccess.errors import createLogFile


def validateFigures(figuresManager, value, fileManager):
    try:
        figuresManager.setNumber(value)
        return figuresManager.operation()
    except Exception as error:
        createLogFile(fileManager, error, error.__traceback__, value)
        return None
