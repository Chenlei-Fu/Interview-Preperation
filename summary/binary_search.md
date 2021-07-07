# Binary Search

## Template
Minimize k , s.t. condition(k) is True
```python
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

### Bisect - Array bisection algorithm
```python
import bisect

# locate the insertion point for x in a to maintain sorted order
# if x is already present in a, the inertion point will be left of any existing entries
bisect.bisect_left(a, x, lo=0, hi=len(a))
# Similar to bisect_left(), but returns an insertion point which to the right of any existing entries of x in a.
bisect.bisect_right(a, x, lo=0, hi=len(a))
```


## Leetcode Questions

### General Questions

#### [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x+1
        while l < r:
            mid = l + (r-l)//2
            if mid * mid > x:
                r = mid
            else:
                l = mid + 1
        return l-1 # since l * l > x
```

#### [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l
```

### Advanced Questions
If we can discover some kind of monotonicity, for example, if condition(k) is True then condition(k + 1) is True, then we can consider binary search.

#### [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
If there's still room for the current package, we put this package onto the conveyor belt, otherwise we wait for the next day to place this package. If the total days needed exceeds D, we return False, otherwise we return True.

```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            mid = l + (r-l)//2
            if self.feasible(weights, days, mid):
                r = mid
            else:
                l = mid + 1
        return l
    
    def feasible(self, weights, days, capacity):
        day, tmp = 1, 0
        for weight in weights:
            tmp += weight
            if tmp > capacity: # too heavy, wait for the next day
                day += 1
                tmp = weight
            if day > days:
                return False
        return True
```