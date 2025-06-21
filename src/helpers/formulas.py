from array import ArrayType
import numpy as np
from helpers.arrays import appendArray


def checkFormula(formula: str) -> str:
    openParenthesisCount = formula.count("(")
    closeParenthesisCount = formula.count(")")
    if openParenthesisCount != closeParenthesisCount:
        raise Exception("Formula no válida")
    if "(" in formula and ")" in formula:
        insideParenthesis = formula[formula.find("(") + 1:formula.rfind(")")]
        formula = formula.replace(f"({insideParenthesis})",
                                  checkFormula(insideParenthesis))
    pairs = splitInPairs(formula)
    for pair in pairs:
        isFirstIncognit = pair[0] in ["A", "B", "C"]
        isSecondIncognit = pair[2] in ["A", "B", "C"]
        isSum = pair[1] == "+"
        isSub = pair[1] == "-"
        if isFirstIncognit and (isSum or isSub) and not isSecondIncognit:
            raise Exception("Formula no válida")
        if not isFirstIncognit and (isSum or isSub) and isSecondIncognit:
            raise Exception("Formula no válida")
    return pairs[0][0]


def splitInPairs(text: str) -> ArrayType[str]:
    pairs = np.array([])
    operatorsCount = 0
    for char in text:
        if char == "+":
            operatorsCount += 1
        elif char == "-":
            operatorsCount += 1
        elif char == "*":
            operatorsCount += 1
        elif char == "/":
            operatorsCount += 1

    while len(pairs) < operatorsCount:
        pairs = appendArray(pairs, f"{text[0]}{text[1]}{text[2]}")
        text = text[2:]
    return pairs
