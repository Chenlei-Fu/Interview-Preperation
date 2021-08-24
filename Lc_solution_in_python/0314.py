from collections import defaultdict
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        q: queue
        col_nodes = map<col, list<node>>
        """
        if not root:
            return []
        q = deque([(root, 0)])
        col_nodes, min_col, max_col, res = defaultdict(list), 0, 0, []
        
        while q:
            node, col = q.popleft()
            col_nodes[col].append(node.val)
            if node.left:
                q.append((node.left, col-1))
                min_col = min(min_col, col-1)
            if node.right:
                q.append((node.right, col+1))
                max_col = max(max_col, col+1)
        
        for i in range(min_col, max_col+1):
            res.append(col_nodes[i])
        return res