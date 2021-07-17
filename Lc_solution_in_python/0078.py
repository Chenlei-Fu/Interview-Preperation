from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backTracking(nums, [], res, 0)
        return res

    def backTracking(self, nums, tmp, res, start):
        res.append(tmp)
        for i in range(start, len(nums)):
            self.backTracking(nums, tmp + [nums[i]], res, i + 1)  # not allow duplicates
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = [[]]
#         for num in nums:
#             size = len(res)
#             for i in range(size):
#                 subset = res[i].copy()
#                 subset.append(num)
#                 res.append(subset)
#         return res