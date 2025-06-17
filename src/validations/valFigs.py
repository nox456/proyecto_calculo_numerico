def validateFigures(figuresManager, value, fileManager):
    try:
        figuresManager.setNumber(value)
        return figuresManager.operation()
    except Exception as error:
        from proccess.errors import createLogFile
        createLogFile(fileManager, error, error.__traceback__, value)
        return None
