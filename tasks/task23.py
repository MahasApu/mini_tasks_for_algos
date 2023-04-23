from typing import List, Optional


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_valid(node, root_max, root_min):
            if not node:
                return True

            if node.val >= root_max or node.val <= root_min:
                return False

            if not is_valid(node.left, node.val, root_min):
                return False

            if not is_valid(node.right, root_max, node.val):
                return False

            return True

        return is_valid(root, float('inf'), float('-inf'))
