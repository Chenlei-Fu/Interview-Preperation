# https://leetcode.com/problems/find-root-of-n-ary-tree/
# Author: chenlei fu
# time complexity: O(N)
# space complexity: O(1)


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        # serialized in level order
        if not tree:
            return None

        total = 0
        for node in tree:
            total += node.val - sum(child.val for child in node.children)
        for node in tree:
            if node.val == total:
                return node
        return None