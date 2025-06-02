from proccess.files import selectFile
from proccess.numbers import getNumbers, setSystems
from repositories.NumericSystem import NumericSystem


def main():
    path = "."
    file = selectFile(path)
    if file is None:
        print("-- PROGRAMA TERMINADO --")
        return
    content = file.getContent()
    numbers = getNumbers(content)
    systemManager = NumericSystem()
    setSystems(numbers, systemManager)


main()
