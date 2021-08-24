# Dynamic Programming
- [Dynamic Programming](#dynamic-programming)
  - [Fibonacci Number](#fibonacci-number)
    - [70. Climbing Stairs](#70-climbing-stairs)
    - [198. House Robber](#198-house-robber)

## Fibonacci Number

### [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        dp[n] = dp[n-1] + dp[n-2]
        """
        if n <= 2: return n
        dp = [i for i in range(n+1)]
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
```
**Optimization**
How to optimize the space complexity?
Since `dp[n]` only related to `dp[n-1]` and `dp[n-2]`, we can just use two varaibles to store the values

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        dp[n] = dp[n-1] + dp[n-2]
        """
        if n <= 2: return n
        dp_n1, dp_n2 = 2, 1
        for i in range(3, n+1):
            cur = dp_n2 + dp_n1
            dp_n2 = dp_n1
            dp_n1 = cur
        return cur
```

### [198. House Robber](https://leetcode.com/problems/house-robber/)
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[i] = max(dp[i-2] + nums[i], nums[i], dp[i-1])
        """
        dp = nums
        for i, num in enumerate(nums):
            if i == 0: continue
            elif i <= 1:
                dp[i] = max(dp[i], dp[i-1])
            else:
                dp[i] = max(dp[i], dp[i-1], dp[i-2] + num)
        return dp[len(nums)-1]
```

**Optimization**
* Time Complexity: `O(n)`
* Space Complexity: `O(1)`
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        """
        pre2, pre1 = 0, 0
        for i, num in enumerate(nums):
            cur = max(pre2 + num, pre1)
            pre2 = pre1
            pre1 = cur
        return cur
```

**Follow Ups**
[213. House Robber II](https://leetcode.com/problems/house-robber-ii/)

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]
        return max(self.helper(nums, 0, n-2), self.helper(nums, 1, n-1))
    
    def helper(self, nums, begin, end):
        pre2, pre1 = 0, 0
        for i in range(begin, end + 1):
            cur = max(pre2 + nums[i], pre1)
            pre2 = pre1
            pre1 = cur
        return cur
```