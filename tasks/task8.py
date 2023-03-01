
def isIdealPermutation(nums):

    def locals_inv(arr):
                if len(arr) == 1: return 0
                k=0
                for i in range(len(arr)-1):
                    if arr[i]>arr[i+1]:
                        k+=1
                return k


    def merge_count_inversion(arr):
        if len(arr) <= 1:
            return arr, 0
        middle = (len(arr) + 1) // 2
        left, l = merge_count_inversion(arr[:middle])
        right, r = merge_count_inversion(arr[middle:])
        split, s = merge_count_split_inversion(left, right)
        return split, (l + r + s)

    def merge_count_split_inversion(left, right):
        result = []
        count = 0
        i, j = 0, 0
        left_len = len(left)
        while i < left_len and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                count += left_len - i
                j += 1
        result += left[i:]
        result += right[j:]
        return result, count

    gl = merge_count_inversion(nums)[1]
    loc = locals_inv(nums)
    print(gl, loc)

    return gl == loc


if __name__ == "__main__":
    print(isIdealPermutation([2,0,1]))