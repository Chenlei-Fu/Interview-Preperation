# Binary Search

- [Binary Search](#binary-search)
  - [Template](#template)
    - [Bisect - Array bisection algorithm](#bisect---array-bisection-algorithm)
  - [Leetcode Questions](#leetcode-questions)
    - [General Questions](#general-questions)
      - [69. Sqrt(x)](#69-sqrtx)
      - [35. Search Insert Position](#35-search-insert-position)
    - [Advanced Questions](#advanced-questions)
      - [1011. Capacity To Ship Packages Within D Days](#1011-capacity-to-ship-packages-within-d-days)
      - [4. Median of Two Sorted Arrays](#4-median-of-two-sorted-arrays)
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

#### [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i  # 保证len(left_part) == len(right_part)
            if i < m and nums1[i] < nums2[j - 1]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1: return max_left

                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) / 2
```