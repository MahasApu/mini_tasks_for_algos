class Solution:

    def __init__(self):
        self.h_dict = {}

    def height_getter(self, node: 'TreeNode') -> int:
        if not node:
            return 0
        left = self.height_getter(node.left)
        right = self.height_getter(node.right)
        return 1 + max(left, right)

    def get_balance(self, node: 'TreeNode'):
        if not node:
            return 0
        return self.height_getter(node.left) - self.height_getter(node.right)

    def left_rotation(self, node: 'TreeNode') -> 'TreeNode':
        if not node:
            return node

        right = node.right
        node.right = right.left
        right.left = node
        return right

    def right_rotation(self, node: 'TreeNode') -> 'TreeNode':
        if not node:
            return node

        left = node.left
        node.left = left.right
        left.right = node
        return left

    def nice_rotation(self, root):
        if not root:
            return root

        root.left = self.nice_rotation(root.left)
        root.right = self.nice_rotation(root.right)

        if self.get_balance(root) > 1:
            if self.get_balance(root.left) < 1:
                root.left = self.left_rotation(root.left)
            return self.nice_rotation(self.right_rotation(root))

        elif self.get_balance(root) < -1:
            if self.get_balance(root.right) < -1:
                root.right = self.right_rotation(root.right)
            return self.nice_rotation(self.left_rotation(root))
        return root

    def balanceBST(self, root: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        return self.nice_rotation(root)
