# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        self.depth(root)
        return self.diameter

    def depth(self, root):
        """
        get the max depth of current root
        the result would be depth of left + depth of right (as the example)
        """
        if not root:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        self.diameter = max(self.diameter, l + r)
        return max(l, r) + 1
