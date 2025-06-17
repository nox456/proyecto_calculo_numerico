def validatePossibleSystems(systemManager, value, fileManager):
    try:
        systemManager.setNumber(value)
        return systemManager.getPossibleSystems()
    except Exception as error:
        from proccess.errors import createLogFile
        createLogFile(fileManager, error, error.__traceback__, value)
        return None
