from repositories.ElementalOperations import ElementalOperations
from array import ArrayType



def validateOperations(operationManager: ElementalOperations, value: str, bases: ArrayType[str]):
    try:
        operationManager.setNumber(value)
        operationManager.setBases(bases)
        return operationManager.getOperations()
    except Exception as e:
        print(e)
        return None
    
def validateGaussOperation(gauss, matrix):
    try:
        return gauss.operation(matrix)
    except Exception as e :
        return e
