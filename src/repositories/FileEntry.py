import numpy as np
from helpers.arrays import appendArray
from typing import TextIO
from array import ArrayType


class FileEntry:
    __name = ""
    __path = ""
    __content = np.array([])

    def __init__(self, name: str, rawContent: TextIO, path: str = "."):
        self.__name = name
        self.__path = path
        self.__content = self.__parseContent(rawContent)

    def __parseContent(self, rawContent: TextIO) -> ArrayType[str]:
        content = np.array([])
        for line in rawContent:
            content = appendArray(content, line.decode("utf-8").strip())
        if len(content) == 0:
            raise Exception("FileContent-Error: El archivo está vacío")
        return content

    def getContent(self) -> ArrayType[str]:
        return self.__content

    def getName(self) -> str:
        return self.__name
