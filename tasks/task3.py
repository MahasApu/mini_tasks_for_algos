def search(nums, target):
    nums = sorted(nums)
    l = 0
    r = len(nums) - 1
    pivot = len(nums) // 2
    while nums[pivot] != target:
        if l > r:
            return -1
        elif target > nums[pivot]:
            l = pivot + 1
        elif target < nums[pivot]:
            r = pivot - 1
        pivot = (l + r) // 2
    if nums[pivot] == target:
        return pivot
