import numpy as np
from helpers.arrays import appendArray
from proccess.files import selectFile
from proccess.numbers import getNumbers, setSystems
from repositories.NumericSystem import NumericSystem
from repositories.FileManager import FileManager
from repositories.FileEntry import FileEntry
from array import ArrayType


class MatrixConverter:

    __manager = None

    def __init__(self, manager: FileManager):
        if manager is None:
            raise Exception(
                "MatrixConverter-Error: Debe ingresar un administrador de archivos")
        self.__manager = manager

    def setManager(self, manager: FileManager):
        if manager is None:
            raise Exception(
                "MatrixConverter-Error: Debe ingresar un administrador de archivos")
        self.__manager = manager

    def getManager(self) -> FileManager:
        return self.__manager

    def convert(self) -> ArrayType[ArrayType[ArrayType[int]]]:
        n = input("Cuantas matrices desea crear? ")
        n = int(n)
        self.__manager.setRouter("./src/storage/sources/")
        files = np.array([None for _ in range(n)])
        filColums = np.array([None for _ in range(n)])
        matrices = np.array([None for _ in range(n)])
        for i in range(n):
            files[i] = selectFile(self.__manager)
            filColums[i] = self.cantReg(files[i])
            matrices[i] = self.createMatrix(filColums[i])
            matrices[i] = self.fillMatrix(files[i], matrices[i], filColums[i])
        return matrices

    def cantReg(self, file: FileEntry) -> ArrayType[int]:
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

    def createMatrix(self, filaColum: ArrayType[int]) -> ArrayType[ArrayType[int]]:
        matrix = np.zeros((filaColum[1], filaColum[0]))
        return matrix

    def fillMatrix(self, file: FileEntry, matrix: ArrayType[ArrayType[int]], filCol: ArrayType[int]) -> ArrayType[ArrayType[int]]:
        n = 0
        content = file.getContent()
        aux = np.array([])
        for space in content:
            aux = appendArray(aux, len(space.split("#")))
        numbers = getNumbers(content, self.__manager)
        systemManager = NumericSystem()
        setSystems(numbers, systemManager, self.__manager)
        for i in range(filCol[1]):
            for j in range(aux[i]):
                value = numbers[n].toDecimal()
                matrix[i][j] = value
                n += 1
        return matrix
