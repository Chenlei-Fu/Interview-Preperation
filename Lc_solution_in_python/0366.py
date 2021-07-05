# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.height(root, res)
        return res

    def height(self, root, res):
        if not root: return -1
        level = 1 + max(self.height(root.left, res), self.height(root.right, res))
        if len(res) == level: res.append([])
        res[level].append(root.val)
        return level



if __name__ == '__main__':
    s = Solution()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left, a.right = b, c
    b.left, b.right = d, e
    print(s.findLeaves(a))