# Tree

* [content](#content)
  * [Recursion](#Recursion)







## Recursion

### 1. Simple Traversal

94\. Binary Tree Inorder Traversal

**Solution:**

```python
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
```





### 2. Depth of Tree

104\. Maximum Depth of Binary Tree

**Solution: **

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```





### 3. Balanced Tree

110\. Balanced Binary Tree

