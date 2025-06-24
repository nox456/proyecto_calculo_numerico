import numpy as np
from helpers.arrays import appendArray

class GaussMatrixOp:
    __matrices = np.array([])

    def __init__(self, mat):
        self.__matrices = mat

    #getters
    def setMatrix(self, matrix):
        self.__matrix=matrix
    
    #setters
    def getMatrix(self):
        return self.__matrix

    #methods
    def operation(self, matrix):
        A = np.array(matrix, dtype=float)
        n = len(A)
        m = len(A[0])
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
        for rows in self.__matrix:
            n+=1
        return n
    
    def startOperation(self):
        for matrix in self.__matrices:
            matrix = self.addToMatrix(matrix)
            print(matrix)
            np.set_printoptions(
            suppress=True,
            precision=3,
            floatmode='fixed'
            )
            result = self.operation(matrix)
            print("Los resultados: ")
            print(result)
