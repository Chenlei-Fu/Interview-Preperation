from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        DP
        dp[i][j] the max number of strings that can be formed with i 0's and j 1's
        have to go from bottom right to top left, because If a cell is updated(because s is selected),
        we should be adding 1 to dp[i][j] from the previous iteration (when we were not considering s),
        But If we go from top left to bottom right, we need to use results from this iteration => overcounting
        
        dp[i][j] = max(dp[i][j], dp[i-c['0']][j-c['1']] + 1)
        """
        if not strs:
            return 0
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            c = Counter(s)
            for i in range(m, c['0']-1, -1):
                for j in range(n, c['1']-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-c['0']][j-c['1']] + 1)
        return dp[m][n]
        