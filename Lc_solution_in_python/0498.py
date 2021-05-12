import collections
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        d = collections.defaultdict(list)
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                d[i + j].append(matrix[i][j])

        res = []
        for k in range(n + m):
            if k % 2 == 1:
                res += (d[k])
            else:
                res += (d[k][::-1])
        return res