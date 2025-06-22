import numpy as np
from helpers.arrays import appendArray

class GaussMatrixOp:
    __matrices = ""
    __filCol = ""

    def __init__(self, mat):
        self.__matrices = mat

    #getters
    def setMatrix(self, matrix):
        self.__matrix=matrix
    
    #setters
    def getMatrix(self):
        return self.__matrix

    #methods
    def defineFilCol(self, matrix):
        i=0
        j=0
        for fil in matrix:
            i+=1
            for col in fil:
                j+=1
        self.__filCol=np.array([i,j])
        print(type(self.__filCol))

    def getKElement(self,n,matrix):
        return matrix[n][n]
    
    def convertRow(self,n,matrix):
        value=self.getKElement(n,matrix)
        for i in range(len(matrix[n])-1):
            element = matrix[n][i]
            element = element / value
            matrix[n][i]=element
            return matrix

    def multRow(self,n, values,matrix):
        value = values[n][n]
        value2 = matrix[n+1][n]
        return value2/value
        
    def operateRows(self, n, matrix):
        s=n
        while n < len(matrix):
            for j in range(len(matrix[n])):
                value=self.multRow(matrix)
                element1 = self.__matrix[s][j]
                element2 = self.__matrix[n][j]
                element1 *= value
                element2 -= element1
                matrix[n][j] = element2

    def printMatrix(self,matrix):
        for row in matrix:
            print(" | ".join(str(item) for item in row))
        print("\n")

    def gaussJordan(self):
        for matrix in self.__matrices:
            for i in range(len(matrix)):
                matrix = self.convertRow(i,matrix)
                matrix = self.operateRows(i,matrix)
                self.printMatrix(matrix)