# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        stack, num = [TreeNode()], ''
        for i, c in enumerate(s):
            if c == ')': 
                stack.pop()
            
            # get cur node
            elif c != '(':
                num += c
                if i+1 == len(s) or not s[i+1].isdigit():
                    cur = TreeNode(int(num))
                    if stack[-1].left:
                        stack[-1].right = cur
                    else:
                        stack[-1].left = cur
                    stack.append(cur)
                    num = ''
            
        return stack[0].left

        # """
        # recursive solution
        # """
    #     if not s or len(s) == 0:
    #         return None
    #     root, _ = self.helper(s, 0)
    #     return root
    
    # def helper(self, s, i):
    #     start = i
    #     while i < len(s) and (s[i].isdigit() or s[i] == '-'):
    #         i += 1
    #     node = TreeNode(int(s[start:i]))
    #     if i < len(s) and s[i] == '(':
    #         i += 1 # skip (
    #         node.left, i = self.helper(s, i)
    #         i += 1
    #     if i < len(s) and s[i] == '(':
    #         i += 1
    #         node.right, i = self.helper(s, i)
    #         i += 1
    #     return node, i
                