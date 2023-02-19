def wiggle_sort(nums):
    pivot = len(nums) // 2
    while pivot:
        for i in range(pivot, len(nums)):
            temp = nums[i]
            j = i
            while j >= pivot and nums[j - pivot] > temp:
                nums[j] = nums[j - pivot]
                j -= pivot
            nums[j] = temp
        pivot //= 2

    right = len(nums) - 1
    pivot = (len(nums) - 1) // 2

    temp = [0 for i in range(len(nums))]

    for i in range(1, len(nums), 2):
        temp[i] = nums[right]
        right -= 1
    for i in range(0, len(nums), 2):
        temp[i] = nums[pivot]
        pivot -= 1

    for i in range(len(nums)):
        nums[i] = temp[i]
    return nums
