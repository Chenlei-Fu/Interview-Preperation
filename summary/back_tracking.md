# Back Tracking
## Content
- [Back Tracking](#back-tracking)
  - [Content](#content)
  - [Combination](#combination)
    - [22. Generate Parentheses](#22-generate-parentheses)
    - [39. Combination Sum](#39-combination-sum)
      - [Follow Ups](#follow-ups)
    - [17. Letter Combinations of a Phone Number](#17-letter-combinations-of-a-phone-number)
  - [Permutations](#permutations)
    - [46. Permutations](#46-permutations)
      - [Follow Ups](#follow-ups-1)
  - [Subsets](#subsets)
    - [78. Subsets](#78-subsets)
      - [Follow Ups](#follow-ups-2)

## Combination

### [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

* Time complexity: O(2^n)
* Space complexity: O(n)

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.buildParenthesis(n, '', res, 0, 0)
        return res
    
    def buildParenthesis(self, n, built, res, open, close):
        if open == n and close == n:
            res.append(built)
            return
        
        if open < n:
            self.buildParenthesis(n, built + '(', res, open + 1, close)
        
        if close < open: # if use close < n, we will have like ())(, which is illegal
            self.buildParenthesis(n, built + ')', res, open, close + 1)
```

**Note**

we don't need to append & remove the last element in built, because when the function tracked back, built will remain the same

(比较省事)



### [39. Combination Sum](https://leetcode.com/problems/combination-sum/description/)

* Time Complexity: (target / avg(candidate)) * len(candidates) ^ (target / avg(candidate)) Or O(2^n) in general
* Space Complexity: O(n)

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.backTracking(candidates, target, 0, [], res)
        return res
        
    def backTracking(self, candidates, target, start, tmp, res):
        if target < 0: 
            return
        if target==0:
            res.append(tmp)
            return
        for i in range(start, len(candidates)):
            self.backTracking(candidates, target-candidates[i], i, tmp + [candidates[i]], res)
```



#### Follow Ups

[40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

No duplicates:

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.backTracking(candidates, target, 0, [], res)
        return res
    
    def backTracking(self, candidates, target, start, path, res):
        if target < 0:
            return
        
        if target == 0:
            res.append(path)
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]: continue # avoid duplicates
            self.backTracking(candidates, target - candidates[i], i+1, path + [candidates[i]], res) # it's i+1!!
```



[216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)

1-9 数字的combination

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.backTracking(k, n, 1, [], res)
        return res
        
    def backTracking(self, k, n, start, path, res):
        if k == 0 and n == 0:
            res.append(path)
            return
        
        if k == 0 or n == 0: #illegal
            return
        
        for i in range(start, 10): # traverse start - 9
            self.backTracking(k-1, n-i, i+1, path + [i], res) #i + 1 since no duplicates
```



### [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

```python
class Solution:
    mapping = {'2': 'abc', '3': 'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res = []
        self.backTracking(digits, 0, '', res)
        return res
    
    def backTracking(self, digits, start, prefix, res):
        if len(prefix) == len(digits):
            res.append(prefix)
            return
        
        for key in self.mapping[digits[start]]:
            self.backTracking(digits, start + 1, prefix + key, res)
```





## Permutations
### [46. Permutations](https://leetcode.com/problems/permutations/)
* Time Complexity: O(n * n!)
  * Since the result contains n! permutations
  * Each time we need to traverse n nums
* Space Complexity: O(n * n!)
  * There is n! output and each has n elements
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backTracking(nums, [], res)
        return res
    
    def backTracking(self, nums, tmp, res):
        if len(tmp) == len(nums):
            res.append(tmp)
            return
        
        for num in nums:
            if num in tmp: continue
            self.backTracking(nums, tmp + [num], res)
```

#### Follow Ups
[47. Permutations II](https://leetcode.com/problems/permutations-ii/)

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backTracking(nums, [], res, [0]*len(nums))
        return res
    
    def backTracking(self, nums, tmp, res, visited):
        if len(tmp) == len(nums):
            res.append(tmp)
            return
        
        for i, num in enumerate(nums):
            if visited[i]: continue
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]: continue
            visited[i] = 1
            self.backTracking(nums, tmp + [num], res, visited)
            visited[i] = 0
```
**Note**
1. we need to sort, or the `nums[i] == nums[i-1]` cannot be applied
2. ```if i > 0 and nums[i] == nums[i-1] and not visited[i-1]: continue` make sure the permutation is in order without duplicates (like `[2,2]`)


## Subsets
### [78. Subsets](https://leetcode.com/problems/subsets/)
* Time Complexity: O(n * 2^n)
* Space Complexity: O(n)
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backTracking(nums, [], res, 0)
        return res
    
    def backTracking(self, nums, tmp, res, start):
        res.append(tmp)
        for i in range(start, len(nums)):
            self.backTracking(nums, tmp + [nums[i]], res, i+1) # not allow duplicates
```

**Method 2: iteration**
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            size = len(res)
            for i in range(size):
                subset = res[i].copy()
                subset.append(num)
                res.append(subset)
        return res
```

#### Follow Ups
[90. Subsets II](https://leetcode.com/problems/subsets-ii/)
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backTracking(nums, [], res, 0)
        return res
    
    def backTracking(self, nums, tmp, res, start):
        res.append(tmp)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]: continue
            self.backTracking(nums, tmp + [nums[i]], res, i + 1)
```



### [698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)

```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total, maxNum = sum(nums), max(nums)
        if total % k != 0 or maxNum > total // k:
            return False
        return self.backTracking(nums, k, 0, total//k, 0, [False] * len(nums))
        
    
    def backTracking(self, nums, k, curSum, expect, start, visited):
        if k == 0:
            return True
        if curSum == expect:
            return self.backTracking(nums, k-1, 0, expect, 0, visited)
        for i in range(start, len(nums)):
            if not visited[i] and curSum + nums[i] <= expect:
                visited[i] = True
                if(self.backTracking(nums, k, curSum + nums[i], expect, i+1, visited)): return True
                visited[i] = False
        return False
```