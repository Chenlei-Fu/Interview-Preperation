class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        method1: recursion
        time: O(N)
        space: O(h) -> (stack)
        """
        res = []
        self.helper(root, res)
        return res
        
    def helper(self, root, res):
        if not root:
            return None
    
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)