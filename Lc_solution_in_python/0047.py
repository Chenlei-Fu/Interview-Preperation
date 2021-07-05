from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backTracking(nums, [], res, [0] * len(nums))
        return res

    def backTracking(self, nums, tmp, res, visited):
        if len(tmp) == len(nums):
            res.append(tmp)
            return

        for i, num in enumerate(nums):
            if visited[i]: continue
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]: continue
            visited[i] = 1
            self.backTracking(nums, tmp + [num], res, visited)
            visited[i] = 0


if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1]))