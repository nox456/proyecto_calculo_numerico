import numpy as np
from helpers.arrays import splitInPairs
from array import ArrayType
from repositories.Number import Number
from helpers.matrices import sumaMatrices, multiMatrices, divideMatrices, restaMatrices

alpha = "DEFGHIJKLMNOPQRSTUVWXYZ"


class Formula:
    """Representación de una fórmula.

    Attributes:
        raw (str): Fórmula en texto plano.
        result (str): Resultado de la evaluación de la fórmula.
        isValid (bool): Indica si la fórmula es válida.
        isMatrix (bool): Indica si la fórmula tiene matrices.
        values (dict): Valores iniciales que tomaran las variables de la formula
    """
    __raw = ""
    __result = ""
    __isValid = True
    __isMatrix = False
    __values = {}

    def __init__(self, raw: str, isMatrix: bool, isValid: bool):
        if isValid:
            self.__checkFormula(raw, isMatrix)
            self.__raw = raw
        else:
            self.__raw = raw
        self.__isValid = isValid
        self.__isMatrix = isMatrix

    def __checkFormula(self, formula: str, isMatrix: bool) -> str:
        """Valida la fórmula.

        Args:
            formula (str): Fórmula en texto plano.
            isMatrix (bool): Indica si la fórmula tiene matrices.

        Returns:
            str: Fórmula en texto plano con las variables reemplazadas.

        Raises:
            Exception: Si la fórmula no es válida.
        """
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

    def evaluateNumbersFormula(self, numberTrio: ArrayType[Number]) -> None:
        """Reemplaza las variables de la fórmula con los valores de los números y la evalua.

        Args:
            numberTrio (ArrayType[Number]): Lista de números a evaluar.
        """
        firstValue = numberTrio[0].toDecimal()
        secondValue = numberTrio[1].toDecimal() if len(numberTrio) > 1 else 0
        thirdValue = numberTrio[2].toDecimal() if len(numberTrio) > 2 else 0
        results = {"A": firstValue, "B": secondValue, "C": thirdValue}
        self.__values = {"A": firstValue, "B": secondValue, "C": thirdValue}
        letter = alpha[self.parseFormula(self.__raw, results) - 1]
        self.__result = results[letter]

    def evaluateMatrixFormula(self, matrices: ArrayType[ArrayType[ArrayType[int]]]) -> None:
        """Reemplaza las variables de la fórmula con las matrices.

        Args:
            matrices (ArrayType[ArrayType[ArrayType[int]]]): Matrices a evaluar.
        """
        firstMatrix = matrices[0]
        secondMatrix = matrices[1] if len(matrices) > 1 else np.array([])
        thirdMatrix = matrices[2] if len(matrices) > 2 else np.array([])
        results = {"A": firstMatrix, "B": secondMatrix, "C": thirdMatrix}
        self.__values = {"A": firstMatrix, "B": secondMatrix, "C": thirdMatrix}
        letter = alpha[self.parseFormula(self.__raw, results) - 1]
        self.__result = self.__formatMatrix(results[letter])

    def getRaw(self) -> str:
        """Devuelve la fórmula en texto plano.

        Returns:
            str: Fórmula en texto plano.
        """
        return self.__raw

    def getResult(self) -> str:
        """Devuelve el resultado de la evaluación de la fórmula.

        Returns:
            str: Resultado de la evaluación de la fórmula.
        """
        return self.__result

    def isValid(self) -> bool:
        """Devuelve si la fórmula es válida.

        Returns:
            bool: Indica si la fórmula es válida.
        """
        return self.__isValid

    def isMatrix(self) -> bool:
        """Devuelve si la fórmula es una matriz.

        Returns:
            bool: Indica si la fórmula es una matriz.
        """
        return self.__isMatrix

    def parseFormula(self, formula: str, results: dict[str, str | ArrayType[ArrayType[int]]], resultsCount: int = 0) -> int:
        """Calcula el resultado de la formula a partir de la variables

        Args:
            formula (str): La formula original
            results (dict): Diccionario con los valores de las variables iniciales y calculadas
            resultsCount (int): Contador para llevar la cantidad de variables calculadas de la formula

        Returns:
            int: La posicion del resultado final de la formula
        """
        while "(" in formula and ")" in formula:
            formula, resultsCount = self.__calcParenthesis(formula, results, resultsCount)
        for operator in np.array(["*", "/", "+", "-"]):
            while formula.find(operator) != -1:
                n = formula.find(operator)
                op1 = None
                op2 = None
                if formula[n - 1] in results:
                    if not self.__isMatrix:
                        op1 = float(results[formula[n - 1]])
                    else:
                        op1 = results[formula[n - 1]]
                else:
                    op1 = float(formula[n - 1])

                if formula[n + 1] in results:
                    if not self.__isMatrix:
                        op2 = float(results[formula[n + 1]])
                    else:
                        op2 = results[formula[n + 1]]
                else:
                    op2 = float(formula[n + 1])

                if operator == "*":
                    if self.__isMatrix:
                        results[alpha[resultsCount]] = multiMatrices(op1, op2)
                    else:
                        results[alpha[resultsCount]] = op1 * op2
                    results[alpha[resultsCount]] = op1 * op2
                elif operator == "/":
                    if self.__isMatrix:
                        results[alpha[resultsCount]] = divideMatrices(op1, op2)
                    else:
                        results[alpha[resultsCount]] = op1 / op2
                elif operator == "+":
                    if self.__isMatrix:
                        results[alpha[resultsCount]] = sumaMatrices(op1, op2)
                    else:
                        results[alpha[resultsCount]] = op1 + op2
                elif operator == "-":
                    if self.__isMatrix:
                        results[alpha[resultsCount]] = restaMatrices(op1, op2)
                    else:
                        results[alpha[resultsCount]] = op1 - op2
                formula = formula.replace(
                    f"{formula[n - 1]}{formula[n]}{formula[n + 1]}", alpha[resultsCount])
                resultsCount += 1
        return resultsCount

    def getValues(self) -> dict[str, str]:
        """Devuelve el diccionario con las variables iniciales de la formula

        Returns:
            dict: Diccionario
        """
        return self.__values

    def __calcParenthesis(self, formula: str, results: dict[str, str], resultsCount: int) -> tuple[str, int]:
        """Extrae el contenido de los paréntesis y los calcula

        Args:
            formula (str): La formula original
            results (dict): Diccionario con los valores de las variables iniciales y calculadas
            resultsCount (int): Contador para llevar la cantidad de variables calculadas de la formula

        Returns:
            tuple[str, int]: La formula sin los paréntesis y el nuevo contador de resultados
        """
        insideParenthesis = ""
        for char1 in formula:
            if char1 == "(":
                textAux = formula[formula.find(char1) + 1:]
                closeParenthesis = False
                i = 0
                while not closeParenthesis:
                    if textAux[i] == "(":
                        i = textAux.find(")", i + 1) + 1
                    elif textAux[i] == ")":
                        closeParenthesis = True
                        insideParenthesis = textAux[:i]
                    else:
                        i += 1
        resultsCount = self.parseFormula(insideParenthesis, results, resultsCount)
        formula = formula.replace(f"({insideParenthesis})", alpha[resultsCount - 1])
        return formula, resultsCount

    def __formatMatrix(self, matrix: ArrayType[ArrayType[int]]) -> str:
        matrixString = ""
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrixString = f"{matrixString}{matrix[i][j]}|"
            matrixString = f"{matrixString}\n"
        return matrixString
