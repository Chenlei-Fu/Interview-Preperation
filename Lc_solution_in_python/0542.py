from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Optimization: when reach out '0'
        """
        m, n = len(mat), len(mat[0])
        q, visited = deque([]), set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        self.bfs(mat, q, visited, m, n)
        return mat

    def bfs(self, mat, q, visited, m, n):
        while q:
            x, y = q.popleft()
            for x_, y_ in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_x = x + x_
                next_y = y + y_
                if self.isValid(next_x, next_y, visited, m, n):
                    visited.add((next_x, next_y))
                    q.append((next_x, next_y))
                    mat[next_x][next_y] = mat[x][y] + 1

    def isValid(self, x, y, visited, m, n):
        if not (0 <= x < m) or not (0 <= y < n):
            return False
        if (x, y) in visited:
            return False
        return True