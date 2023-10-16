class Solution:

    def numTrees(self, n: int) -> int:
        tree_counter = [1 if i < 2 else 0 for i in range(n + 1)]

        for amount in range(2, n + 1):
            for leftSize in range(amount):
                rightSize = amount - 1 - leftSize
                tree_counter[amount] += tree_counter[leftSize] * tree_counter[rightSize]
        return tree_counter[n]
