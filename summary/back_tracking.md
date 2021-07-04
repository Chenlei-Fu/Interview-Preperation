# Back Tracking

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



### [Combination Sum](https://leetcode.com/problems/combination-sum/description/)

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

