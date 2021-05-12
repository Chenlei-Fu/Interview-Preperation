# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        """
        iteration
        """
        stack, i, res = [root], 0, []
        while stack:
            node = stack.pop()
            if not node: continue
            if node.val != voyage[i]: return [-1]
            i += 1
            
            if node.left and node.left.val != voyage[i]:
                res.append(node.val) 
                stack.extend([node.left, node.right])
            else:
                stack.extend([node.right, node.left])
        return res
    
    # def __init__(self):
    #         self.i = 0
    #     self.res = []
        
    # def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
    #     """
    #     recursion
    #     """
    #     return self.res if self.dfs(root, voyage) else [-1]
    
    # def dfs(self, root, voyage):
    #     if not root: return True
    #     if root.val != voyage[self.i]: return False
    #     self.i += 1
    #     if root.left and root.left.val != voyage[self.i]:
    #         self.res.append(root.val)
    #         return self.dfs(root.right, voyage) and self.dfs(root.left, voyage)
    #     return self.dfs(root.left, voyage) and self.dfs(root.right, voyage)