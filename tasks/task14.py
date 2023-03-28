import random
from typing import List


def swap(arr: List[int], ind1: int, ind2: int):
    temp = arr[ind1]
    arr[ind1] = arr[ind2]
    arr[ind2] = temp


def lomuto_partition(array: List[int], pivot_index: int) -> int:
    swap(array, pivot_index, 0)
    pivot_index = 0
    i = 0
    for j in range(pivot_index + 1, len(array)):
        if array[j] > array[pivot_index]:
            i += 1
            swap(array, i, j)
    swap(array, pivot_index, i)
    return i


def kth(arr: List[int], k: int) -> int:
    if len(arr) <= 1:
        return arr[0]

    pivot = random.randint(0, len(arr) - 1)
    p = lomuto_partition(arr, pivot)

    if p + 1 == k:
        return arr[p]
    elif p + 1 > k:
        return kth(arr[:p], k)
    else:
        return kth(arr[p + 1:], k - p - 1)


def generate_rand_arr(size: int) -> List[int]:
    return [random.randint(1, 100) for __ in range(size)]


def sort_tester(array: List[int], k: int):
    print(kth(array, k))


if __name__ == '__main__':
    a = generate_rand_arr(15)
    print(a)
    sort_tester(a, 5)
