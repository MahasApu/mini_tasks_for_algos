from typing import List
import random
def swap(arr: List, ind1: int, ind2: int):
    temp = arr[ind1]
    arr[ind1] = arr[ind2]
    arr[ind2] = temp


def merge(arr: List, start1: int, end1: int, start2: int, end2: int, buff1: int, buff2: int):
    i, j, k = start1, start2, buff1
    while i <= end1 and j <= end2 and k <= buff2:

        if arr[i] <= arr[j]:
            swap(arr, i, k)
            i += 1
        else:
            swap(arr, j, k)
            j += 1
        k += 1

    while i <= end1 and k <= buff2:
        swap(arr, i, k)
        k += 1
        i += 1

    while j <= end2 and k <= buff2:
        swap(arr, j, k)
        k += 1
        j += 1


def merge_sort(array: List, start: int, end: int, buff1: int, buff2: int):

    if end - start <= 1:
        if array[start] > array[end]:
            swap(array, start, end )
        return

    if end - start > 0:
        middle = start + (end - start) // 2
        merge_in_place(array, start, middle)
        merge_in_place(array, middle + 1, end)
        merge(array, start, middle, middle + 1, end, buff1, buff2)


def merge_in_place(arr: List, start: int, end: int):
    middle = start + (end - start - 1) // 2
    merge_sort(arr, start, middle, middle + 1, end)
    pivot = middle

    while pivot > start:
        mid = start + (pivot - start - 1) // 2
        merge_sort(arr, mid, pivot, start, mid)
        merge(arr, start, mid, pivot + 1, end, mid + 1, end)
        pivot = mid

    if pivot <= start:
        for i in range(start, end + 1):
            j = i
            while j > start and arr[j - 1] > arr[j]:
                swap(arr, j - 1, j)
                j -= 1


def printer(arr: List):
    merge_in_place(arr, 0, len(arr) - 1)
    print(arr)


if __name__ == "__main__":
    arr1 = [11, 55, 4545, 342, 31, 35, 3, 6, 34, 4, 2, 33, 56, 7, 7, 45, 4, 55, 34, 22, 42, 1, 453, 34, 111,
            2, 56, 5, 879, 8, 7, 556, 3, 34, 34, 22, 3, 45, 3, -11, 5, 6, 56, 7, -12, 99, 7879, 4, 3, 4, 5, 4, 3, 9]

    arr2 = [607, 641, 431, 614, 438, -28, 326, -32, 609, 963, 943, 156, -63, 103, 465, 828, 70, 566, 260, 765, 540, -64,
            594, -85, 269, 735, 2, 214, 370, -57, 248, 187, 508, 496, 561, 861, 830]
    arr = [2, 1, 0, 8, 22, 12, 1, 0, 9, 13, 7, 88, 3, 99, 23, 9, 0]
    arr0 = [1, 13, 99, 51, 28, 91, 30, 34, 111, 56, 22, 37, 12, 1, 5, 15, 60]
    arr4 = [1, 13, 28, 51, 99, 30, 34, 91, 111, 121, 23, 56, 22, 37, 12, 1, 5, 15, 60]
    size = 1024
    arr5 = [random.randint(-100, 100) for j in range(size)]
    printer(arr5)
