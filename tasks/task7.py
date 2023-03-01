
# DMTA-like solution

def classic_merge(nums):
    def merge(array, start, middle, end):
        n1 = middle - start + 1
        n2 = end - middle

        b = []
        c = []
        for i in range(n1):
            b.append(array[start + i])

        for j in range(n2):
            c.append(array[middle + j + 1])

        i, j = 0, 0
        el = start
        while i < n1 and j < n2:
            if b[i] <= c[j]:
                array[el] = b[i]
                i += 1
            else:
                array[el] = c[j]
                j += 1
            el += 1
        while i < n1:
            array[el] = b[i]
            i += 1
            el += 1
        while j < n2:
            array[el] = c[j]
            j += 1
            el += 1

    def merge_sort(array, start, end):
        if start > end:
            return
        if start < end:
            middle = (start + end) // 2

            merge_sort(array, start, middle)
            merge_sort(array, middle + 1, end)

            print(start, middle, end)
            merge(array, start, middle, end)

    merge_sort(nums, 0, len(nums) - 1)
    return nums

# in-place merge

def in_place(nums):

    def swap(arr, ind1, ind2):
        temp = arr[ind1]
        arr[ind1] = arr[ind2]
        arr[ind2] = temp

    def merge_in_place(arr, start, end):
        length = end - start + 1
        mid = (length + 1) // 2
        while mid >= 1:
            pointer = start

            while pointer + mid <= end:
                if arr[pointer] > arr[pointer + mid]:
                    swap(arr, pointer, pointer + mid)
                pointer += 1

            if mid == 1:
                break
            mid = (mid + 1) // 2


    def merge(arr, start, end):

        if end - start < 1:
            return
        if end - start == 1:
            if arr[start] > arr[end]:
                return swap(arr, start, end)
            return

        mid = start + (end - start) // 2
        merge(arr, start, mid)
        merge(arr, mid, end)
        merge_in_place(arr, start, end)

    merge(nums, 0, len(nums) - 1)
    return nums

if __name__ == '__main__':
    print(classic_merge([3,6,34,4,2,33,56,7,7,5,45,4]))
    print(in_place([3, 6, 34, 4, 2, 33, 56, 7, 7, 5, 45, 4]))