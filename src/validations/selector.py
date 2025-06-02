
def validateSelector(min, max, text):
    while True:
        try:
            value = int(input(text + "(-1) para salir: "))
            if value == -1:
                return -1
            if value < min or value > max:
                raise Exception(
                    "Selection-Error: El valor debe estar entre los límites")
            return value
        except Exception as e:
            print(e)
