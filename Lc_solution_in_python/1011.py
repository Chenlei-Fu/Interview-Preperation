from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            mid = l + (r - l) // 2
            if self.feasible(weights, days, mid):
                r = mid
            else:
                l = mid + 1
        return l

    def feasible(self, weights, days, capacity):
        day, tmp = 1, 0
        for weight in weights:
            tmp += weight
            if tmp > capacity:  # too heavy, wait for the next day
                day += 1
                tmp = weight
            if day > days:
                return False
        return True