import numpy as np
from helpers.arrays import appendArray
from validations.operations import validateGaussOperation

class GaussMatrixOp:
    __matrices = np.array([])

    def __init__(self, mat):
        if len(mat) == 0:
            raise ValueError("Error: No hay matrices")
        else:
            self.__matrices = mat

    #setters
    def setMatrix(self, matrix):
        if matrix == None:
            raise ValueError("Error: Es necesario tener las matrices")
        if len(matrix) == 0:
            raise ValueError("Error: No hay matrices")
        else:
            self.__matrices = matrix
    
    #getters
    def getMatrix(self):
        return self.__matrices

    #methods
    def operation(self, matrix):
        A = np.array(matrix, dtype=float)
        n = len(A)
        for i in range(n):
            if A[i, i] == 0:
                raise ValueError("División por cero en la fila {}".format(i))
            A[i] = A[i] / A[i, i]
            for j in range(n):
                if i != j:
                    A[j] = A[j] - A[j, i] * A[i]
        return A[:, -1]
    
    def addToMatrix(self, matrix):
        matrixAux = np.zeros((len(matrix), len(matrix[0]) + 1))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrixAux[i][j] = matrix[i][j]
            matrixAux[i][-1] = 1
        return matrixAux

    def cantMatrx(self):
        n=0
        for rows in self.__matrices:
            n+=1
        return n

    def checkMatrix(self, matrix):
        if not isinstance(matrix, (np.ndarray)):
            raise ValueError("La matriz debe ser un arreglo de NumPy.")
        if len(matrix) != len(matrix[0]):
            return "Al no ser una matriz cuadrada, tendra o infinitas soluciones o ninguna solucion"
        return ""
    
    def startOperation(self):
        results = np.array([])
        for matrix in self.__matrices:
            result = self.checkMatrix(matrix)
            matrix = self.addToMatrix(matrix)
            np.set_printoptions(suppress=True,precision=3,floatmode='fixed')
            if result == "":
                result = validateGaussOperation(self, matrix)
            results = appendArray(results, result)
        return results
