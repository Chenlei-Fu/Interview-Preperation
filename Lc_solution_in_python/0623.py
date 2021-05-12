# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        """
        method 1: BFS
        """
        # dummy, dummy.left = TreeNode(None), root
        # row = [dummy]
        # for _ in range(d - 1):
        #     row = [kid for node in row for kid in (node.left, node.right) if kid]
        #
        # for node in row:
        #     node.left, node.left.left = TreeNode(v), node.left
        #     node.right, node.right.right = TreeNode(v), node.right
        # return dummy.left

        """
        method 2: DFS
        """
        if not root or d <= 0:
            return None
        if d == 1:
            return TreeNode(v, root, None)
        if d == 2:
            root.left = TreeNode(v, root.left, None)
            root.right = TreeNode(v, None, root.right)
            return root

        root.left = self.addOneRow(root.left, v, d - 1)
        root.right = self.addOneRow(root.right, v, d - 1)
        return root


