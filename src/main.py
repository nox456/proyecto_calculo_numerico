from proccess.files import selectFile, createResultFile, selectFormulas, createFormulasResultFile
from proccess.numbers import getNumbers, setSystems, generateResultsFromFormulas, setOperations
from helpers.matrixConverter import MatrixConverter
from proccess.figures import getSigFigs
from repositories.NumericSystem import NumericSystem
from repositories.SigFigures import SigFigures
from repositories.FileManager import FileManager
from helpers.formulas import checkIsMatrix, getFormulas
from repositories.ElementalOperations import ElementalOperations
from repositories.GaussMatrixOp import GaussMatrixOp


def main() -> None:
    path = "./src/storage/sources/"
    fileManager = FileManager(path)
    file = selectFile(fileManager)
    if file is None:
        print("-- PROGRAMA TERMINADO --")
        return
    isMatrix = checkIsMatrix(fileManager)
    formulaFile = selectFormulas(fileManager, isMatrix)
    if formulaFile is None:
        print("-- PROGRAMA TERMINADO --")
        return
    content = file.getContent()
    numbers = getNumbers(content, fileManager)
    if len(numbers) == 0:
        print("-- PROGRAMA TERMINADO --")
        return
    systemManager = NumericSystem()
    setSystems(numbers, systemManager, fileManager)
    operationManager = ElementalOperations()
    figuresManager = SigFigures("0")
    getSigFigs(figuresManager, numbers, fileManager)
    # TODO: initialize ElemsOps ADT
    matrixCheck = MatrixConverter(fileManager)
    matrices = matrixCheck.convert()
    fileManager.setRouter(
        "./src/storage/results/")
    formulaContent = formulaFile.getContent()
    formulas = getFormulas(formulaContent, fileManager, isMatrix)
    generateResultsFromFormulas(formulas, numbers)
    createResultFile(fileManager, file.getName(), numbers)
    createFormulasResultFile(fileManager, formulas, formulaFile.getName())

    print("-- PROGRAMA TERMINADO --")
    setOperations(numbers, operationManager)


main()
