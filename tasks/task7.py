def swap(arr, ind1, ind2):
    temp = arr[ind1]
    arr[ind1] = arr[ind2]
    arr[ind2] = temp


def merge(arr, start1, end1, start2, end2, buff1, buff2, buffer):
    # lsize = end1 - start1
    # rsize = end2 - start2
    # bsize = buff2 - buff1

    i, j, k = start1, start2, buff2
    while i < end1 and j < end2:

        if arr[i] < arr[j]:
            swap(arr, i, k)
            i += 1
        else:
            swap(arr, j, k + buff1)
            j += 1
        k += 1

    while i + start1 < end1 and k + buff1 < buff2:
        swap(arr, i + start1, k + buff1)
        k += 1
        i += 1

    while j + start2 < end2 and k + buff1 < buff2:
        swap(arr, j + start2, k + buff1)
        k += 1
        j += 1


def merge_sort(array, start, end, buff1, buff2, buffer):
    if end - start == 0:
        return
    if end - start == 1:
        if array[0] > array[1]:
            swap(array, 0, 1)
        return

    if end - start > 1:
        middle = start + (end - start) // 2

        merge_sort(array, 0, middle, buff1, buff2, buffer)
        merge_sort(array, middle + 1, end, buff1, buff2, buffer)
        merge(array, 0, middle, middle + 1, end, buff1, buff2, buffer)


def merge_in_place(arr, start, end):
    if end - start == 0:
        return
    if end - start == 1:
        if arr[0] > arr[1]:
            swap(arr, 0, 1)
        return

    pivot = (end - start) // 2
    merge_sort(arr, 0, pivot, pivot+1, end, arr)

    while pivot > 0:
        mid = (pivot) // 2
        merge_sort(arr, 0, mid, mid + 1, end, arr)
        merge(arr, 0, mid, pivot, end, mid, end, arr)
        pivot = mid


def printer(arr):
    merge_in_place(arr, 0, len(arr) - 1)
    print(arr)


if __name__ == "__main__":

    arr1 = [2, 55, 4545, 342, 31, 35, 3, 6, 34, 4, 2, 33, 56, 7, 7, 45, 4, 55, 34, 22, 42, 1, 453, 34, 111,
            2, 56, 5, 879, 8, 7, 556, 3, 34, 34, 22, 3, 45, 3, -11, 5, 6, 56, 7, -12, 99, 7879, 4, 3, 4, 5, 4, 3, 9]

    arr2 = [607, 641, 431, 614, 438, -28, 326, -32, 609, 963, 943, 156, -63, 103, 465, 828, 70, 566, 260, 765, 540, -64,
            594, -85, 269, 735,
            2, 214, 370, -57, 248, 187, 508, 496, 561, 861, 830]
    arr = [2, 1, 8, 11, 22, 12, 1, 0, 9, 13]

    printer(arr)
