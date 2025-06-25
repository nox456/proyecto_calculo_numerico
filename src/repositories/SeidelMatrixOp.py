import numpy as np
from helpers.arrays import appendArray
from validations.operations import validateGaussOperation


class SeidelMatrixOp:
    __matrices = np.array([])

    def __init__(self, mat):
        if len(mat) == 0:
            raise ValueError("Error: No hay matrices")
        else:
            self.__matrices = mat

    # Setters
    def setMatrix(self, matrix):
        if matrix is None:
            raise ValueError("Error: Es necesario tener las matrices")
        elif len(matrix) == 0:
            raise ValueError("Error: No hay matrices")
        else:
            self.__matrices = matrix

    # Getters
    def getMatrix(self):
        return self.__matrices

    # Métodos
    def operation(self, matrix, tol=1e-10, max_iter=1500):
        A = np.array(matrix, dtype=float)
        n = len(A)
        x = np.zeros(n)
        if not self.isDominant(A):
            A_new = self.convertDominant(A)
            if A_new is None:
                raise ValueError(
                    "No se pudo convertir la matriz a diagonalmente dominante")
            else:
                A = A_new
        for iteration in range(max_iter):
            x_old = x.copy()
            for i in range(n):
                if A[i, i] == 0:
                    raise ValueError(f"División por cero en la fila {i}")
                suma = 0.0
                for j in range(n):
                    if j != i:
                        suma += A[i, j] * x[j]
                x[i] = (A[i, -1] - suma) / A[i, i]
            diff = max(abs(x[i] - x_old[i]) for i in range(n))
            if diff < tol:
                break
        return x

    def isDominant(self, matrix):
        n = len(matrix)
        for i in range(n):
            diag = abs(matrix[i][i])
            for j in range(n):
                if j != i:
                    if diag < abs(matrix[i][j]) or diag < abs(matrix[j][i]):
                        return False
        return True

    def convertDominant(self, matrix):
        n = len(matrix)
        for i in range(n):
            maxVal = -1
            maxIndex = i
            for j in range(n):
                currentAbs = abs(matrix[i][j])
                if currentAbs > maxVal:
                    maxVal = currentAbs
                    maxIndex = j
            if maxIndex != i:
                matrix[[i, maxIndex]] = matrix[[maxIndex, i]]
        if not self.isDominant(matrix):
            raise ValueError(
                f"No es posible realizar esta operacion.")
        return matrix

    def addToMatrix(self, matrix):
        matrixAux = np.zeros((len(matrix), len(matrix[0]) + 1))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrixAux[i][j] = matrix[i][j]
            matrixAux[i][-1] = 1
        return matrixAux

    def cantMatrx(self):
        return len(self.__matrices)

    def checkMatrix(self, matrix):
        if not isinstance(matrix, (np.ndarray)):
            raise ValueError("La matriz debe ser un arreglo de NumPy.")
        if len(matrix) != len(matrix[0]):
            return "Al no ser una matriz cuadrada, tendrá o infinitas soluciones o ninguna solución"
        return ""

    def startOperation(self):
        results = np.array([])
        for matrix in self.__matrices:
            result = self.checkMatrix(matrix)
            if result != "":
                return result
            matrix = self.addToMatrix(matrix)
            np.set_printoptions(suppress=True, precision=3, floatmode='fixed')
            result = validateGaussOperation(self, matrix)
            results = appendArray(results, result)
        return results
