# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def dfs(node: 'TreeNode'):
            if not node:
                yield ''
            else:
                yield from dfs(node.left)
                yield from dfs(node.right)
                yield str(node.val)

        return ','.join(dfs(root))

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def _dfs(_data):
            val = _data.pop()
            if not val:
                return
            n = TreeNode(val)
            n.right, n.left = _dfs(_data), _dfs(_data)
            return n

        return _dfs(data.split(','))
