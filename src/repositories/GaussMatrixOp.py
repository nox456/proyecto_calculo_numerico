import numpy as np
from helpers.arrays import appendArray

class GaussMatrixOp:
    __matrix = np.array([])

    def __init__(self, mat):
        self.__matrix = mat

    #getters
    def setMatrix(self, matrix):
        self.__matrix=matrix
    
    #setters
    def getMatrix(self):
        return self.__matrix

    #methods
    def operation(self):
        n = self.cantMatrx()
        matrices = np.array([])
        for i in range(n):
            matrices = appendArray(matrices, self.addToMatrix(self.__matrix[i]))
        for i in range(n):
            Ab = matrices[i]
            Ab[i] = Ab[i] / Ab[i, i]
            for j in range(n):
                if i != j:
                    Ab[j] = Ab[j] - Ab[j, i] * Ab[i]
        return Ab[:, -1]
    
    def addToMatrix(self, matrix):
        matrixAux = np.zeros((len(matrix), len(matrix[0]) + 1))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrixAux[i][j] = matrix[i][j]
            matrixAux[i][len(matrix[i])] = 1
        return matrixAux

    def cantMatrx(self):
        n=0
        for rows in self.__matrix:
            n+=1
        return n
    
    def startOperation(self):
        for i in range(len(self.__matrix)):
            matrix = self.operation()
            print("Los resultados son: ")
            print(matrix)
