from typing import List, Optional


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def dfs(node, hight: int):
            if node:
                if hight >= len(result):
                    result.append(node.val)
                else:
                    result[hight] = node.val
                dfs(node.left, hight + 1)
                dfs(node.right, hight + 1)

        dfs(root, 0)
        return result
