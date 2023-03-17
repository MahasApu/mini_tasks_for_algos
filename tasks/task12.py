import random
from typing import List, Callable


def swap(array: List[int], ind1: int, ind2: int):
    temp = array[ind1]
    array[ind1] = array[ind2]
    array[ind2] = temp


def quick_sort(array: List[int], start: int, end: int, partition: Callable):
    if start >= end:
        return
    pivot = partition(array, start, end)
    quick_sort(array, start, pivot - 1, partition)
    quick_sort(array, pivot + 1, end, partition)


def lomuto_partition(array: List[int], start: int, end: int) -> int:
    pivot_index = random.randint(start, end)
    if pivot_index != start:
        swap(array, pivot_index, start)

    pivot = array[start]
    i = start
    for j in range(start, end + 1):
        if array[j] < pivot:
            i += 1
            swap(array, i, j)
    swap(array, start, i)
    return i


def hoare_partition(array: List[int], start: int, end: int) -> int:
    pivot_index = random.randint(start, end)
    if pivot_index != start:
        swap(array, pivot_index, start)

    pivot = array[start]
    i = start + 1
    j = end
    while True:
        while array[i] < pivot and i < end:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            break
        swap(array, i, j)
        i += 1
        j -= 1

    swap(array, start, j)
    return j


def generate_rand_arr(size: int) -> List[int]:
    return [random.randint(1, 100) for __ in range(size)]


def sort_tester(array: List[int], partition_name: Callable):
    quick_sort(array, 0, len(array) - 1, partition_name)


if __name__ == '__main__':
    arr = generate_rand_arr(100000)
    # sort_tester(arr, hoare_partition)
    sort_tester(arr, lomuto_partition)
    #print(arr)
