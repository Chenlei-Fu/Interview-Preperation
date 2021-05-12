# https://leetcode.com/problems/kth-missing-positive-number/
# Author: chenlei fu
# time complexity: O(LogN)
# space complexity: O(1)


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # binary search
        # arr = [2,3,4,7,11], k = 5
        # arr[2] - (2+1) = 1 -- miss 1 in pos 3
        # we find the pos that arr[pos] - (pos + 1) == k

        l, r = 0, len(arr) # be careful about the right edge
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] - (mid + 1) < k:
                l = mid + 1
            else:
                r = mid
        return l + k
