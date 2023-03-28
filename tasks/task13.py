import random
from benchmarker import format_table

with open("C:/Users/vaskm/OneDrive/Рабочий стол/2022/tasks for C/for_algos/for_algos/output.txt", "r") as file:
    data = file.readlines()
    new_data = []
    for line in data:
        new_data.append(line.split())


def get_time(data, amount):

    def sample_mean(arr, amount):
        summ = 0
        for mark in arr:
            summ += float(mark)
        return f'{(summ / amount):.7f}s'

    def standard_deviation(arr, amount):
        summ, summ_2 = 0, 0
        for mark in arr:
            exec_time = float(mark)
            summ += exec_time
            summ_2 += exec_time ** 2

        pivot = summ / amount
        pivot_quadr = summ_2 / amount
        deviation = (pivot_quadr - pivot ** 2) ** 0.5
        return f'{(deviation):.7f}s'

    def geometric_mean(arr, amount):
        product = 1
        power = 1 / amount
        for mark in arr:
            product *= float(mark)

        result = product ** power
        return f'{(result):.7f}s'

    result = []
    for marks in data:
        result.append([sample_mean(marks, amount), standard_deviation(marks, amount), geometric_mean(marks, amount)])
    result.append([0,0,0])
    format_table(benchmarks=['Hoare partition', 'branch-free Lomuto partition', 'classic Lomuto partition'],
                 algos=['sample mean', 'standard deviation', 'geometric mean'],
                 results=result)


get_time(new_data, len(new_data[0]))