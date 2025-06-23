import numpy as np
from helpers.arrays import appendArray
from proccess.files import selectFile
from proccess.numbers import getNumbers, setSystems
from repositories.NumericSystem import NumericSystem


def convert(manager): 
    n=input("Cuantas matrices desea crear? ")
    n=int(n)
    manager.setRouter("./src/storage/sources/")
    files = np.array([None for _ in range(n)])
    filColums = np.array([None for _ in range(n)])
    matrices = np.array([None for _ in range(n)])
    for i in range(n):
        files[i]=selectFile(manager)
        filColums[i] = cantReg(files[i])
        matrices[i] = createMatrix(filColums[i])
        matrices[i] = fillMatrix(files[i], matrices[i],filColums[i],manager)
        printMatrix(matrices[i])
    return matrices 

def cantReg(file):
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

def createMatrix(filaColum):
    matrix = np.zeros((filaColum[1], filaColum[0]))
    return matrix

def fillMatrix(file, matrix, filCol, manager):
    n=0
    content = file.getContent()
    aux = np.array([])
    for space in content:
        aux=appendArray(aux, len(space.split("#")))
    numbers = getNumbers(content, manager)
    systemManager = NumericSystem()
    setSystems(numbers, systemManager, manager)
    for i in range(filCol[1]):
        for j in range(aux[i]):
            value = numbers[n].toDecimal()
            matrix[i][j] = value
            n += 1
    return matrix

def printMatrix(matrix):
    for row in matrix:
        print(" | ".join(str(item) for item in row))
    print("\n")