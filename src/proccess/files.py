from validations.files import validateSourceFileName, validateFileEntry
import numpy as np
import random
from repositories.FileManager import FileManager
from repositories.FileEntry import FileEntry
from array import ArrayType
from repositories.Number import Number
from repositories.Formula import Formula
from helpers.arrays import appendArray


def selectFiles(manager: FileManager) -> ArrayType[FileEntry]:
    files = manager.listFiles()
    if len(files) == 0:
        print("No hay archivos disponibles")
        return None
    else:
        filesEntries = np.array([])
        for file in files:
            if validateSourceFileName(file, manager) is None:
                continue
            rawContent = manager.openFile(file)
            if rawContent is None:
                continue
            fileEntry = validateFileEntry(file, rawContent, manager)
            if fileEntry is None:
                continue
            filesEntries = appendArray(filesEntries, fileEntry)
        return filesEntries


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
            resultLine = f"{number.getValue()}#{joinedSystems[1:]}#{number.getFigs()}#{
                number.getOperations()}\n"

        else:
            resultLine = f"{
                number.getValue()} -> No pertenece a ningun sistema numerico\n"
        manager.writeFile(resultFileName, resultLine)


def getFilesContent(files: ArrayType[FileEntry]) -> ArrayType[ArrayType[str]]:
    content = np.array([])
    for file in files:
        content = appendArray(content, file.getContent())
    return content


def createResultMatrixFile(manager: FileManager, matrices, matrixManager):
    newSerial = random.randint(1000, 9999)
    resultFileName = f"matrix_2025_{newSerial}.txt"
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


def selectFormulas(manager: FileManager, isMatrix: bool) -> ArrayType[FileEntry]:
    manager.setRouter("./src/storage/formulas/")
    formulasFiles = manager.listFiles()
    if len(formulasFiles) == 0:
        print("No hay formularios disponibles")
        return None
    else:
        formulas = np.array([])
        for file in formulasFiles:
            if validateSourceFileName(file, manager) is None:
                continue
            rawContent = manager.openFile(file)
            if rawContent is None:
                continue
            formula = validateFileEntry(file, rawContent, manager)
            if formula is None:
                continue
            formulas = appendArray(formulas, formula)
        return formulas


def createFormulasResultFile(manager: FileManager, formulas: ArrayType[Formula], formulaFiles: ArrayType[FileEntry]) -> None:
    for i in range(len(formulaFiles)):
        sourceFileAttributes = np.array(
            formulaFiles[i].getName().rstrip(".bin").split("_"))
        newSerial = random.randint(1000, 9999)
        resultFileName = f"{sourceFileAttributes[2]}_{
            sourceFileAttributes[1]}_{newSerial}.txt"
        for formula in formulas[i]:
            if not formula.isValid():
                resultLine = f"Formula invalida -> {formula.getRaw()}\n"
                manager.writeFile(resultFileName, resultLine)
            else:
                if formula.isMatrix():
                    resultLine = f"{formula.getRaw()}\n{formula.getResult()}\n"
                else:
                    resultLine = f"{formula.getRaw()}#{formula.getValues()}#{
                        formula.getResult()}\n"
                manager.writeFile(resultFileName, resultLine)


def createResultFiles(manager: FileManager, files: ArrayType[FileEntry], numbers: ArrayType[ArrayType[Number]]) -> None:
    for i in range(len(files)):
        sourceFileName = files[i].getName()
        sourceFileAttributes = np.array(sourceFileName.rstrip(".bin").split("_"))
        newSerial = random.randint(1000, 9999)
        resultFileName = f"{sourceFileAttributes[2]}_{
            sourceFileAttributes[1]}_{newSerial}.txt"
        for number in numbers[i]:
            if number.isValid():
                systems = number.getSystems()
                joinedSystems = ""
                for system in systems:
                    joinedSystems = f"{joinedSystems},{system}"

                resultLine = f"{number.getValue()}#{joinedSystems[1:]}#{
                    number.getFigs()}#{number.getOperations()}\n"
            else:
                resultLine = f"{
                    number.getValue()} -> No pertenece a ningun sistema numerico\n"
            manager.writeFile(resultFileName, resultLine)
