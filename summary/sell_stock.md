# Stock Problems

* Leetcode Questions:

1. [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/#/description)
2. [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/#/description)
3. [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/#/description)
4. [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/#/description)
5. [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/#/description)
6. [714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/)

* Content

  * [Overview](#Overview)
  * [121. Best Time to Buy and Sell Stock](#121. Best Time to Buy and Sell Stock (Easy))

  * [122. Best Time to Buy and Sell Stock II](#122. Best Time to Buy and Sell Stock II (Easy))

  * [123. Best Time to Buy and Sell Stock III](#123. Best Time to Buy and Sell Stock III (Hard))

  * [188. Best Time to Buy and Sell Stock IV](#188. Best Time to Buy and Sell Stock IV (Hard))

  * [309. Best Time to Buy and Sell Stock with Cooldown](#309. Best Time to Buy and Sell Stock with Cooldown (Medium))

  * [714. Best Time to Buy and Sell Stock with Transaction Fee](#714. Best Time to Buy and Sell Stock with Transaction Fee (Medium))





### Overview



**General Case**

Let `T[i][k]` denotes the maximum profit that could be gained at the end of the `ith` day with at most `k` transactions. Since we have **buy, sell, rest** three states, `T[i][k]` should be split into two: `T[i][k][0]` and `T[i][k][1]`

`T[i][k][0]` the maximum profit at the end of the `i-th` day with at most `k` transactions and with `0` stock in our hand AFTER taking the action (手中没有股票)

`T[i][k][1]` the maximum profit at the end of the `i-th` day with at most `k` transactions and with `1` stock in our hand AFTER taking the action (手中有股票)

**Base Cases:**

```python
T[-1][k][0] = 0 # no stock
T[-1][k][1] = -infinity # since we cannot have 1 stock if there is no stock available
T[i][0][0] = 0 # no stock and transaction
T[i][0][1] = -infinity # since we cannot have 1 stock if there is no transaction is allowed
```



**State Translation Function:**

```python
T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
```

* the action taken on `ith` day is rest

  keep the same as `i-1th` dat

* the action taken on `ith` day is sell

  We should have stock yesterday: `T[i-1][k][1]`, and we sell this stock on `ith` day



```python
T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i])
```

* the action taken on `ith` day is rest

  keep the same as `i-1th` dat

* the action taken on `ith` day is buy

  We should **not** have stock yesterday: `T[i-1][k-1][0]`, and we buy this stock on `ith` day

  Keep in mind that we need to decline the number of transition on the `i-1 th` day.



**Note** that the maximum number of allowable transactions remains the same, due to the fact that a transaction consists of two actions coming as a pair -- **buy** and **sell**. Only action **buy** will change the maximum number of transactions allowed.

(Alternatively, we can choose only **sell** as the option)



The pseudo code would be:

```python
for price in prices:
  T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
  T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i])
return T[i][k][0]
```



### 121. Best Time to Buy and Sell Stock (Easy)

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`

**Example 1:**

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```



**Solution 1:**

```python
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        min_price -> keep the minimum price
        profit -> keep the max profit
        """
        if len(prices) <= 1:
            return 0
        min_price, profit = sys.maxsize, -1
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit
```



**Solution 2:**

If we use the general case, we define `k = 1`

The state transition function:

```python
T[i][1][0] = max(T[i-1][1][0], T[i-1][1][1] + prices[i])
T[i][1][1] = max(T[i-1][1][1], T[i-1][0][0] - prices[i]) = max(T[i-1][1][1], - prices[i])
```



That is, we only have two state: `T[i][1][0]` and `T[i][1][1]`, so we can simplify the array as two single variable `T_i10` and `T_i11`

```python
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        T_i10, T_i11 = 0, -sys.maxsize
        for price in prices:
            T_i10 = max(T_i10, T_i11 + price) # rest or sell
            T_i11 = max(T_i11, -price) # rest or buy
        return T_i10
```





### 122. Best Time to Buy and Sell Stock II (Easy)

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



**Example:**

```
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
```



**Solution 1:**

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                res += prices[i+1] - prices[i]
        return res
```



**Solution 2:**

Since `k` can be infinity, the state `k` can be deleted.

The state transition function:

```python
T[i][0] = max(T[i-1][0], T[i-1][1] + prices[i])
T[i][1] = max(T[i-1][1], T[i-1][0] - prices[i])
```



That is, we only have two state: `T[i][0]` and `T[i][1]`, so we can simplify the array as two single variable `T_i0` and `T_i1`



```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        T_i0, T_i1 = 0, -sys.maxsize
        for price in prices:
            T_i0_old = T_i0
            T_i0 = max(T_i0, T_i1 + price) # rest or sell
            T_i1 = max(T_i1, T_i0_old-price) # rest or buy
        return T_i0
```





### 123. Best Time to Buy and Sell Stock III (Hard)

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

Find the maximum profit you can achieve. You may complete **at most two transactions**.

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

**Example:**

```
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
```



**Solution: **

Similar to the case where `k = 1`, except now we have four variables instead of two on each day: `T[i][1][0]`, `T[i][1][1]`, `T[i][2][0]`, `T[i][2][1]`, and the recurrence relations are:



```
T[i][2][0] = max(T[i-1][2][0], T[i-1][2][1] + prices[i])
T[i][2][1] = max(T[i-1][2][1], T[i-1][1][0] - prices[i])
T[i][1][0] = max(T[i-1][1][0], T[i-1][1][1] + prices[i])
T[i][1][1] = max(T[i-1][1][1], T[i-1][0][0] -prices[i]) = max(T[i-1][1][1], - prices[i])
```



where again we have taken advantage of the base case`T[i][0][0] = 0` for the last equation. The `O(n)` time and `O(1)` space solution is as follows:



```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        T_i10, T_i11 = 0, -sys.maxsize
        T_i20, T_i21 = 0, -sys.maxsize
        for price in prices:
            T_i20 = max(T_i20, T_i21 + price)
            T_i21 = max(T_i21, T_i10 - price)
            T_i10 = max(T_i10, T_i11 + price)
            T_i11 = max(T_i11, -price)
        return T_i20
```





### 188. Best Time to Buy and Sell Stock IV (Hard)

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `ith` day, and an integer `k`.

Find the maximum profit you can achieve. You may complete at most `k` transactions.

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

**Example: **

```
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
```



**Solution: **

A profitable transaction takes at least two days (buy at one day and sell at the other, provided the buying price is less than the selling price). If the length of the `prices` array is `n`, the maximum number of profitable transactions is `n/2` (integer division). After that no profitable transaction is possible, which implies the maximum profit will stay the same. Therefore the critical value of `k` is `n/2`. If the given `k` is no less than this value, i.e., `k >= n/2`, we can extend `k` to positive infinity and the problem is equivalent to **`Case II`**.

For the state transition function:

```
T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i])
```

Since we only have state `T[i][k][0]` and state `T[i][k][1]`, the array can be defined as

```python
T_ik0, T_ik1 = [0] * (k+1), [-sys.maxsize] * (k+1)
```



```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k >= (len(prices) >> 1):
            # k as infity
            T_i0, T_i1 = 0, -sys.maxsize
            for price in prices:
                T_i0_old = T_i0
                T_i0 = max(T_i0, T_i1 + price) # rest or sell
                T_i1 = max(T_i1, T_i0_old-price) # rest or buy
            return T_i0
        
        else:
            T_ik0, T_ik1 = [0] * (k+1), [-sys.maxsize] * (k+1)
            for price in prices:
                for j in range(k, 0, -1):
                    T_ik0[j] = max(T_ik0[j], T_ik1[j] + price)
                    T_ik1[j] = max(T_ik1[j], T_ik0[j-1] - price)
            return T_ik0[k]
```



### 309. Best Time to Buy and Sell Stock with Cooldown (Medium)

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



**Example: **

```
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```



**Solution: **

This case resembles **`infinity k`** very much due to the fact that they have the same `k` value, except now the recurrence relations have to be modified slightly to account for the "**cooldown**" requirement. The original recurrence relations are as below:

```
T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
T[i][k][1] = max(T[i-1][k][1], T[i-1][k][0] - prices[i])
```



But with "cooldown", we cannot buy on the `i-th` day if a stock is sold on the `(i-1)-th` day. Therefore, in the second equation above, instead of `T[i-1][k][0]`, we should actually use `T[i-2][k][0]` if we intend to buy on the `i-th` day. Everything else remains the same and the new recurrence relations are

```
T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
T[i][k][1] = max(T[i-1][k][1], T[i-2][k][0] - prices[i])
```



And here is the `O(n)` time and `O(1)` space solution:

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        T_i0, T_i0_pre, T_i1 = 0, 0, -sys.maxsize
        for price in prices:
            T_i0_old = T_i0
            T_i0 = max(T_i0, T_i1 + price)
            T_i1 = max(T_i1, T_i0_pre - price)
            T_i0_pre = T_i0_old
        return T_i0
```



### 714. Best Time to Buy and Sell Stock with Transaction Fee (Medium)

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day, and an integer `fee` representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

**Example: **

```
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
```



**Solution: **

The state transition function:

```
T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
T[i][k][1] = max(T[i-1][k][1], T[i-1][k][0] - prices[i] + fee)
```



```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        T_i0, T_i1 = 0, -sys.maxsize
        for price in prices:
            T_i0_old = T_i0
            T_i0 = max(T_i0, T_i1 + price)
            T_i1 = max(T_i1, T_i0_old - price - fee)
        return T_i0
```

