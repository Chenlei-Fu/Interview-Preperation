class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        if not grid or not grid[0]:
            return 0

        count, n, m = 0, len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':  # go deeper
                    self.dfs(grid, i, j, n, m)
                    count += 1
        return count

    def dfs(self, grid, i, j, n, m):
        # illegal cases
        if not (0 <= i < n) or not (0 <= j < m) or grid[i][j] != '1':
            return

        grid[i][j] = '#'  # visited
        self.dfs(grid, i + 1, j, n, m)
        self.dfs(grid, i - 1, j, n, m)
        self.dfs(grid, i, j + 1, n, m)
        self.dfs(grid, i, j - 1, n, m)