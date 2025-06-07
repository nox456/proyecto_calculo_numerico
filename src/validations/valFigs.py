from proccess.errors import createLogFile


def validateFigures(figuresManager, value, fileManager):
    try:
        figuresManager.setNumber(value)
        return figuresManager.operation()
    except Exception as e:
        print(e)
        createLogFile(fileManager, e)
        return None
