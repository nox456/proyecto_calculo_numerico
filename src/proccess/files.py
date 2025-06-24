from validations.selector import validateSelector
from validations.files import validateSourceFileName, validateFileEntry
import numpy as np
import random
from repositories.FileManager import FileManager
from repositories.FileEntry import FileEntry
from array import ArrayType
from repositories.Number import Number
from repositories.Formula import Formula
from proccess.numbers import setMatrixOperations

def selectFile(manager: FileManager) -> FileEntry:
    files = manager.listFiles()
    if len(files) == 0:
        print("No hay archivos disponibles")
        return None
    print("Archivos disponibles:")
    for i in range(len(files)):
        print(f"{i + 1}. {files[i]}")
    choice = validateSelector(
        1, len(files), f"Elige el archivo a leer (1-{len(files)}): ", manager)
    if choice == -1:
        return None
    else:
        if validateSourceFileName(files[choice - 1], manager) is None:
            return None
        rawContent = manager.openFile(files[choice - 1])
        if rawContent is None:
            return None
        name = files[choice - 1]
        file = validateFileEntry(name, rawContent, manager)
        return file


def createResultFile(manager: FileManager, sourceFileName: str, numbers: ArrayType[Number]) -> None:
    sourceFileAttributes = np.array(sourceFileName.rstrip(".bin").split("_"))
    newSerial = random.randint(1000, 9999)
    resultFileName = f"{sourceFileAttributes[2]}_{
        sourceFileAttributes[1]}_{newSerial}.txt"
    for number in numbers:
        if number.isValid():
            systems = number.getSystems()
            joinedSystems = ""
            for system in systems:
                joinedSystems = f"{joinedSystems},{system}"
            resultLine = f"{number.getValue()}#{joinedSystems[1:]}#{number.getFigs()}#{number.getOperations()}\n"

        else:
            resultLine = f"{
                number.getValue()} -> No pertenece a ningun sistema numerico\n"
        manager.writeFile(resultFileName, resultLine)

def createResultMatrixFile(manager: FileManager, sourceFileName: str, matrices, matrixManager):
    sourceFileAttributes = np.array(sourceFileName.rstrip(".bin").split("_"))
    newSerial = random.randint(1000, 9999)
    resultFileName = f"{sourceFileAttributes[2]}_{sourceFileAttributes[1]}_{newSerial}_matrices.txt"
    for matrix in matrices:
        if len(matrix) == 0:
            resultLine = "Matriz vacia\n"
        else:
            resultLine = ""
            for row in matrix:
                rowValues = [str(num) for num in row]
                resultLine += " | ".join(rowValues) + "\n"
        manager.writeFile(resultFileName, resultLine)
        manager.writeFile(resultFileName, "Operaciones: ")
        manager.writeFile(resultFileName, matrixManager.doOperations(matrix) + "\n")

def selectFormulas(manager: FileManager, isMatrix: bool) -> FileEntry:
    manager.setRouter("./src/storage/formulas/")
    formulas = manager.listFiles()
    if len(formulas) == 0:
        print("No hay formularios disponibles")
        return None
    print("\nFormularios disponibles:")
    for i in range(len(formulas)):
        print(f"{i + 1}. {formulas[i]}")
    choice = validateSelector(
        1, len(formulas), f"Elige el formulario a leer (1-{len(formulas)}): ", manager)
    if choice == -1:
        return None
    else:
        if validateSourceFileName(formulas[choice - 1], manager) is None:
            return None
        rawContent = manager.openFile(formulas[choice - 1])
        if rawContent is None:
            return None
        name = formulas[choice - 1]
        formulaFile = validateFileEntry(name, rawContent, manager)
        return formulaFile


def createFormulasResultFile(manager: FileManager, formulas: ArrayType[Formula], sourceFileName: str) -> None:
    sourceFileAttributes = np.array(sourceFileName.rstrip(".bin").split("_"))
    newSerial = random.randint(1000, 9999)
    resultFileName = f"{sourceFileAttributes[2]}_{
        sourceFileAttributes[1]}_{newSerial}.txt"
    for formula in formulas:
        if not formula.isValid():
            resultLine = f"Formula invalida -> {formula.getRaw()}\n"
            manager.writeFile(resultFileName, resultLine)
        else:
            if formula.isMatrix():
                resultLine = f"{formula.getRaw()}\n{formula.getResult()}\n"
            else:
                resultLine = f"{formula.getRaw()}#{formula.getValues()}#{formula.getResult()}\n"
            manager.writeFile(resultFileName, resultLine)
