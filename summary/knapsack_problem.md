# knapsack problem

## Overview

The **knapsack problem** is a problem in [combinatorial optimization](https://en.wikipedia.org/wiki/Combinatorial_optimization): Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.



#### 0-1 Knapsack

There is only one item of each type, and you can choose to put it or not.

We define an 2-D array `dp[i][j]` which stores the maximum value that can be achieved if the weight of the first `i` item doesn't exceed `j` (前i件物品恰放入一个容量为v的背包可以获得的最大价值). Let `w(i)` to be the weight of `ith` item, `v(i)` to be the value of `ith` item.

There are two cases:

* The `ith` item doesn't added to knapsack

  ```python
  dp[i][j] = dp[i-1][j]
  ```

  

* The `ith` item added to knapsack

  ```python
  dp[i][j] = dp[i-1][j-w[i]] + v[i]
  ```

  

Therefore, the state translation function would be:

```python
dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
```



After optimizing the space complexity. Since the state of `ith` item only related to the `(i-1)th` item, we can defined a 1-D array:

```python
dp[j] = max(dp[j], dp[j-w] + v[j])
```



code:

```python
'''
@param weights: array stores weights for N items
@param values: array stores values for N items
@param total_weights: volume of the knapsack
@param N: number of items
@return: the number of items
'''
def knapsack_demo(weights, values, total_weights, N):
    dp = [0] * (total_weights + 1)
    for i in range(N):
        w, v = weights[i], values[i]
        for j in range(total_weights, w-1, -1): # 要倒序，因为j depends on (j-1)
            dp[j] = max(dp[j], dp[j-w] + v)
    return dp[total_weights]

weights = [3, 4, 5]
values = [4, 5, 6]
total_weights = 10
N = 3
print(knapsack_demo(weights, values, total_weights, N))
```



#### Unbounded Knapsack (BKP)

Unlike the 01 backpack issue, there are unlimited pieces of each item available.

State Translation Function:

```python
dp[i][j] = max{dp[i-1][j-k*w[i]] + k*v[i] | 0<=k*w[i]<=j}
```

After optimizing the space complexity, the pseudo code would be:

```python
for i=1..N
    for j=0..total_weights
        dp[j] = max(dp[j], dp[j-w] + v) # we only need to change the order of loop
```



## Leetcode Problems

[416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/description/)

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        knapsack problem
        weights: the value of numbers
        values: true/false
        total_weights: sum/2
        N: undefined
        
        dp[j] represents whether i total weights can be represented by the numbers
        dp[j] = dp[j] | dp[j-num]
        
        if some items can be sum up as total_weights, the remaining items can also be sum up as total_weights
        """
        sum_num = sum(nums)
        if(sum_num % 2 != 0):
            return False
        total_weights = sum_num//2
        dp = [0] * (total_weights + 1)
        dp[0] = 1 # since empty 
        
        for num in nums:
            for j in range(total_weights, num-1, -1):
                dp[j] = dp[j] or dp[j - num]
        return dp[total_weights]
```

