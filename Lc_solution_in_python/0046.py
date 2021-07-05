from typing import List


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