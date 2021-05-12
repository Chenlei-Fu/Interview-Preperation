class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        DP
        dp[i][j] = s[i] == s[j] and (j - i + 1) < 3 or dp[i+1][j-1]
        """
        res, n = 0, len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and ((j-i+1) < 3 or dp[i+1][j-1])
                res += dp[i][j]
                
        return res

    #     """
    #     backtracking
    #     """
    #     res = 0
        
    #     for i in range(len(s)):
    #         res += self.isPalindromic(s, i, i+1)
    #         res += self.isPalindromic(s, i, i)
    #     return res
    
    # def isPalindromic(self, s, left, right):
    #     res = 0
    #     while left >= 0 and right < len(s) and s[left] == s[right]:
    #         left -= 1
    #         right += 1
    #         res += 1
    #     return res