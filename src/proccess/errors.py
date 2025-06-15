from datetime import datetime
from random import randint
import traceback


def createLogFile(manager, error, trace, value):
    tb = traceback.extract_tb(trace)
    oldPath = manager.getPath()
    manager.setRouter("./src/storage/")

    now = datetime.now().strftime("%d/%m/%Y")
    serial = randint(1000, 9999)
    errorName = error.__class__.__name__
    ubication = f"{tb[0].filename}: linea {tb[0].lineno}"

    errorLog = f"{errorName}_{now}_{serial}: [{error} / {value} / {ubication}]\n"
    manager.writeFile("errors.log", errorLog)
    manager.setRouter(oldPath)
