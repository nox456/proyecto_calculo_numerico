from proccess.files import selectFile
from proccess.numbers import getNumbers, setSystems, setOperations
from repositories.NumericSystem import NumericSystem
from repositories.ElementalOperations import ElementalOperations


def main():
    path = "."
    file = selectFile(path)
    if file is None:
        print("-- PROGRAMA TERMINADO --")
        return
    content = file.getContent()
    numbers = getNumbers(content)
    systemManager = NumericSystem()
    operationManager = ElementalOperations()
    setSystems(numbers, systemManager)
    setOperations(numbers, operationManager)
    # TODO: initialize SigFigs ADT

    for number in numbers:
        if number.isValid():
            print(f"Numero: {number.getValue()}")
            print(f"Sistemas: {number.getSystems()}")
            print(f"Operaciones: {number.getOperations()}")
        else:
            print(f"Numero invalido: {number.getValue()}")


main()
