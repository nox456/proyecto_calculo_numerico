import numpy as np
from helpers.arrays import splitInPairs
from array import ArrayType
from repositories.Number import Number


class Formula:
    __raw = ""
    __replaced = ""
    __result = ""
    __isValid = True

    def __init__(self, raw: str, isMatrix: bool, isValid: bool):
        if isValid:
            self.__checkFormula(raw, isMatrix)
            self.__raw = raw
        else:
            self.__raw = raw
        self.__isValid = isValid

    def __checkFormula(self, formula: str, isMatrix: bool) -> str:
        openParenthesisCount = formula.count("(")
        closeParenthesisCount = formula.count(")")
        if openParenthesisCount != closeParenthesisCount:
            raise Exception("Formula no válida")
        if isMatrix:
            if "(" in formula and ")" in formula:
                insideParenthesis = formula[formula.find("(") + 1:formula.rfind(")")]
                formula = formula.replace(f"({insideParenthesis})",
                                          self.__checkFormula(insideParenthesis, isMatrix))
            pairs = splitInPairs(formula)
            for pair in pairs:
                isFirstIncognit = pair[0].lower() in np.array(["a", "b", "c"])
                isSecondIncognit = pair[2].lower() in np.array(["a", "b", "c"])
                isSum = pair[1] == "+"
                isSub = pair[1] == "-"
                if isFirstIncognit and (isSum or isSub) and not isSecondIncognit:
                    raise Exception("Formula no válida")
                if not isFirstIncognit and (isSum or isSub) and isSecondIncognit:
                    raise Exception("Formula no válida")
            return pairs[0][0]
        return formula[0]

    def evaluateFormula(self, numberTrio: ArrayType[Number]) -> None:
        firstValue = numberTrio[0].toDecimal()
        secondValue = numberTrio[1].toDecimal() if len(numberTrio) > 1 else 0
        thirdValue = numberTrio[2].toDecimal() if len(numberTrio) > 2 else 0
        self.__replaced = self.__raw.lower().replace("a", str(firstValue))
        self.__replaced = self.__replaced.lower().lower().replace(
            "b", str(secondValue))
        self.__replaced = self.__replaced.lower().replace(
            "c", str(thirdValue))
        self.__result = eval(self.__replaced)

    def getRaw(self) -> str:
        return self.__raw

    def getResult(self) -> str:
        return self.__result

    def isValid(self) -> bool:
        return self.__isValid
