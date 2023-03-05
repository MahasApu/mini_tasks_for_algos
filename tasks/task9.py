import random


def classic_mult_matrix(matrix1, matrix2):
    assert len(matrix1) == len(matrix2)
    assert len(matrix1[0]) == len(matrix2[1])

    length = len(matrix1)
    result = [[0 for i in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def printer(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


if __name__ == "__main__":
    size = 3
    matrix1 = [[random.randint(1, 11) for j in range(size)] for i in range(size)]
    matrix2 = [[random.randint(1, 11) for j in range(size)] for i in range(size)]
    printer(classic_mult_matrix(matrix1, matrix2))
