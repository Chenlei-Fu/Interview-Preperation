from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total, maxNum = sum(nums), max(nums)
        if total % k != 0 or maxNum > total // k:
            return False
        return self.backTracking(nums, k, 0, total // k, 0, [False] * len(nums))

    def backTracking(self, nums, k, curSum, expect, start, visited):
        if k == 0:
            return True
        if curSum == expect:
            return self.backTracking(nums, k - 1, 0, expect, 0, visited)
        for i in range(start, len(nums)):
            if not visited[i] and curSum + nums[i] <= expect:
                visited[i] = True
                if (self.backTracking(nums, k, curSum + nums[i], expect, i + 1, visited)): return True
                visited[i] = False
        return False