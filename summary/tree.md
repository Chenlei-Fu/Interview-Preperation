# Tree
## Content
- [Tree](#tree)
  - [Content](#content)
  - [Recursion](#recursion)
    - [1. Simple Traversal](#1-simple-traversal)
    - [2. Depth of Tree](#2-depth-of-tree)
    - [3. Balanced Tree](#3-balanced-tree)
    - [4. max path (diameter)](#4-max-path-diameter)
    - [5. Inversion](#5-inversion)
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
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        method2: iteration
        """
        stack, res = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res
```



**Follow ups**

Inorder v.s Preorder v.s Postorder

![tree12](https://media.geeksforgeeks.org/wp-content/cdn-uploads/2009/06/tree12.gif)

* Inorder (Left, Root, Right) : 4 2 5 1 3 
* Preorder (Root, Left, Right) : 1 2 4 5 3 
* Postorder (Left, Right, Root) : 4 5 2 3 1



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



[366. Find Leaves of Binary Tree](https://leetcode.com/problems/find-leaves-of-binary-tree/)

Use the height (depth) as the index of the return array

```python
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.height(root, res)
        return res
    
    def height(self, root, res):
        if not root: return -1
        level = 1 + max(self.height(root.left, res), self.height(root.right, res))
        if len(res) == level: res.append([]) # no enough space to store
        res[level].append(root.val)
        return level
```





### 3. Balanced Tree

110\. [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

```python
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
# ================================================
# similar ideas:
#     def isBalanced(self, root: TreeNode) -> bool:
#         if not root:
#             return True
#         l_height = self.getHeight(root.left)
#         r_height = self.getHeight(root.right)
#         return abs(l_height - r_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
#     def getHeight(self, root):
#         if not root:
#             return 0
#         return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
```



### 4. max path (diameter)

[543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

```python
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
        
```

**My Errors**

We cannot calculate the diameter directly. Instead, calculate the depth of left and right tree. The method is divide and conquer, because for a tree, we usually think about two branches seperately. So calculating the depth would be much more reusable for the code. 



### 5. Inversion

[226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(left)
        return root
```

