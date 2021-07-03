from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            if parent[x] == 0:  # if no parent, return itself
                return x
            parent[x] = find(parent[x])  # if have parent, find it
            return parent[x]

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx == ry:
                return False
            parent[rx] = ry
            return True

        parent = [0] * len(edges)
        for x, y in edges:
            if not union(x - 1, y - 1):  # if not, parent array will out of range
                return [x, y]

        raise ValueError('illegal input')