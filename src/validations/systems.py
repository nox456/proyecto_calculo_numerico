

def validatePossibleSystems(systemManager, value):
    try:
        systemManager.setNumber(value)
        return systemManager.getPossibleSystems()
    except Exception as e:
        print(e)
        return None
