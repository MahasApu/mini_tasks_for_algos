from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        extra_jump = 0
        try:
            for index in range(len(nums)):
                if index > extra_jump:
                    return False
                jump = nums[index]
                start_pointer = index + jump
                extra_jump = max(extra_jump, start_pointer)
            return True
        except IndexError:
            return True
