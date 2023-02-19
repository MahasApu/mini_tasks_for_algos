'''По заданному массиву количества цитирований статей
рассчитать индекс Хирша исследователя.

Решить задачу необходимо на литкоде:
https://leetcode.com/problems/h-index/

Встроенные сортировки использовать нельзя.

За реализацию сортировки Shell-а со сложностью лучше
квадратичной начисляется дополнительный балл. '''


def swap(arr, ind_1, ind_2):
    temp = arr[ind_1]
    arr[ind_1] = arr[ind_2]
    arr[ind_2] = temp


def insertion_sort_k(array, k):
    for i in range(k - 1, len(array)):
        j = i
        while j - k >= 0 and array[j - k] < array[j]:
            swap(array, j - k, j)
            j -= k
    return array


def ceil(num_1, num_2):
    return (num_1 + num_2 + 1) // num_2


def shell_sort(array):
    a = [(3 ** i - 1) // 2 for i in range(len(array)//3 + 1 ) if i >= 1]
    for elem in a:
        if elem <= ceil(len(array), 2):
            insertion_sort_k(array, elem)
    return array


def find_h_index(array):
    if array[len(array) - 1] >= len(array):
        return len(array)
    for i in range(len(array)):
        if array[i] < i + 1:
            return i
    return 0

def checker(arr):
    return find_h_index(shell_sort(arr))