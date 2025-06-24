from proccess.files import selectFiles, createResultFiles, selectFormulas, createFormulasResultFile, getFilesContent
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
        files = selectFiles(fileManager)
        if files is None or len(files) == 0:
            print("-- PROGRAMA TERMINADO --")
            return
        content = getFilesContent(files)
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

        createResultFiles(fileManager, files, numbers)

    formulasEntries = selectFormulas(fileManager, isMatrix)

    if formulasEntries is None:
        print("-- PROGRAMA TERMINADO --")
        return

    formulaContent = getFilesContent(formulasEntries)

    formulas = getFormulas(formulaContent, fileManager, isMatrix,
                           numbers if numbers is not None else matrices)

    generateResultsFromFormulas(formulas, numbers, matrices, fileManager)

    fileManager.setRouter(
        "./src/storage/results/")
    createFormulasResultFile(fileManager, formulas, formulasEntries)

    print("-- PROGRAMA TERMINADO --")


main()
