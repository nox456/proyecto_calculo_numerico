import numpy as np
from proccess.files import selectFiles, getFilesContent
from proccess.numbers import getNumbers, setSystems
from repositories.NumericSystem import NumericSystem
from repositories.FileManager import FileManager
from repositories.FileEntry import FileEntry
from array import ArrayType


class MatrixConverter:

    __manager = None
    __files = np.array([])

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
        self.__manager.setRouter("./src/storage/sources/")
        self.__files = selectFiles(self.__manager)
        filColums = np.array([None for _ in range(len(self.__files))])
        matrices = np.array([None for _ in range(len(self.__files))])
        for i in range(len(self.__files)):
            filColums[i] = self.cantReg(self.__files[i])
            matrices[i] = self.createMatrix(filColums[i])
        self.fillMatrix(self.__files, matrices, filColums)
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
        matrix = [[0 for _ in range(filaColum[0])] for _ in range(filaColum[1])]
        return matrix

    def fillMatrix(self, files: ArrayType[FileEntry], matrix: ArrayType[ArrayType[ArrayType[int]]], filCol: ArrayType[ArrayType[int]]) -> ArrayType[ArrayType[int]]:
        content = getFilesContent(files)
        numbers = getNumbers(content, self.__manager, True)
        systemManager = NumericSystem()
        setSystems(numbers, systemManager, self.__manager, True)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                for k in range(len(matrix[i][j])):
                    if k < len(numbers[i][j]):
                        matrix[i][j][k] = numbers[i][j][k].toDecimal()
                    else:
                        matrix[i][j][k] = 0
        return matrix

    def getFiles(self) -> ArrayType[FileEntry]:
        return self.__files
