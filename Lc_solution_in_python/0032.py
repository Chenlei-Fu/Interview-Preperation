class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        DP with stack
        DP[i]: longest valid parentheses of s[0:i]
        """
        dp, stack = [0] * (len(s) + 1), []
        for i, p in enumerate(s):
            if p == '(':
                stack.append(i)
            elif stack:
                j = stack.pop()
                dp[i+1] = dp[j] + (i-j)+1 # tricky thing: assign to the next index
        return max(dp)
        
        """
        pure dp (no stack)
        dp[i], it stores the longest length of valid parentheses which is end at i.
        """
        dp, res = [0] * len(s), 0
        for i in range(1, len(s)):
            if s[i] == ')':
                # case 1: ()()
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2 if dp[i-2] else 2
                
                # case 2: (()())
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2] if i-dp[i-1]-2 >= 0 else dp[i-1] + 2

            res = max(res, dp[i])
        return res
        
        """
        pure stack
        """
        res, stack = 0, [-1]
        for i, p in enumerate(s):
            if p == ')' and stack and stack[-1] >= 0 and s[stack[-1]] == '(':
                stack.pop() #remove this parentheses
                res = max(res, i - stack[-1])
            else: stack.append(i)
        return res