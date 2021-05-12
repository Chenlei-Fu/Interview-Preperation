class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        DP
        dp[i] = dp[i] + dp[i-coin]
        i is the amount, dp[i] is the total ways of changes
        
        完全背包问题
        dp[i][j] : the number of combinations to make up amount j by using the first i types of coins
        State transition:

        1. not using the ith coin, only using the first i-1 coins to make up amount j, then we have dp[i-1][j] ways.
        2. using the ith coin, since we can use unlimited same coin, we need to know how many ways to make up amount j - coins[i-1] by using first i coins(including ith), which is dp[i][j-coins[i-1]]
        dp[i][j] = dp[i-1][j] + (j >= coins[i-1] ? dp[i][j-coins[i-1]] : 0)
        然后优化空间
        
        dp[i] += dp[i - coin]
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i - coin]
        return dp[amount]