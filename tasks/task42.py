from typing import List


class SegmentTree:

    def __init__(self, nums: List[int]):

        self.amount = len(nums)
        self.t = [0] * (4 * self.amount)
        self.build(nums, 1, 0, self.amount - 1)

    def build(self, nums, v: int, tl: int, tr: int):

        if tl == tr:
            self.t[v] = nums[tl]
            return
        tm = (tl + tr) >> 1
        self.build(nums, v * 2, tl, tm)
        self.build(nums, v * 2 + 1, tm + 1, tr)
        self.t[v] = self.t[v * 2] + self.t[v * 2 + 1]

    def update(self, index: int, value: int, v: int, tl: int, tr: int):

        if tl == tr:
            self.t[v] = value
            return

        tm = (tl + tr) >> 1
        if index <= tm:
            self.update(index, value, v * 2, tl, tm)
        else:
            self.update(index, value, v * 2 + 1, tm + 1, tr)
        self.t[v] = self.t[v * 2] + self.t[v * 2 + 1]

    def getSum(self, v: int, tl: int, tr: int, l: int, r: int) -> int:

        if l == tl and r == tr:
            return self.t[v]
        tm = (tl + tr) >> 1
        res = 0

        if l <= tm:
            res += self.getSum(v * 2, tl, tm, l, min(r, tm))
        if r >= tm + 1:
            res += self.getSum(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r)

        return res


class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val, 1, 0, self.tree.amount - 1)

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.getSum(1, 0, self.tree.amount - 1, left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
