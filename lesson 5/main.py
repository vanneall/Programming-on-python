import copy
import math


def smaldet(matrix: list):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def submatrix(matrix: list, i: int, j: int):
    resultMatrix = []
    offset = 0
    for row in range(len(matrix)):
        if row == i:
            offset += 1
            continue
        resultMatrix.append([])
        for column in range(len(matrix[row])):
            if column == j:
                continue
            resultMatrix[row - offset].append(matrix[row][column])
    return resultMatrix


def det(matrix: list, i: int = 0):
    if len(matrix) == 2:
        return smaldet(matrix)
    determinant = 0
    for j in range(len(matrix[0])):
        determinant += math.pow(-1, i + j) * matrix[i][j] * det(submatrix(matrix, i, j))
    return determinant


def minor(matrix: list, i: int, j: int):
    return det(submatrix(matrix, i, j))


def alg(matrix: list, i: int, j: int):
    return math.pow(-1, i + j) * minor(matrix, i, j)


def algamatrix(matrix: list):
    alg_matrix = []
    for i in range(len(matrix)):
        alg_matrix.append([])
        for j in range(len(matrix)):
            alg_matrix[i].append(alg(matrix, i, j))
    return alg_matrix


def transpose(matrix: list):
    res = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if i == j:
                continue
            else:
                res[i][j], res[j][i] = res[j][i], res[i][j]
    return res


def inv(matrix: list):
    alg_matrix_T = transpose(copy.deepcopy(algamatrix(copy.deepcopy(matrix))))
    det_matrix = det(matrix)
    for i in range(len(alg_matrix_T)):
        for j in range(len(alg_matrix_T[i])):
            alg_matrix_T[i][j] = alg_matrix_T[i][j] / det_matrix
    return alg_matrix_T


def multiply(matrix1: list, matrix2: list, row: int, column: int):
    res = 0
    for column_matrix1 in range(len(matrix1[0])):
        for row_matrix2 in range(column_matrix1, len(matrix2)):
            a = matrix1[row][column_matrix1]
            b = matrix2[row_matrix2][column]
            res += a * b
            break
    return res


def multiply_matrix(matrix1: list, matrix2: list):
    res_matrix = []
    for i_new_matrix in range(len(matrix1)):
        res_matrix.append([])
        for j_new_matrix in range(len(matrix1[i_new_matrix])):
            res_matrix[i_new_matrix].append(multiply(matrix1, matrix2, i_new_matrix, j_new_matrix))
    return res_matrix


def moore_penrose(matrix: list):
    return multiply_matrix(inv(multiply_matrix(transpose(copy.deepcopy(matrix)), matrix)),
                           transpose(copy.deepcopy(matrix)))


A = [[0, 2, 1, 4], [1, 0, 3, 2], [0, 1, 4, 0], [1, 2, 1, 1]]

print(inv(A))
print(moore_penrose(A))
