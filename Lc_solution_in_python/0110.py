class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        method: recursion
        """
        self.check = True
        self.maxDepth(root)
        return self.check

    def maxDepth(self, root):
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        if abs(l - r) > 1:
            self.check = False
        return 1 + max(l, r)