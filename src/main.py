from proccess.files import selectFile, createResultFile
from proccess.numbers import getNumbers, setSystems
from repositories.NumericSystem import NumericSystem
from repositories.FileManager import FileManager


def main():
    path = "."
    fileManager = FileManager(path)
    file = selectFile(fileManager)
    if file is None:
        print("-- PROGRAMA TERMINADO --")
        return
    content = file.getContent()
    numbers = getNumbers(content)
    systemManager = NumericSystem()
    setSystems(numbers, systemManager)
    # TODO: initialize SigFigs ADT
    # TODO: initialize ElemsOps ADT
    fileManager.setRouter(
        "/home/nox/Documentos/Projects/Proyecto_Calculo_Numerico/src/storage")
    createResultFile(fileManager, file.getName(), numbers)

    print("-- PROGRAMA TERMINADO --")


main()
