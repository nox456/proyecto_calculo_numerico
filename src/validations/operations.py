
def validateOperations(operationManager, value, bases):
    try:
        operationManager.setNumber(value)
        operationManager.setBases(bases)
        return operationManager.getOperations()
    except Exception as e:
        print(e)
        return None