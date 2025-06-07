from proccess.files import selectFile, createResultFile
from proccess.numbers import getNumbers, setSystems
from proccess.figures import getSigFigs
from repositories.NumericSystem import NumericSystem
from repositories.SigFigures import SigFigures
from repositories.FileManager import FileManager


def main():
    path = "."
    fileManager = FileManager(path)
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
    # TODO: initialize ElemsOps ADT
    fileManager.setRouter(
        "./src/storage/")
    createResultFile(fileManager, file.getName(), numbers)

    print("-- PROGRAMA TERMINADO --")


main()
