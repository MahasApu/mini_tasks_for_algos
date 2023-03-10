def swap(arr, ind1, ind2):
    temp = arr[ind1]
    arr[ind1] = arr[ind2]
    arr[ind2] = temp


def insertion_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        j = i
        while j > start and arr[j - 1] > arr[j]:
            swap(arr, j - 1, j)
            j -= 1


def merge(arr, start1, end1, start2, end2, buff1, buff2, buffer):
    # l_size = end1 - start1 + 1
    # r_size = end2 - start2 + 1
    # b_size = buff2 - buff1 + 1

    i, j, k = start1, start2, buff1
    while i <= end1 and j <= end2:

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


def merge_sort(array, start, end, buff1, buff2, buffer):
    if end - start > 0:
        middle = start + (end - start) // 2
        merge_in_place(array, start, middle)
        merge_in_place(array, middle + 1, end)
        merge(array, start, middle, middle + 1, end, buff1, buff2, buffer)


def merge_in_place(arr, start, end):
    middle = start + (end - start - 1) // 2
    merge_sort(arr, start, middle, middle + 1, len(arr) - 1, arr)

    if middle - start < 2:
        print(arr, "nn")
        for i in range(start, end + 1):
            j = i
            print(j, start, end + 1)
            while j > start and arr[j - 1] > arr[j]:
                swap(arr, j - 1, j)
                print(arr, "iii")
                j -= 1

        return

    pivot = middle

    while pivot - start > 2:
        mid = (pivot - start - 1) // 2
        merge_sort(arr, mid, pivot, start, len(arr) - 1, arr)
        merge(arr, start, mid, pivot + 1, end, mid + 1, len(arr) - 1, arr)
        pivot = mid


# def merge(arr, start, end, buf1, buf2):
#     middle = start + (end - start) // 2
#     merge_inplace(arr, start, middle)
#     merge_inplace(arr, middle + 1, end)
#
#     size = end - start + 1
#     r_size = end - middle
#     l_size = end - r_size
#
#     i, j, k = 0, 0, 0
#     while i < l_size and j < r_size:
#
#         if arr[i] < arr[j]:
#             swap(arr, i + start, k + buf1)
#             i += 1
#         else:
#             swap(arr, j + middle, k + buf1)
#             j += 1
#         k += 1
#
#     while i + start < l_size and k < buf2:
#         swap(arr, i, k)
#         k += 1
#         i += 1
#
#     while j + middle < r_size and k < buf2:
#         swap(arr, j, k)
#         k += 1
#         j += 1
#
#     return
#
#
# def merge_inplace(arr, start, end):
#     # if end - start == 0:
#     #     return
#     # if end - start == 1:
#     #     if arr[start] > arr[end]:
#     #         swap(arr, start, end)
#     # if end - start == 2:
#     #     for i in range(start , end + 1):
#     #             j = i
#     #             while j > start and arr[j - 1] > arr[j]:
#     #                 swap(arr, j - 1, j)
#     #                 j -= 1
#     #     return
#     pivot = (end - start) // 2
#     merge(arr, 0, pivot, pivot + 1, end)
#     merge(arr, pivot // 2 + 1, pivot, 0, pivot // 2)


def printer(arr):
    # merge_inplace(arr, 0, len(arr) - 1)
    merge_in_place(arr, 0, len(arr) - 1)
    print(arr)


if __name__ == "__main__":
    arr1 = [2, 55, 4545, 342, 31, 35, 3, 6, 34, 4, 2, 33, 56, 7, 7, 45, 4, 55, 34, 22, 42, 1, 453, 34, 111,
            2, 56, 5, 879, 8, 7, 556, 3, 34, 34, 22, 3, 45, 3, -11, 5, 6, 56, 7, -12, 99, 7879, 4, 3, 4, 5, 4, 3, 9]

    arr2 = [607, 641, 431, 614, 438, -28, 326, -32, 609, 963, 943, 156, -63, 103, 465, 828, 70, 566, 260, 765, 540, -64,
            594, -85, 269, 735,
            2, 214, 370, -57, 248, 187, 508, 496, 561, 861, 830]
    arr = [2, 1, 0, 8, 22, 12, 1, 0, 9, 13, 7, 88, 3, 99, 23, 9, 0]

    printer(arr)
