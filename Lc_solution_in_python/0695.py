class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        method 1: DFS
        """
        count, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                count = max(count, self.dfs(i, j, grid, m, n))
        return count

    def dfs(self, i, j, grid, m, n):
        if not (0 <= i < m) or not (0 <= j < n) or not grid[i][j] == 1:
            return 0

        grid[i][j] = 0  # mark as seen
        left = self.dfs(i, j - 1, grid, m, n)
        right = self.dfs(i, j + 1, grid, m, n)
        up = self.dfs(i - 1, j, grid, m, n)
        down = self.dfs(i + 1, j, grid, m, n)
        return left + right + up + down + 1


# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         """
#         method2: BFS
#         """
#         seen = set()
#         count, m, n = 0, len(grid), len(grid[0])
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1 and (i, j) not in seen:
#                     count = max(count, self.bfs(i, j, grid, seen, m, n))
#         return count
#
#     def bfs(self, i, j, grid, seen, m, n):
#         def isValid(x, y):
#             if not (0 <= x < m) or not (0 <= y < n):
#                 return False
#             if (x, y) in seen:
#                 return False
#             return grid[x][y] == 1
#
#         seen.add((i, j))
#         queue = deque([(i, j)])
#         count = 1
#         while queue:
#             x, y = queue.popleft()
#             for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
#                 next_x = x + delta_x
#                 next_y = y + delta_y
#                 if not isValid(next_x, next_y):
#                     continue
#
#                 seen.add((next_x, next_y))
#                 queue.append((next_x, next_y))
#                 count += 1
#         return count