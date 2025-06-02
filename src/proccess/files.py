from repositories.FileManager import FileManager
from validations.selector import validateSelector
from repositories.FileEntry import FileEntry


def selectFile(path):
    manager = FileManager(path)
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
        return FileEntry(name, rawContent, path)
