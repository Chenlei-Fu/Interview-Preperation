from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backTracking(nums, [], res, 0)
        return res

    def backTracking(self, nums, tmp, res, start):
        res.append(tmp)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]: continue
            self.backTracking(nums, tmp + [nums[i]], res, i + 1)