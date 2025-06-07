from proccess.errors import createLogFile


def validatePossibleSystems(systemManager, value, fileManager):
    try:
        systemManager.setNumber(value)
        return systemManager.getPossibleSystems()
    except Exception as e:
        print(e)
        createLogFile(fileManager, e)
        return None
