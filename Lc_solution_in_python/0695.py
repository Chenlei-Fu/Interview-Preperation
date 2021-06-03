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