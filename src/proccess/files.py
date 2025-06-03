from validations.selector import validateSelector
from repositories.FileEntry import FileEntry
import numpy as np
import random


def selectFile(manager):
    files = manager.listFiles()
    print("Archivos disponibles:")
    for i in range(len(files)):
        print(f"{i + 1}. {files[i]}")
    choice = validateSelector(
        1, len(files), f"Elige el archivo a leer (1-{len(files)}): ")
    if choice == -1:
        return None
    else:
        rawContent = manager.openFile(files[choice - 1])
        name = files[choice - 1]
        return FileEntry(name, rawContent, manager.getPath())


def createResultFile(manager, sourceFileName, numbers):
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

            resultLine = f"{number.getValue()}#{joinedSystems[1:]}#{number.getFigs()}\n"
            # TODO: add ElemsOps to resultLine
            # TODO: add SigFigs to resultLine
        else:
            resultLine = f"{
                number.getValue()} -> No pertenece a ningun sistema numerico\n"
        manager.writeFile(resultFileName, resultLine)
