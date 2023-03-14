import random
from benchmarker import format_table
import types

from time import time


def get_time(funcs, *args):
    times = 10
    def time_wrapper(func, *args):
        start_time = time()
        func(args)
        end_time = time()
        total_time = end_time - start_time
        return total_time

    def sample_mean(func, *args):
        counter, summ = 1, 0
        while counter <= times:
            summ += time_wrapper(func, *args)
            counter += 1
        return f'{(summ / times):.7f}s'

    def standard_deviation(func, *args):
        counter, summ, summ_2 = 1, 0, 0
        while counter <= times:
            exec_time = time_wrapper(func, *args)
            summ += exec_time
            summ_2 += exec_time ** 2
            counter += 1

        pivot = summ / times
        pivot_quadr = summ_2 / times
        deviation = (pivot_quadr - pivot ** 2) ** 0.5
        return f'{(deviation):.7f}s'

    def geometric_mean(func, *args):
        counter, product = 1, 1
        power = 1 / times
        while counter <= times:
            product *= time_wrapper(func, *args)
            counter += 1
        result = product ** power
        return f'{(result):.7f}s'

    result = []
    for func in funcs:
        result.append([sample_mean(func, *args), standard_deviation(func, *args), geometric_mean(func, *args)])

    format_table(benchmarks=['naive matrix mult', 'quick matrix mult', 'strassen algorithm'],
                 algos=['sample mean', 'standard deviation', 'geometric mean'],
                 results=result)


'''
    Sub functions for matrix
'''


def plus_matrix(matrix1, matrix2):
    if len(matrix1) > 1 and len(matrix2) > 1:

        row_len1 = len(matrix1[0])
        column_len1 = len(matrix1)
        row_len2 = len(matrix2[0])
        column_len2 = len(matrix2)

        assert row_len1 == column_len2

        result = [[0 for _ in range(row_len1)] for _ in range(column_len1)]
        for i in range(column_len1):
            for j in range(row_len1):
                result[i][j] += matrix1[i][j] + matrix2[i][j]

        return result
    else:
        if isinstance(matrix1[0], list):
            return [[matrix1[0][0] + matrix2[0][0]]]
        else:
            return [matrix1[0] + matrix2[0]]


def minus_matrix(matrix1, matrix2):
    if len(matrix1) > 1 and len(matrix2) > 1:

        row_len1 = len(matrix1[0])
        column_len1 = len(matrix1)
        row_len2 = len(matrix2[0])
        column_len2 = len(matrix2)

        assert row_len1 == column_len2

        result = [[0 for _ in range(row_len1)] for _ in range(column_len1)]
        for i in range(column_len1):
            for j in range(row_len1):
                result[i][j] += matrix1[i][j] - matrix2[i][j]

        return result
    else:

        if isinstance(matrix1[0], list):
            return [[matrix1[0][0] - matrix2[0][0]]]
        else:
            return [matrix1[0] - matrix2[0]]


def mult_matrix(matrix1, matrix2):
    if len(matrix1) > 1 and len(matrix2) > 1:
        row_len1 = len(matrix1[0])
        column_len1 = len(matrix1)
        row_len2 = len(matrix2[0])
        column_len2 = len(matrix2)

        assert row_len1 == column_len2

        result = [[0 for _ in range(row_len2)] for _ in range(column_len1)]

        for i in range(column_len1):
            for j in range(row_len2):
                for k in range(column_len2):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

        return result
    else:
        return [matrix1[0] * matrix2[0]]


def divide_matrix(matrix):
    column_len = len(matrix)
    row_len = len(matrix[0])
    mid_column = column_len // 2
    mid_row = row_len // 2

    matrix_11 = [M[:mid_column] for M in matrix[:mid_row]]
    matrix_12 = [M[mid_column:] for M in matrix[:mid_row]]
    matrix_21 = [M[:mid_column] for M in matrix[mid_row:]]
    matrix_22 = [M[mid_column:] for M in matrix[mid_row:]]

    return matrix_11, matrix_12, matrix_21, matrix_22


def merge_matrix(matrix_11, matrix_12, matrix_21, matrix_22):
    matrix_total = []
    column_len1 = len(matrix_11)
    column_len2 = len(matrix_21)

    if column_len1 > 1:
        for i in range(column_len1):
            matrix_total.append(matrix_11[i] + matrix_12[i])

        for j in range(column_len2):
            matrix_total.append(matrix_21[j] + matrix_22[j])
    else:

        matrix_total.append(matrix_11 + matrix_12)
        matrix_total.append(matrix_21 + matrix_22)

    return matrix_total


def classic_mult_matrix(args):
    if isinstance(args, tuple):
        matrix1 = args[0]
        matrix2 = args[1]
    else: return

    row_len1 = len(matrix1[0])
    column_len1 = len(matrix1)
    row_len2 = len(matrix2[0])
    column_len2 = len(matrix2)

    assert row_len1 == column_len2

    result = [[0 for _ in range(row_len2)] for _ in range(column_len1)]

    for i in range(column_len1):
        for j in range(row_len2):
            for k in range(column_len2):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def extend_matrix_size(matrix):
    length = len(matrix)
    power_two = 1
    while power_two < length:
        power_two <<= 1
    return power_two


def quick_mult_matrix(args):
    if isinstance(args, tuple):
        matrix1 = args[0]
        matrix2 = args[1]
    else: return

    column_len1 = len(matrix1)
    column_len2 = len(matrix2)

    assert column_len1 == column_len2

    if column_len1 == 1 and column_len2 == 1:
        return [matrix1[0][0] * matrix2[0][0]]
    elif column_len1 <= 128 and column_len2 <= 128:
        return mult_matrix(matrix1, matrix2)
    else:
        A, B, C, D = divide_matrix(matrix1)
        E, F, G, H = divide_matrix(matrix2)

        AE = quick_mult_matrix((A, E))
        BG = quick_mult_matrix((B, G))
        AF = quick_mult_matrix((A, F))
        BH = quick_mult_matrix((B, H))
        CE = quick_mult_matrix((C, E))
        DG = quick_mult_matrix((D, G))
        CF = quick_mult_matrix((C, F))
        DH = quick_mult_matrix((D, H))

        AE_plus_BG = plus_matrix(AE, BG)
        AF_plus_BH = plus_matrix(AF, BH)
        CE_plus_DG = plus_matrix(CE, DG)
        CF_plus_DH = plus_matrix(CF, DH)

        result = merge_matrix(AE_plus_BG, AF_plus_BH, CE_plus_DG,
                              CF_plus_DH)
        return result


def strassen_algorithm(args):
    if isinstance(args, tuple):
        matrix1 = args[0]
        matrix2 = args[1]
    else: return

    column_len1 = len(matrix1)
    column_len2 = len(matrix2)

    assert column_len1 == column_len2

    if column_len1 == 1 and column_len2 == 1:
        return [matrix1[0][0] * matrix2[0][0]]
    elif column_len1 <= 128 and column_len2 <= 128:
        return mult_matrix(matrix1, matrix2)


    else:
        A, B, C, D = divide_matrix(matrix1)
        E, F, G, H = divide_matrix(matrix2)

        F_H = minus_matrix(F, H)
        A_B = plus_matrix(A, B)
        C_D = plus_matrix(C, D)
        G_E = minus_matrix(G, E)
        A_D = plus_matrix(A, D)
        E_H = plus_matrix(E, H)
        B_D = minus_matrix(B, D)
        G_H = plus_matrix(G, H)
        A_C = minus_matrix(A, C)
        E_F = plus_matrix(E, F)

        P1 = strassen_algorithm((A, F_H))
        P2 = strassen_algorithm((A_B, H))
        P3 = strassen_algorithm((C_D, E))
        P4 = strassen_algorithm((D, G_E))
        P5 = strassen_algorithm((A_D, E_H))
        P6 = strassen_algorithm((B_D, G_H))
        P7 = strassen_algorithm((A_C, E_F))

        Q1 = plus_matrix(plus_matrix(P5, P4), minus_matrix(P6, P2))
        Q2 = plus_matrix(P1, P2)
        Q3 = plus_matrix(P3, P4)
        Q4 = plus_matrix(minus_matrix(P1, P3), minus_matrix(P5, P7))

        result = merge_matrix(Q1, Q2, Q3, Q4)
        return result


def printer(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


if __name__ == "__main__":
    size = 512
    m1 = [[random.randint(1, 2) for j in range(size)] for i in range(size)]
    m2 = [[random.randint(1, 2) for j in range(size)] for i in range(size)]
    E = [[0 if j != i else 1 for j in range(size)] for i in range(size)]
    get_time([classic_mult_matrix, quick_mult_matrix, strassen_algorithm], m1, m2)


