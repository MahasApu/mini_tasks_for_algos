import random
from benchmarker import format_table

from time import time


def get_time(funcs, **kwargs):
    times = 10

    def time_wrapper(func, **kwargs):
        start_time = time()
        func(kwargs)
        end_time = time()
        total_time = end_time - start_time
        return total_time

    def sample_mean(func, **kwargs):
        counter, summ = 1, 0
        while counter <= times:
            summ += time_wrapper(func, **kwargs)
            counter += 1

        return f'{(summ / times):.5f}s'

    def standard_deviation(func, **kwargs):
        counter, summ, summ_2 = 1, 0, 0
        while counter <= times:
            exec_time = time_wrapper(func, **kwargs)
            summ += exec_time
            summ_2 += exec_time ** 2
            counter += 1

        pivot = summ / times
        pivot_quadr = summ_2 / times
        deviation = (pivot_quadr - pivot ** 2) ** 0.5
        return f'{(deviation):.5f}s'

    def geometric_mean(func, **kwargs):
        counter, product = 1, 1
        power = 1 / times
        while counter <= times:
            product *= time_wrapper(func, **kwargs)
            counter += 1
        result = product ** power

        return f'{(result):.5f}s'

    result = []
    for func in funcs:
        result.append([sample_mean(func, **kwargs), standard_deviation(func, **kwargs), geometric_mean(func, **kwargs)])

    format_table(benchmarks=['naive matrix mult'],
                 algos=['sample mean', 'standard deviation', 'geometric mean'],
                 results=result)


'''
    Sub functions for matrix
'''


def plus_matrix(matrix1, matrix2):
    row_len1 = len(matrix1[0])
    column_len1 = len(matrix1)
    row_len2 = len(matrix2[0])
    column_len2 = len(matrix2)

    assert row_len1 == column_len2

    result = [[0 for _ in range(row_len1)] for _ in range(column_len1)]
    for i in range(column_len1):
        # iterate through columns
        for j in range(row_len1):
            result[i][j] += matrix2[i][j] + matrix1[i][j]

    return result


def minus_matrix(matrix1, matrix2):
    row_len1 = len(matrix1[0])
    column_len1 = len(matrix1)
    row_len2 = len(matrix2[0])
    column_len2 = len(matrix2)

    assert row_len1 == column_len2

    result = [[0 for _ in range(row_len1)] for _ in range(column_len1)]
    for i in range(column_len1):
        # iterate through columns
        for j in range(row_len1):
            result[i][j] += matrix2[i][j] - matrix1[i][j]


def classic_mult_matrix(kwargs):
    matrix1 = kwargs['matrix1']
    matrix2 = kwargs['matrix2']

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


def eight_rec_mult_matrix(matrix1, matrix2):
    assert len(matrix1) == len(matrix2)
    assert len(matrix1[0]) == len(matrix2[1])

    # check if the size of matrix is not equal to any of power of two
    # then extend the size by adding zeros


def printer(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


if __name__ == "__main__":
    size = 64
    m1 = [[random.randint(1, 11) for j in range(size)] for i in range(size)]
    m2 = [[random.randint(1, 11) for j in range(size - size // 2)] for i in range(size)]
    E = [[0 if j != i else 1 for j in range(size)] for i in range(size)]
    get_time([classic_mult_matrix], matrix1=m1, matrix2=E)
