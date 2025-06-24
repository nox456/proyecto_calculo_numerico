import numpy as np

class MatrixOperations:

    __matrix = np.array([[]])
    __operations = ""

    def __init__(self, matrix = np.array([[]])):
        self.__matrix = matrix

    def setMatrix(self, matrix):
        self.__matrix = matrix

    def getMatrix(self):
        return self.__matrix

    def getOperations(self):
        return self.__operations
    
    # Utilitarias

    def __swapRow(self):
        if len(self.__matrix[0]) < 2:
            return self.__matrix
        newMatrix = self.__matrix.copy()
        newMatrix[0] = self.__matrix[1]
        newMatrix[1] = self.__matrix[0]
        return newMatrix

    def __swapColumn(self):
        if len(self.__matrix[1]) < 2:
            return self.__matrix
        newMatrix = self.__matrix.copy()

        for i in range(len(newMatrix)):
            newMatrix[i, 0] = self.__matrix[i, 1]
            newMatrix[i, 1] = self.__matrix[i, 0]
        return newMatrix

    def __lambdaMult(self, a = 2):
        newMatrix = self.__matrix.copy()

        for i in range(len(newMatrix[0])):
            newMatrix[0][i] = newMatrix[0][i]*a
        return newMatrix

    def __linearCombRow(self, a = 2):
        newMatrix = self.__matrix.copy()

        for i in range(len(newMatrix[0])):
            newMatrix[0][i] += newMatrix[1][i]*a
        return newMatrix
    
    def doOperations(self, matrix):
        self.__matrix = matrix
        self.__operations = ""
        m = self.__swapRow()
        m = self.__swapColumn()
        self.__operations += "cambio"
        m = self.__lambdaMult()
        self.__operations += "; multLambda"
        m = self.__linearCombRow()
        self.__operations += "; combinacion"

        if len(self.__operations) == 0:
            self.__operations = "No hay operaciones disponibles"
        
        return self.__operations