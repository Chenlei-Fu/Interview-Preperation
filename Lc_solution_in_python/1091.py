from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        if grid[0][0]: return -1
        q, level, n = deque([(0, 0)]), 1, len(grid)
        visited = [[0 for _ in range(n)] for _ in range(n)]
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                if visited[x][y]: continue
                if x == n - 1 and y == n - 1:
                    return level
                visited[x][y] = 1
                for x_, y_ in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1), (1, 1), (-1, -1)]:
                    next_x = x + x_
                    next_y = y + y_
                    if not self.isValid(next_x, next_y, grid, visited, n):
                        continue
                    q.append((next_x, next_y))
            level += 1
        return -1

    def isValid(self, x, y, grid, visited, n):
        if not (0 <= x < n) or not (0 <= y < n): return False
        if grid[x][y]: return False
        if visited[x][y]: return False
        return True