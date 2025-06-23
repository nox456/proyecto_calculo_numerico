from proccess.files import selectFile, createResultFile, selectFormulas, createFormulasResultFile
from proccess.numbers import getNumbers, setSystems, generateResultsFromFormulas, setOperations
from helpers.matrixConverter import MatrixConverter
from proccess.figures import getSigFigs
from repositories.NumericSystem import NumericSystem
from repositories.SigFigures import SigFigures
from repositories.FileManager import FileManager
from helpers.formulas import checkIsMatrix, getFormulas
from repositories.ElementalOperations import ElementalOperations


def main() -> None:
    path = "./src/storage/sources/"
    fileManager = FileManager(path)

    isMatrix = checkIsMatrix(fileManager)

    matrices = None
    numbers = None

    if isMatrix:
        matrixCheck = MatrixConverter(fileManager)
        matrices = matrixCheck.convert()
    else:
        file = selectFile(fileManager)
        if file is None:
            print("-- PROGRAMA TERMINADO --")
            return
        content = file.getContent()
        numbers = getNumbers(content, fileManager)
        if len(numbers) == 0:
            print("-- PROGRAMA TERMINADO --")
            return

        systemManager = NumericSystem()
        setSystems(numbers, systemManager, fileManager)

        figuresManager = SigFigures("0")
        getSigFigs(figuresManager, numbers, fileManager)

        operationManager = ElementalOperations()
        setOperations(numbers, operationManager)

        fileManager.setRouter(
            "./src/storage/results/")

        createResultFile(fileManager, file.getName(), numbers)

    formulaFile = selectFormulas(fileManager, isMatrix)

    if formulaFile is None:
        print("-- PROGRAMA TERMINADO --")
        return

    formulaContent = formulaFile.getContent()

    formulas = getFormulas(formulaContent, fileManager, isMatrix,len(numbers if numbers is not None else matrices))

    generateResultsFromFormulas(formulas, numbers, matrices)

    fileManager.setRouter(
        "./src/storage/results/")
    createFormulasResultFile(fileManager, formulas, formulaFile.getName())

    print("-- PROGRAMA TERMINADO --")


main()
