class Solution:
    def climbStairs(self, n: int) -> int:
        """
        ways[n] = ways[n-1] + ways[n-2]
        """
        if n <= 2: return n
        ways = [i for i in range(n+1)]
        for i in range(3, n+1):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[n]