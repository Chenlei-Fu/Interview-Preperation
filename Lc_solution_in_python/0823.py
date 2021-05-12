class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp, mod = {}, 10**9 + 7
        arr.sort()
        for a in arr:
            dp[a] = 1
            for b in dp:
                # traverse all smaller values
                if a % b == 0:
                    dp[a] += dp[b] * dp.get(a/b, 0)
        return sum(dp.values()) % mod