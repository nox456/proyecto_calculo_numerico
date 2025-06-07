from datetime import datetime


def createLogFile(manager, error):
    oldPath = manager.getPath()
    manager.setRouter("./src/storage/")
    now = datetime.now()
    errorLog = f"{now.strftime("%d/%m/%Y %H:%M:%S")}: {error}\n"
    manager.writeFile("errors.log", errorLog)
    manager.setRouter(oldPath)
