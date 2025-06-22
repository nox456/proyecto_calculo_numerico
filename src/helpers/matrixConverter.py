import numpy as np
from helpers.arrays import appendArray
from proccess.files import selectFile
from proccess.numbers import getNumbers, setSystems
from repositories.NumericSystem import NumericSystem

class MatrixConverter:

    manager = None

    def __init__(self, manager):
        if manager is None:
            raise Exception("MatrixConverter-Error: Debe ingresar un administrador de archivos")
        self.manager = manager

    def setManager(self, manager):
        if manager is None:
            raise Exception("MatrixConverter-Error: Debe ingresar un administrador de archivos")
        self.manager = manager

    def getManager(self):
        return self.manager

    def convert(self): 
        input("Deberá seleccionar 2 archivos: ")
        fileA=selectFile(self.manager)
        fileB=selectFile(self.manager)
        filaColumA= self.CantReg(fileA)
        filaColumB= self.CantReg(fileB)
        matrixA = self.createMatrix(filaColumA)
        matrixB = self.createMatrix(filaColumB) 
        matrixA = self.fillMatrix(fileA, matrixA,filaColumA)
        matrixB = self.fillMatrix(fileB, matrixB,filaColumB)
        self.printMatrix(matrixA)
        self.printMatrix(matrixB)     

    def CantReg(self,file):
        filaColum = np.array([0, 0])
        if (file == ""):
            print("Objet-file: El archivo está vacio.")
            return filaColum
        file = file.getContent()
        camp = np.array([])
        cont = 0
        band = 0
        aux = 0
        for i in file:
            cont = cont + 1
            camp = i.split("#")
            if (band == 0):
                aux = len(camp)
                band = 1
            elif (len(camp) > aux):
                aux = len(camp)
        filaColum[0] = aux
        filaColum[1] = cont
        return filaColum

    def createMatrix(self,filaColum):
        matrix = np.zeros((filaColum[1], filaColum[0]))
        return matrix

    def fillMatrix(self,file, matrix, filCol):
        n=0
        content = file.getContent()
        aux = np.array([])
        for space in content:
            aux=appendArray(aux, len(space.split("#")))
        numbers = getNumbers(content, self.manager)
        systemManager = NumericSystem()
        setSystems(numbers, systemManager, self.manager)
        for i in range(filCol[1]):
            for j in range(aux[i]):
                value = numbers[n].toDecimal()
                matrix[i][j] = value
                n += 1
        return matrix

    def printMatrix(self,matrix):
        for row in matrix:
            print(" | ".join(str(item) for item in row))
        print("\n")