import numpy as np
from helpers.arrays import appendArray


class FileEntry:
    __name = ""
    __path = ""
    __content = np.array([])

    def __init__(self, name, rawContent, path="."):
        self.__name = name
        self.__path = path
        self.__content = self.__parseContent(rawContent)

    def __parseContent(self, rawContent):
        content = np.array([])
        for line in rawContent:
            content = appendArray(content, line.decode("utf-8").strip())
        return content

    def getContent(self):
        return self.__content
