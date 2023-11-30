from typing import List


class FenwickTree:

    def __init__(self, arr):
        self.a = arr
        self.n = max(self.a) + 1
        self.s = [0 for _ in range(self.n)]

    def f(self, x: int) -> int:
        return x & (x + 1)

    def g(self, x: int) -> int:
        return x | (x + 1)

    def getPrefixSum(self, current_pos: int) -> int:
        answer = 0
        while current_pos >= 0:
            answer += self.s[current_pos]
            current_pos = self.f(current_pos) - 1
        return answer

    def increment(self, pos: int, val: int) -> int:
        while pos < self.n:
            self.s[pos] += val
            pos = self.g(pos)

    def update(self, pos: int, val: int) -> int:
        self.increment(val, val - self.a[pos])

    def sum(self, l: int, r: int) -> int:
        return self.getPrefixSum(r) - self.getPrefixSum(l - 1)


class Solution:

    def createSortedArray(self, instructions: List[int]) -> int:
        tree = FenwickTree(instructions)
        answer = 0
        for index, value in enumerate(instructions):
            answer += min(tree.getPrefixSum(value - 1), index - tree.getPrefixSum(value))
            tree.increment(value, 1)

        return answer % (10 ** 9 + 7)
