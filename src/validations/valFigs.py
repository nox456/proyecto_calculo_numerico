def validateFigures(figuresManager, value):
    try:
        figuresManager.setNumber(value)
        return figuresManager.operation()
    except Exception as e:
        print(e)
        return None