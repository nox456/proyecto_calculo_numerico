from proccess.errors import createLogFile


def validatePossibleSystems(systemManager, value, fileManager):
    try:
        systemManager.setNumber(value)
        return systemManager.getPossibleSystems()
    except Exception as error:
        createLogFile(fileManager, error, error.__traceback__, value)
        return None
