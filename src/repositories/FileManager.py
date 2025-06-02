import os
import numpy as np
from helpers.arrays import appendArray


class FileManager:
    __path = os.getcwd()

    def __init__(self, path=os.getcwd()):
        if len(path) == 0:
            raise Exception("Manage-Error: Debe ingresar una ruta")
        self.__path = self.__utilPath(path)

    def setRouter(self, path):
        if len(path) == 0:
            raise Exception("Manage-Error: Debe ingresar una ruta")
        self.__path = self.__utilPath(path)

    def readFiles(self):
        files = self.__listFiles()
        print("Archivos disponibles:")
        for i in range(len(files)):
            print(f"{i + 1}. {files[i]}")
        choice = int(input(f"Elige el archivo a leer (1-{len(files)}): "))
        file = self.__openFile(files[choice - 1])
        return file

    def __openFile(self, fileName):
        filePath = os.path.join(self.__path, fileName)
        try:
            file = open(filePath, "rb")
            return file
        except FileNotFoundError as e:
            print(f"Manage-Error: El archivo no existe: {e}")
            return None

    def __listFiles(self):
        directoryEntries = np.array(os.listdir(self.__path))
        files = np.array([])
        for entry in directoryEntries:
            if entry.endswith(".bin"):
                files = appendArray(files, str(entry))
        return files

    def __utilPath(self, path):
        if not os.path.exists(path):
            raise Exception("Manage-Error: La ruta ingresada no existe")
        if not os.path.isdir(path):
            raise Exception(
                "Manage-Error: La ruta ingresada no es un directorio")
        return path
